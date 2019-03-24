import upygame as upg
import umachine
import sprite

pixelsManLeft = b'\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x03\x10\x10\x10\x11\x00\
\x00\x03\x10\x00\x00\x12\x00\
\x00\x01\x10\x11\x00\x12\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x00\x01\x11\x11\x00\x01\
\x01\x11\x11\x11\x67\x00\x01\
\x01\x00\x01\x11\x11\x11\x11\
\x01\x00\x01\x11\x11\x00\x00\
\x01\x00\x04\x54\x44\x00\x00\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x00\x00\x10\x11\x11\x00\
\x00\x00\x00\x10\x00\x00\x00\
\x00\x00\x00\x11\x11\x00\x00\
'
pixelsManRight = b'\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x03\x10\x10\x10\x11\x00\
\x00\x03\x10\x00\x00\x12\x00\
\x00\x01\x10\x01\x10\x12\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x00\x01\x11\x11\x00\x01\
\x01\x11\x11\x11\x67\x00\x01\
\x01\x00\x01\x11\x11\x11\x11\
\x01\x00\x01\x11\x11\x00\x00\
\x01\x00\x04\x54\x44\x00\x00\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x01\x11\x10\x10\x00\x00\
\x00\x00\x00\x00\x10\x00\x00\
\x00\x00\x01\x11\x10\x00\x00\
'

pixelsUp = b'\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x03\x10\x10\x10\x12\x00\
\x00\x03\x10\x00\x00\x12\x00\
\x00\x01\x10\x01\x00\x11\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x00\x01\x11\x11\x00\x00\
\x01\x11\x11\x11\x67\x11\x11\
\x01\x00\x01\x11\x11\x00\x01\
\x01\x00\x01\x11\x11\x00\x01\
\x01\x00\x04\x54\x44\x00\x01\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
'


pixelsDead = b'\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x10\x00\x00\x10\x00\
\x00\x01\x10\x70\x70\x12\x00\
\x00\x03\x10\x00\x00\x12\x00\
\x00\x03\x10\x07\x70\x11\x00\
\x01\x00\x10\x00\x00\x10\x00\
\x01\x00\x01\x11\x11\x00\x00\
\x01\x00\x01\x11\x67\x11\x11\
\x01\x11\x11\x11\x11\x00\x01\
\x00\x00\x01\x11\x11\x00\x01\
\x00\x00\x04\x54\x44\x00\x01\
\x00\x00\x01\x11\x11\x00\x00\
\x00\x00\x00\x10\x10\x00\x00\
\x00\x00\x00\x10\x11\x11\x00\
\x00\x00\x00\x10\x00\x00\x00\
\x00\x00\x00\x11\x11\x00\x00\
'

class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 14
        self.h2 = 16
        self.image = upg.surface.Surface(self.w2, self.h2, pixelsManLeft)
        self.rect = self.image.get_rect()
    
        self.rect.x  = 50
        self.rect.y  = 70
        
        self.vx = 0
        self.vy = 0

        self.A  = False
        self.maxHeight = 50
        self.B = 0
        self.minB = 0
        self.maxB = 3
        self.D = False
    
    def handleInput(self):
        """ handle button presses"""
        eventtype = upg.event.poll()
        if eventtype != upg.NOEVENT:
            if eventtype.type== upg.KEYDOWN:
                if eventtype.key == upg.K_LEFT:
                    self.leftButton(True)
                if eventtype.key == upg.K_RIGHT:
                    self.rightButton(True)
                if eventtype.key == upg.BUT_A:
                    self.A = True
                    self.aButton(True)
                if eventtype.key == upg.BUT_B:
                    self.bButton(True)
            if eventtype.type== upg.KEYUP:
                if eventtype.key == upg.K_LEFT:
                    self.leftButton(False)
                if eventtype.key == upg.K_RIGHT:
                    self.rightButton(False)
                if eventtype.key == upg.BUT_A:
                    self.A = False
                    self.aButton(False)  
                if eventtype.key == upg.BUT_B:
                    self.bButton(False)  
                    
    def leftButton(self,button):
        if button == True:
            if self.vy != -3:
                self.image = upg.surface.Surface(self.w2, self.h2, pixelsManLeft)
            if self.B > 0:
                self.vx = -4
                self.rect.y -= 6
                self.B -= 1
            else:
                self.vx = -2
        else:
            self.vx = 0
    
    def rightButton(self,button):
        if button == True:
            if self.vy != -3:
                self.image = upg.surface.Surface(self.w2, self.h2, pixelsManRight)
            if self.B > 0:
                self.vx = 4
                self.rect.y -= 6
                self.B -=1
            else:
                self.vx = 2
        else:
            self.vx = 0
            
    def aButton(self,button):
        """ a moves you forward """
        if button == True:
            self.vy = -3
            self.image = upg.surface.Surface(self.w2, self.h2, pixelsUp)
            return 0
        else:
            self.image = upg.surface.Surface(self.w2, self.h2, pixelsManLeft)
            self.vy = 0
            return 0
            
    def bButton(self,button):
        """b adds a boost"""
        if button == True:
            if self.B < self.maxB and self.vx == 0:
                self.B += 1
                return 0

    def update(self):
        if self.D == True:
            self.image = upg.surface.Surface(self.w2, self.h2, pixelsDead)
        else:
            self.handleInput()
            # if your within the screen bounds change velocity
            if (self.rect.x + self.vx) <= 105 and (self.rect.x + self.vx) >= -10:
                self.rect.x = self.rect.x + self.vx
                # deal with the forward boosting
                if self.rect.y > self.maxHeight:
                    self.rect.y = self.rect.y + self.vy
                if self.rect.y < 70 and self.A == False:
                    #print("hi")
                    self.rect.y = self.rect.y + 1
    
            #print number of boosts you have available
            umachine.draw_text(0,0,str(self.B),5)
        