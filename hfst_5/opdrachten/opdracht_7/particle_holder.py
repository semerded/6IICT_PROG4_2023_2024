from colors import Colors
from particle import BoringParticle

class ParticleHolder:
    def __init__(self, amountOfParticles: int, speed: int) -> None:
        self.particleList = []
        self.speed = speed
        for _ in range(amountOfParticles):
            self.particleList.append(self._particleBuilder())
        
    def _particleBuilder(self) -> BoringParticle:
        return BoringParticle(self.speed)
        
    def place(self):
        for particle in self.particleList:
            particle.place()