from particles.base_particle import BaseParticle

class BoringParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        super().__init__(speed)
        
    def place(self):
        self.basePlace()
        if self.checkForOutOfBounds():
            self.reset()