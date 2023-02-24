from tkinter import*
import random

def click():
    k=(random.randint(0,2))


root=Tk()
c = Canvas(root, width=400, height=400, bg='white')
c.pack()
a=Button(root, text='Нажми', activebackground='red', command=click).pack()

j=c(80, 80, 80, 80, fill='yellow', outline='green', width=3, activedash=(5, 4))
s=c(100, 10, 20, 90, 180, 90)
o=c(50, 10, 150, 110, width=2) 
k=(j, s, o) 


root.mainloop()
