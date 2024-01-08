import tkinter as tk

APP = tk.Tk()

commonSettings = {
    "padx": 50,
    "pady": 50,
    "text": " "
}

gameDataList = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

class Constructor:
    def __init__(self) -> None:
        self.turn = "X"
        self.gamePlay = False
        
    def __updateTurn__(self):
        self.turn = "O" if self.turn == "X" else "X"
        starter.config(text=self.turn)
        
    def changeStarter(self):
        if self.gamePlay != True:
            self.__updateTurn__()
            
    def knop0(self):
        self.gamePlay = True
        if gameDataList[0][0] == 0:
            gameDataList[0][0] = 1 if self.turn == "X" else 2
            knop0.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop1(self):
        self.gamePlay = True
        if gameDataList[0][1] == 0:
            gameDataList[0][1] = 1 if self.turn == "X" else 2
            knop1.config(text=self.turn)
            
            self.__updateTurn__()
        return True
    def knop2(self):
        self.gamePlay = True
        if gameDataList[0][2] == 0:
            gameDataList[0][2] = 1 if self.turn == "X" else 2
            knop2.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop3(self):
        self.gamePlay = True
        if gameDataList[1][0] == 0:
            gameDataList[1][0] = 1 if self.turn == "X" else 2
            knop3.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop4(self):
        self.gamePlay = True
        if gameDataList[1][1] == 0:
            gameDataList[1][1] = 1 if self.turn == "X" else 2
            knop4.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop5(self):
        self.gamePlay = True
        if gameDataList[1][2] == 0:
            gameDataList[1][2] = 1 if self.turn == "X" else 2
            knop5.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop6(self):
        self.gamePlay = True
        if gameDataList[2][0] == 0:
            gameDataList[2][0] = 1 if self.turn == "X" else 2
            knop6.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop7(self):
        self.gamePlay = True
        if gameDataList[2][1] == 0:
            gameDataList[2][1] = 1 if self.turn == "X" else 2
            knop7.config(text=self.turn)
            self.__updateTurn__()
        return True
    def knop8(self):
        self.gamePlay = True
        if gameDataList[2][2] == 0:
            gameDataList[2][2] = 1 if self.turn == "X" else 2
            knop8.config(text=self.turn)
            self.__updateTurn__()
        return True
CONSTRUCT = Constructor()
    
text = tk.Label(APP, text="3 op een rij!")
PvP = tk.Button(APP, padx=40, pady=20, text="PvP")
PvC = tk.Button(APP, padx=40, pady=20, text="PvC")
starter = tk.Button(APP, padx=40, pady=20, text="X", command=CONSTRUCT.changeStarter)
knop0 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop0)
knop1 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop1)
knop2 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop2)
knop3 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop3)
knop4 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop4)
knop5 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop5)
knop6 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop6)
knop7 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop7)
knop8 = tk.Button(APP, **commonSettings, command=CONSTRUCT.knop8)

text.grid(column=0, row=0, columnspan=3)
PvP.grid(column=0, row=1)
starter.grid(column=1, row=1)
PvC.grid(column=2, row=1)
knop0.grid(column=0, row=2)
knop1.grid(column=1, row=2)
knop2.grid(column=2, row=2)
knop3.grid(column=0, row=3)
knop4.grid(column=1, row=3)
knop5.grid(column=2, row=3)
knop6.grid(column=0, row=4)
knop7.grid(column=1, row=4)
knop8.grid(column=2, row=4)


while True:
    
    
    APP.update()