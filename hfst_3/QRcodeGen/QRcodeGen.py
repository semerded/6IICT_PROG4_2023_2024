import tkinter as tk
import qrcode
from PIL import Image

def makeQRcode():
    qrcodeObj = qrcode.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    qrcodeObj.save("test.png")




APP = tk.Tk()

APP.geometry('400x500+440+180')
APP.resizable(height=False, width=False)

APP.title("QR code scanner 5000")

QRcode = tk.Canvas(APP, width = 400, height = 400)      
QRcode.grid(row=0, column=0, rowspan=3, columnspan=3)    
img = tk.PhotoImage(file="test.png")      
QRcode.create_image(200,200, image=img) 

urlLabel = tk.Label(APP, text="URL")
urlLabel.grid(row=3, column=0)
urlInput = tk.Entry(APP)
urlInput.grid(row=3, column=1, columnspan=2)




APP.mainloop()

