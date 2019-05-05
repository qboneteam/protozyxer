from tkinter import *

root = Tk()
root.title("Заголовок окна")
root.geometry("640x480")
canvas = Canvas(root, width=640, height=480, bg='#000000')
canvas.pack()
root.mainloop()