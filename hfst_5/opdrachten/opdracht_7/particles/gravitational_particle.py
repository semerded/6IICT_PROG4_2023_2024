from particles.base_particle import BaseParticle
from colors import Colors
import globals

class GravitationalParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        super().__init__(speed, (0, 255, 0))
        self.gravity = 0.00005 * speed
    
    def place(self):
        distanceToCenter = ((self.currentPostition[0] - globals.appWidth / 2) ** 2 + (self.currentPostition[1] - globals.appHeight / 2) ** 2) ** 0.5
        print(distanceToCenter)
        
        if self.currentPostition[0] > globals.appWidth / 2:
            self.xMovement -= self.gravity * (globals.appWidth - distanceToCenter)
        else:
            self.xMovement += self.gravity * (globals.appWidth - distanceToCenter)
            
        if self.currentPostition[1] > globals.appHeight / 2:
            self.yMovement -= self.gravity * (globals.appHeight - distanceToCenter) 
        else:
            self.yMovement += self.gravity * (globals.appHeight - distanceToCenter) 
            
        self.currentPostition[0] += self.xMovement / globals.FPS * self.speedMultiplier
        self.currentPostition[1] += self.yMovement / globals.FPS * self.speedMultiplier
                
        self.placeOnScreen()