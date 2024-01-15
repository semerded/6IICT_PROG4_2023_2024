from random import choice
from colors import Colors
from particles.boring_particle import BoringParticle
from particles.bouncing_particle import BouncingParticle
from particles.spinning_particle import SpinningParticle

particleTypes = [BoringParticle, BouncingParticle, SpinningParticle]
# particleTypes = [SpinningParticle]

class ParticleHolder:
    def __init__(self, amountOfParticles: int, speed: int) -> None:
        self.particleList = []
        self.speed = speed
        for _ in range(amountOfParticles):
            self.particleList.append(self._particleBuilder())
        
    def _particleBuilder(self):
        return choice(particleTypes)(self.speed)
        
    def place(self):
        for particle in self.particleList:
            particle.place()