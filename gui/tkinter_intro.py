import tkinter
from turtle import width
window = tkinter.Tk()
window.title('GUI Program')
window.minsize(width =500,height=500)
my_label =  tkinter.Label(text = 'my label', font=('Arial', 24))
my_label.pack()


window.mainloop()
