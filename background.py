# background.py
import upygame as upg
import sprite

starPixels1 = b'\
\x01\x00\
\x11\x10\
'

starPixels2 = b'\
\x01\x10\
\x01\x10\
'

starPixels3 = b'\
\x00\x10\
\x00\x00\
'

class background(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 4
        self.h2 = 2
        self.image = upg.surface.Surface(self.w2, self.h2, starPixels1)
        self.rect = self.image.get_rect()
                
        self.rect.x = 0
        self.rect.y = 0
        
        self.startIndex = 0
        self.yLimits = 90-10
        self.index = 1
        self.xPos = 5
        self.indexMax = 4
        
    def update(self):
        """ background needs to slide down screen"""
        self.startIndex += 1
        if(self.startIndex > 16):
            self.startIndex = 1
        # Draw the worm and the grass
        self.index = self.startIndex
        
        for y in range(self.yLimits,0,-4):
            if self.index == self.indexMax:
                # Draw grass in certain places.
                self.rect.x = self.xPos
                self.rect.y = y
            self.index += 1
            if(self.index > 16):
                self.index = 1

class background2(background):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 4
        self.h2 = 2
        self.image = upg.surface.Surface(self.w2, self.h2, starPixels2)
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.startIndex = 0
        self.yLimits = 90-10
        self.index = 1
        self.xPos = 100
        self.indexMax = 8
    
class background3(background):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 4
        self.h2 = 2
        self.image = upg.surface.Surface(self.w2, self.h2, starPixels3)
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.startIndex = 0
        self.yLimits = 90-10
        self.index = 1
        self.xPos = 20
        self.indexMax = 12

class background4(background):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 4
        self.h2 = 2
        self.image = upg.surface.Surface(self.w2, self.h2, starPixels1)
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = 0
        
        self.startIndex = 0
        self.yLimits = 90-10
        self.index = 1
        self.xPos = 70
        self.indexMax = 16



        
        
        
        
