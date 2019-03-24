# Enemies.py
import sprite
import upygame as upg

cometPixels = b'\
\x00\x04\x00\
\x00\x04\x00\
\x00\x44\x00\
\x00\x44\x00\
\x04\x74\x40\
\x04\x11\x40\
\x01\x11\x10\
\x11\x11\x11\
\x01\x11\x10\
\x00\x11\x00\
'

rocketPixelsL = b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\
\x00\x01\x21\x11\x51\x11\x31\x11\x11\x17\x00\
\x01\x11\x12\x11\x15\x11\x13\x11\x11\x17\x70\
\x11\x11\x12\x11\x15\x11\x13\x1e\x11\x77\x77\
\x01\x11\x12\x11\x15\x11\x13\x11\x11\x17\x40\
\x00\x01\x21\x11\x51\x11\x31\x11\x11\x17\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\
'
rocketPixelsR = b'\
\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x41\x11\x11\x1c\x11\x1b\x11\x14\x10\x00\
\x07\x71\x11\x11\xc1\x11\xb1\x11\x41\x11\x10\
\x74\x77\x11\x51\xc1\x11\xb1\x11\x41\x11\x11\
\x07\x71\x11\x11\xc1\x11\xb1\x11\x41\x11\x10\
\x00\x71\x11\x11\x1c\x11\x1b\x11\x14\x10\x00\
\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\
'

ufoPixels = b'\
\x00\x00\x00\x00\x66\x66\x00\x00\x00\x00\
\x00\x00\x00\x06\x05\x55\x60\x00\x00\x00\
\x00\x00\x00\x60\x05\x05\x06\x00\x00\x00\
\x00\x00\x00\x60\x05\x55\x06\x00\x00\x00\
\x00\x00\x00\x60\x05\x00\x06\x00\x00\x00\
\x00\x11\x11\x11\x11\x11\x11\x11\x11\x00\
\x01\x12\x21\x17\x71\x1b\xb1\x1a\xa1\x10\
\x11\x12\x21\x17\x71\x1b\xb1\x1a\xa1\x11\
\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\
\x01\x11\x11\x11\x11\x11\x11\x11\x11\x10\
\x00\x00\x33\x33\x33\x33\x33\x33\x00\x00\
'

class comet(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 6
        self.h2 = 10
        
        self.image = upg.surface.Surface(self.w2, self.h2, cometPixels)
        self.vx = 0
        self.vy = 1
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        
class rocketLeft(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 22
        self.h2 = 7
        
        self.image = upg.surface.Surface(self.w2, self.h2, rocketPixelsL)
        self.vx = -2
        self.vy = 0
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx

class rocketRight(rocketLeft):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 22
        self.h2 = 7
        self.image = upg.surface.Surface(self.w2, self.h2, rocketPixelsR)
        self.vx = 2
        self.vy = 0
        self.rect = self.image.get_rect()

class ufo(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.w2 = 20
        self.h2 = 11
        
        self.image = upg.surface.Surface(self.w2, self.h2, ufoPixels)
        self.vx = 1
        self.vy = 1
        self.rect = self.image.get_rect()
        self.time = 0
        self.timeSwitch = 15
        
    def update(self):
        self.time += 1
        self.rect.y += self.vy
        if self.time < self.timeSwitch:
            self.rect.x += self.vx
        else:
            self.rect.x -= self.vx
        if self.time == 2* self.timeSwitch:
            self.time = 0
        
        
        
        
        
        
        
        