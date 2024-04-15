import gFrame

app = gFrame.AppConstructor("50dw", "50dh", gFrame.pygame.RESIZABLE, manualUpdating=True)

startDimensions = ["90vw", "90vh"]
startPosition = ["5vw", "5vh"]
def drawRect(width: gFrame.validScreenUnit, heigth: gFrame.validScreenUnit, x: gFrame.validScreenUnit, y: gFrame.validScreenUnit):
    x, y, width, heigth = gFrame.ScreenUnit.convertMultipleUnits(x, y, width, heigth)
    if width < 10 or heigth < 10:
        return
    gFrame.Draw.border(x, y, width, heigth, 1, gFrame.Color.BLACK)
    drawRect(width * 0.8, heigth * 0.8, x + width * 0.1, y + heigth * 0.1)

while True:
    app.eventHandler()
    app.fill(gFrame.Color.WHITE)
        
    if app.drawElements():
        drawRect(*startDimensions, *startPosition)