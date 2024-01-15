from particles.base_particle import BaseParticle
import globals, constants, random, math

class SpinningParticle(BaseParticle):
    def __init__(self, speed: int) -> None:
        super().__init__(speed, (255, 0,0))
        
    def place(self):
        newAngle = self.angle + random.random() * self.speedMultiplier / constants.FPS
        if newAngle > 360:
            newAngle = 0
        self.changeAngle(newAngle)
        self.changeColor(self._calculateColor())
        self.basePlace()
        
    def _calculateColor(self) -> globals.RGBcolor:
        redValue = abs(math.cos(self.angle)) * 255
        blueValue = abs(math.sin(self.angle)) * 255
        return redValue, 0, blueValue