import pygame, globals, constants, math, random
from colors import Colors

class BaseParticle:
    def __init__(self, speed: int, color: globals.RGBcolor) -> None:
        self.speedMultiplier = speed
        self.color = color
        self._constructor()
        
    def _constructor(self):
        self.speed = random.random() * self.speedMultiplier * 100 / constants.FPS
        if self.speed < self.speedMultiplier / 5:
            self.speed = self.speedMultiplier / 5
        self.angle = random.random()* 360
        self.previousAngle = self.angle
        self._calculateAngle()
        
        self.currentPostition = [300, 300]
            
    def basePlace(self):
        self.update()
        pygame.draw.circle(globals.display, self.color, self.currentPostition, 10)

    def update(self):
        """
        update is called with place method
        """
        if self.angle != self.previousAngle:
            self._calculateAngle()
        
        self.currentPostition[0] += self.xMovement
        self.currentPostition[1] += self.yMovement
        
    def _calculateAngle(self):
        self.xMovement = self.speed * math.cos(self.angle)
        self.yMovement = self.speed * math.sin(self.angle)
        
    def checkForOutOfBounds(self):
        for position in self.currentPostition:
            if position < -10 or position > constants.BREEDTE + 10: # 10 pixel tollerance
                return True
        return False
              
    def reset(self):
        self._constructor()
        
    def changeAngle(self, newAngle: int):
        self.angle = newAngle
        
    def changeSpeed(self, newSpeed: int):
        self.speed = newSpeed
        
    def changeColor(self, newColor: globals.RGBcolor):
        self.color = newColor