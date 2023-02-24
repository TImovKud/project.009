from tkinter import*

def click():
    a=Label(root, text= width=15, bg='black', fg='cyan', font='consolas').pack

root=Tk()
root.title('Приложение')
root.geometry('500x400')
b=Entry(root, width=10, bg='white', fg='red', font='consolas').pack
btn=Button(root, text='Click', width=15, height=2, bg='white', command=click).pack
root.mainloop()
