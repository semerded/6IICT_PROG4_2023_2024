from particles.base_particle import BaseParticle
from colors import Colors
from random import randint
import constants, globals

bouncingColors: list[globals.RGBcolor] = [Colors.YELLOW, Colors.BLUE]

class BouncingParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        self.currentColor = randint(0, 1)
        super().__init__(speed, bouncingColors[self.currentColor])
        
    def place(self):
        self.basePlace()
        if self.currentPostition[0] < 5 or self.currentPostition[0] > constants.BREEDTE - 5:
            self.xMovement *= -1
            self._changeColorWhenWallTouched()
        if self.currentPostition[1] < 5 or self.currentPostition[1] > constants.HOOGTE - 5:
            self.yMovement *= -1
            self._changeColorWhenWallTouched()
            
    def _changeColorWhenWallTouched(self):
        self.currentColor = 0 if self.currentColor == 1 else 1
        self.changeColor(bouncingColors[self.currentColor])
            