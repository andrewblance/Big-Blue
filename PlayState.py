# PlayState.py
import upygame as upg
import umachine
import globalvars as gv
import changeState as cs
from Player import Player
from background import background, background2, background3, background4
import sprite
from Enemies import comet, rocketLeft, rocketRight, ufo
import urandom as random

class playState():
    def __init__(self):
        self.ticker = 1
        self.frameNum = 0
        self.lastX = 0
        self.deathTimer = 0
        
        self.timer         = [200, 250, 300, 300,  300]
        
        self.cometFreq     = [13,  13,  1,   13,   13] 
        self.cometAmount   = [10,  10,  0,   10,   10]
        
        self.rocketFreqL   = [1,   30,  80,  1,    75] 
        self.rocketAmountL = [0,   1,   1,   0,    1 ]
        
        self.rocketFreqR   = [1,   80,  25,  1,    30] 
        self.rocketAmountR = [0,   1,   1,   0,    1 ]
        
        self.ufoFreq       = [1,   1,   40,  40,   40] 
        self.ufoAmount     = [0,   0,   3,   2,    2 ]
        
    def levelInfo(self):
        """ choose level characteristics """
        index = gv.level - 1
        length = self.timer[index]
        
        numC = self.cometAmount[index]
        freqC = self.cometFreq[index]
        
        numRl  = self.rocketAmountL[index]
        freqRl = self.rocketFreqL[index]
        numRr  = self.rocketAmountR[index]
        freqRr = self.rocketFreqR[index]
        
        numU  = self.ufoAmount[index]
        freqU = self.ufoFreq[index]
        
        return length, numC, freqC, numRl, freqRl, numRr, freqRr, numU, freqU
    
    def cometPlacer(self, freq, group):
        """ place comets at top of screen randomly"""
        if (self.frameNum % freq) == 0:
            for s in group:
                if s.rect.y > 80:
                    s.rect.y = -10
                    x = 10 + random.getrandbits(8) * 90 // 256
                    if abs(x - self.lastX) < 7:
                        if x < self.lastX:
                            x -= 7
                        else:
                            x += 7
                    s.rect.x = x
                    self.lastX = x
                    break
                
    def rocketPlacer(self, freq, group, LR):
        """ place rockets at bottom of the screen """
        if (self.frameNum % freq) == 0:
            for s in group:
                if LR == True:
                    if s.rect.x < -16:
                        s.rect.x = 110
                        if bool(random.getrandbits(1)) == 1:
                            y = 80
                        else:
                            y = 50
                        s.rect.y = y
                        break
                if LR == False:
                    if s.rect.x > 116:
                        s.rect.x = -16
                        if bool(random.getrandbits(1)) == 1:
                            y = 80
                        else:
                            y = 50
                        s.rect.y = y
                        break
                
    def enemyCreator(self,enemyType,n,x,y,groupSmall, en):
        """ add n number of enemies to groups"""
        for i in range(n):
            if enemyType == 1:
                enemy = comet()
            if enemyType ==2:
                enemy = rocketLeft()
            if enemyType ==3:
                enemy = rocketRight()
            if enemyType ==4:
                enemy = ufo()
            enemy.rect.x = x
            enemy.rect.y = y
            groupSmall.add(enemy)
            en.add(enemy)
            
    def updateAndRender(self):
        """main play loop"""
        screen_sf  = upg.display.set_mode()
        
        #create groups for the sprites
        enemy_sprites = sprite.Group()
        nice_sprites = sprite.Group()
        
        #choose correct info for the level
        timer, numC, freqC, numRl, freqRl, numRr, freqRr, numU, freqU = self.levelInfo()
        
        #create comets, rockets and ufo sprites
        all_comets = sprite.Group()
        self.enemyCreator(1,numC,100,100,    all_comets,  enemy_sprites)
        all_rocketsL = sprite.Group()
        self.enemyCreator(2,numRl,-100,-100, all_rocketsL,enemy_sprites)
        all_rocketsR = sprite.Group()
        self.enemyCreator(3,numRr,150,-100,  all_rocketsR,enemy_sprites)
        all_ufo = sprite.Group() 
        self.enemyCreator(4,numU,100,100,    all_ufo,     enemy_sprites)
        
        #create player and background sprites
        player = Player()
        nice_sprites.add(player)
        
        #create background
        bkg1, bkg2, bkg3, bkg4  = background(), background2(), background3(), background4()
        nice_sprites.add(bkg1, bkg2,bkg3, bkg4)
        
        while True:
            #check for collisions
            hit = sprite.spritecollideany(player, enemy_sprites)
            if hit != None:
                player.D = True
                while self.deathTimer < 25:
                    nice_sprites.update()
                    nice_sprites.draw(screen_sf)
                    upg.display.flip()
                    self.deathTimer += 1
                return cs.state(2, gv.level)
            
            #draw the timer
            timer -= self.ticker
            umachine.draw_text(90,0,str(timer),3)
            #when time gets to zero go to next level
            if timer == 0:
                if gv.level < 5:
                    return cs.state(4, gv.level)
                if gv.level ==5:
                   return cs.state(3, gv.level)
                   
            #place the enemies
            self.cometPlacer(freqC, all_comets)
            self.rocketPlacer(freqRl, all_rocketsL, True)
            self.rocketPlacer(freqRr, all_rocketsR, False)
            self.cometPlacer(freqU, all_ufo)
            
            #update sprites and draw 'em
            nice_sprites.update()
            nice_sprites.draw(screen_sf)
            enemy_sprites.update()
            enemy_sprites.draw(screen_sf)
            
            upg.display.flip()
            
            #count framenums
            self.frameNum += 1
            if self.frameNum > 1000000:
                self.frameNum = 0;
   
