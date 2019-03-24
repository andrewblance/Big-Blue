# MainMenuState.py
import umachine
import upygame as upg
import changeState as cs
import globalvars as gv
import gc
from background import background, background2, background3, background4
import sprite

class menuState():
    def __init__(self):
        self.x = [0,10,20]
        self.y = [0,20,30]
        self.text = ["hello world","i", "j"]
        self.colour = [1,2,3]
        self.button = upg.BUT_A
        self.nextState = 1
        self.garbageCollect = False
        self.levelToOne = False
        self.levelPlusOne = False
        self.upOrDown = upg.KEYDOWN
        self.scrollBack = True
    
    def drawText(self):
        for i,j,k,l in zip(self.x, self.y, self.text, self.colour):
            umachine.draw_text(i,j,k,l)
    
    def buttonPress(self):
        eventtype = upg.event.poll()
        if eventtype != upg.NOEVENT:
            if eventtype.type== self.upOrDown:
                if eventtype.key == self.button:
                    if(self.garbageCollect):
                        gc.collect()
                    if(self.levelToOne):
                        gv.level = 1
                    if(self.levelPlusOne):
                        gv.level += 1
                    return True
    
    def updateAndRender(self):
        back_sprites = sprite.Group()
        bkg1, bkg2, bkg3, bkg4  = background(), background2(), background3(), \
                                                    background4()
        back_sprites.add(bkg1, bkg2,bkg3, bkg4)
                
        screen_sf  = upg.display.set_mode()
        while True:
            if(self.scrollBack):
                back_sprites.update()
                back_sprites.draw(screen_sf)
            self.drawText()
            if(self.buttonPress()):
                return cs.state(self.nextState, gv.level)
            upg.display.flip()
        

class mms(menuState):
    def __init__(self):
        self.x = [13, 22, 27, 0 , 0 , \
                  14, 23, 28, 1 , 1 ]
        self.y = [10, 20, 30, 43, 53,  \
                  11, 21, 31, 44, 54 ]
        self.text = ["A engages","forward", "thrusters", "B charges","boosters", \
                     "A engages","forward", "thrusters", "B charges","boosters",]
        self.colour = [7,7,7,2,2,\
                       3,3,3,5,5 ]
        self.button = upg.BUT_A
        self.nextState = 1
        self.garbageCollect = False
        self.levelToOne = False 
        self.levelPlusOne = False
        self.upOrDown = upg.KEYDOWN
        self.scrollBack = True
        
class ds(menuState):
    def __init__(self):
        self.x = [0 , 0 , 0, 0, 0,\
                      1,  1, 1, 1]
        self.y = [10, 20, 30, 40, 70,
                       21, 31, 41, 72]
        self.text = ["you've died!","the spaceman", "hasn't made", "it home..", "A to retry level",\
                                    "the spaceman", "hasn't made", "it home..", "A to retry level"]
        self.colour = [7,2,2,2,2,\
                         3,3,3,3]
        self.button = upg.BUT_A
        self.nextState = 1
        self.garbageCollect = True
        self.levelToOne = False 
        self.levelPlusOne = False
        self.upOrDown = upg.KEYDOWN
        self.scrollBack = True

class gos(menuState):
    def __init__(self):
        self.x = [0 , 0 , 0, 0,     0 ,\
                  1,  1,  1, 1, 26, 1]
        self.y = [0, 10, 20, 30,     70,\
                  1, 11, 21, 31, 61, 71]
        self.text = ["thank you so", "much for", "taking me", "home...",             "b to restart",\
                     "thank you so", "much for", "taking me", "home...", "the end!", "b to restart"]
        self.colour = [2,2,2,2,  10,\
                       5,5,5,5,5,7]
        self.button = upg.BUT_B
        self.nextState = 6
        self.garbageCollect = True
        self.levelToOne = True 
        self.levelPlusOne = False
        self.upOrDown = upg.KEYDOWN
        self.scrollBack = True
 
class ts(menuState):
    def __init__(self):
        self.x = [25, 28, 26,29]
        self.y = [40, 70, 41, 71]
        self.text = ["BIG BLUE", "press A", \
                     "BIG BLUE", "press A"]
        self.colour = [6,6,5,5]
        self.button = upg.BUT_A
        self.nextState = 0
        self.garbageCollect = False
        self.levelToOne = False
        self.levelPlusOne = False  
        self.upOrDown = upg.KEYUP
        self.scrollBack = True

class bl(menuState):
    def __init__(self):
        self.x = [10, 0, 10, 28, \
                  11, 1, 11, 29]
        self.y = [0, 10, 20, 70, \
                  1, 11, 21, 71]
        self.text = ["well done!", "finished", "level: " + str(gv.level), "press A",\
                     "well done!", "finished", "level: " + str(gv.level), "press A"]
        self.colour = [2,5,5,2,\
                       5,2,2,6]
        self.button = upg.BUT_A
        self.nextState = 1
        self.garbageCollect = False
        self.levelToOne = False
        self.levelPlusOne = True  
        self.upOrDown = upg.KEYDOWN  
        self.scrollBack = True


