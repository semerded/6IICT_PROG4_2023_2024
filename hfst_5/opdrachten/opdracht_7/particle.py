# Voeg eigenschappen / methoden toe aan BoringParticle op basis van de uitleg in de README.
import pygame, globals, constants, math, random
from colors import Colors

class BoringParticle:
    def __init__(self, speed: int) -> None:
        self.speedMultiplier = speed
        self._constructor()
        
    def _constructor(self):
        self.speed = random.random()* 100 * self.speedMultiplier
        self.angle = random.random()* 360
        self.previousAngle = self.angle
        self._calculateAngle()
        
        self.currentPostition = [300, 300]
            
    def place(self):
        self.update()
        pygame.draw.circle(globals.display, Colors.WHITE, self.currentPostition, 10)

    def update(self):
        """
        update is called with place method
        """
        if self.angle != self.previousAngle:
            self._calculateAngle()
        
        self._checkForOutOfBounds()
        self.currentPostition[0] += self.xMovement / constants.FPS
        self.currentPostition[1] += self.yMovement / constants.FPS
        
    def _calculateAngle(self):
        self.xMovement = self.speed * math.cos(self.angle)
        self.yMovement = self.speed * math.sin(self.angle)
        
    def _checkForOutOfBounds(self):
        for position in self.currentPostition:
            if position <-10 or position > 610: # 10 pixel tollerance
                self.reset()
              
    def reset(self):
        self._constructor()
        
    def changeAngle(self, newAngle: int):
        self.angle = newAngle