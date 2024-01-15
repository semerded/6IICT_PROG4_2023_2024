from particles.base_particle import BaseParticle
import constants

class BouncingParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        super().__init__(speed)
        
    def place(self):
        self.basePlace()
        if self.currentPostition[0] < 5 or self.currentPostition[0] > constants.BREEDTE - 5:
            self.xMovement *= -1
        if self.currentPostition[1] < 5 or self.currentPostition[1] > constants.HOOGTE - 5:
            self.yMovement *= -1
                