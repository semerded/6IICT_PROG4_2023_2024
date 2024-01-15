from particles.base_particle import BaseParticle
from colors import Colors

class BoringParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        super().__init__(speed, Colors.WHITE)
        
    def place(self):
        self.basePlace()
        if self.checkForOutOfBounds():
            self.reset()