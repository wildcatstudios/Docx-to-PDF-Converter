import tkinter as tk
from docx2pdf import convert
import os
from tkinter import filedialog

root= tk.Tk()
root.title("Doc To Pdf Converter")

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

root.iconbitmap(default= "icon.png")

label1 = tk.Label(root, text='Doc to Pdf Converter')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 45, window=label1)

label2 = tk.Label(root, text='Choose Your Docx File :')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)


def path_name():
    path_file = filedialog.askopenfilename()
    path = path_file
    button2 = tk.Button(text='Convert', command=lambda: converted(path), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 210, window=button2)
    def converted(path):
        convert(path)
        convert(path,"output.pdf")
        convert("d://")
        label5 = tk.Label(root, text= "Conversion is complete",font=('helvetica', 10))
        canvas1.create_window(200, 260, window=label5)
    
    
button1 = tk.Button(text='Browse Your File', command=path_name, bg='grey', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 150, window=button1)

root.mainloop()
