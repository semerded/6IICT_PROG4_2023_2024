# Los het spel 'torens van Hanoi' recursief op.

# Uitbreiding: lukt dit in de opdrachtprompt? 
#              Dan kan je het ook in pygame visualiseren.
import gFrame, time
from threading import Thread

app = gFrame.AppConstructor("50dw", "50dh")

DISK_AMOUNT = 3
diskPosition = []
for i in range(DISK_AMOUNT):
    diskPosition.append(1)


def towerOfHanoi(diskNumber: int, from_rod, to_rod, aux_rod):
    if diskNumber == 0:
        return
    towerOfHanoi(diskNumber - 1, from_rod, aux_rod, to_rod)
    moveDisk(diskNumber, to_rod)
    towerOfHanoi(diskNumber - 1, aux_rod, to_rod, from_rod)
    
def drawRod():
    gFrame.Draw.rectangle("24vw", "20vh", "2vw", "80vh", gFrame.Color.BLACK)
    gFrame.Draw.rectangle("49vw", "20vh", "2vw", "80vh", gFrame.Color.BLACK)
    gFrame.Draw.rectangle("74vw", "20vh", "2vw", "80vh", gFrame.Color.BLACK)
    gFrame.Draw.rectangle(0, "80vh", "100vw", "20vh") # grondvalk 

def moveDisk(diskNumber: int, from_rod: int, to_rod: int):
    
    app.requestUpdate()
    time.sleep(0.5)
    
    
def drawDisks():
    
    
Thread(target=towerOfHanoi, args=(3, 1, 3, 2)).start()
    
    
while True:
    app.eventHandler()
    app.fill(gFrame.Color.WHITE)
    
    if app.drawElements():
        drawRod()
        drawDisks()
    
    

towerOfHanoi(3, 1, 3, 2)