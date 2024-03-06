from particles.base_particle import BaseParticle
from colors import Colors
from random import randint
import globals

bouncingColors: list[globals.RGBcolor] = [Colors.YELLOW, Colors.BLUE]

class BouncingParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        self.currentColor = randint(0, 1)
        super().__init__(speed, bouncingColors[self.currentColor])
        
    def place(self):
        if self.currentPostition[0] < 5 or self.currentPostition[0] > globals.appWidth - 5:
            self.xMovement *= -1
            self._changeColorWhenWallTouched()
        if self.currentPostition[1] < 5 or self.currentPostition[1] > globals.appHeight - 5:
            self.yMovement *= -1
            self._changeColorWhenWallTouched()
        if self.checkForOutOfBounds():
            self.reset()
        self.basePlace()
            
    def _changeColorWhenWallTouched(self):
        self.currentColor = 0 if self.currentColor == 1 else 1
        self.changeColor(bouncingColors[self.currentColor])
            