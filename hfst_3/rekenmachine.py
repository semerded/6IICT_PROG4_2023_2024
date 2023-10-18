import tkinter as tk
from functools import partial

APP = tk.Tk()

APP.title("kakulator")

standaardKnop = {
    "master": APP,
    "padx": 50,
    "pady": 50,
}
uitkomst = tk.Label(APP, text="", fg="red", pady=50, font=("Helvetica bold", 40))
uitkomst.grid(row=0, column=0, columnspan=4)

class buttonPressed:
    def __init__(self) -> None:
        self.invulling = ""
        self.type = ""
    def __displayUpdate__(self):
        uitkomst.config(text=self.invulling)
        
    def k0(self):
        self.invulling += "0"
        self.__displayUpdate__()
    def k1(self):
        self.invulling += "1"
        self.__displayUpdate__()
    def k2(self):
        self.invulling += "2"
        self.__displayUpdate__()
    def k3(self):
        self.invulling += "3"
        self.__displayUpdate__()
    def k4(self):
        self.invulling += "4"
        self.__displayUpdate__()
    def k5(self):
        self.invulling += "5"
        self.__displayUpdate__()
    def k6(self):
        self.invulling += "6"
        self.__displayUpdate__()
    def k7(self):
        self.invulling += "7"
        self.__displayUpdate__()
    def k8(self):
        self.invulling += "8"
        self.__displayUpdate__()
    def k9(self):
        self.invulling += "9"
        self.__displayUpdate__()
    def kp(self):
        if self.invulling != "":
            if self.type != "":
                self.invulling = self.invulling[:-1]
            self.type = "+"   
            self.invulling += "+"
            self.__displayUpdate__()

    def km(self):
        if self.invulling != "":
            if self.type != "":
                self.invulling = self.invulling[:-1]
            self.type = "-"
            self.invulling += "-"
            self.__displayUpdate__()
            
    def kv(self):
        if self.invulling != "":
            if self.type != "":
                self.invulling = self.invulling[:-1]
            self.type = "*"
            self.invulling += "*"
            self.__displayUpdate__()
        
    def kd(self):
        if self.invulling != "":
            if self.type != "":
                self.invulling = self.invulling[:-1]
            self.type = "/"
            self.invulling += "/"
            self.__displayUpdate__()
        
    def kdecimaal(self):
        self.invulling += "."
        self.__displayUpdate__()
        
    def bkspc(self):
        flags = ["+", "-", "*", "/"]
        if self.invulling[-1:] in flags:
            self.type = ""
        self.invulling = self.invulling[:-1]
        self.__displayUpdate__()
        
    def c(self):
        self.invulling = ""
        self.type = ""
        self.__displayUpdate__()
        
    def ksolve(self):
        if self.type != "":
            if self.invulling[-2:] == "/0":
                self.invulling = "jij bent een snul"
                self.__displayUpdate__()
                self.invulling = ""
                self.type = ""
            else:
                lijst = self.invulling.split(self.type)
                if self.type == "+":
                    self.invulling = float(lijst[0]) + float(lijst[1])
                elif self.type == "-":
                    self.invulling = float(lijst[0]) - float(lijst[1])
                elif self.type == "*":
                    self.invulling = float(lijst[0]) * float(lijst[1])
                elif self.type == "/":
                    self.invulling = float(lijst[0]) / float(lijst[1])
                self.invulling = str(self.invulling)
                if self.invulling[-2:] == ".0":
                    self.invulling = self.invulling[:-2]
                self.__displayUpdate__()
                self.type = ""
            

    
action = buttonPressed()
        
knop0 = tk.Button(APP, padx=108, pady=50, text="0", command=action.k0)
knop0.grid(row=5, column=0, columnspan=2)
knop1 = tk.Button(**standaardKnop, text="1", command=action.k1)
knop1.grid(row=4, column=0)
knop2 = tk.Button(**standaardKnop, text="2", command=action.k2)
knop2.grid(row=4, column=1)
knop3 = tk.Button(**standaardKnop, text="3", command=action.k3)
knop3.grid(row=4, column=2)
knop4 = tk.Button(**standaardKnop, text="4", command=action.k4)
knop4.grid(row=3, column=0)
knop5 = tk.Button(**standaardKnop, text="5", command=action.k5)
knop5.grid(row=3, column=1)
knop6 = tk.Button(**standaardKnop, text="6", command=action.k6)
knop6.grid(row=3, column=2)
knop7 = tk.Button(**standaardKnop, text="7", command=action.k7)
knop7.grid(row=2, column=0)
knop8 = tk.Button(**standaardKnop, text="8", command=action.k8)
knop8.grid(row=2, column=1)
knop9 = tk.Button(**standaardKnop, text="9", command=action.k9)
knop9.grid(row=2, column=2)
knopBackSpace = tk.Button(**standaardKnop, text="<XX", command=action.bkspc)
knopBackSpace.grid(row=1, column=3)
knopC = tk.Button(**standaardKnop, text="C", command=action.c)
knopC.grid(row=1, column=0)
knopDecimaal = tk.Button(**standaardKnop, text=".", command=action.kdecimaal)
knopDecimaal.grid(row=5, column=2)
knopUitkomst = tk.Button(APP, padx=50, pady=112, text="=", command=action.ksolve)
knopUitkomst.grid(row=4, column=3, rowspan=2)
knopOptellen = tk.Button(**standaardKnop, text="+", command=action.kp)
knopOptellen.grid(row=3, column=3)
knopAftrekken = tk.Button(**standaardKnop, text="-", command=action.km)
knopAftrekken.grid(row=2, column=3)
knopVermenigvuldigen = tk.Button(**standaardKnop, text="*", command=action.kv)
knopVermenigvuldigen.grid(row=1, column=2)
knopDelen = tk.Button(**standaardKnop, text="/", command=action.kd)
knopDelen.grid(row=1, column=1)





APP.mainloop()