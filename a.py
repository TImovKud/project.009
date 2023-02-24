from tkinter import*

def click():
    messagebox.showinfo('Заголовок', '{username}'.format(username=username))

root=Tk()
root.title('Приложение')
root.geometry('500x400')
#a=Label(root, text= width=15, bg='black', fg='cyan', font='consolas').pack
b=Entry(root, width=10, bg='white', fg='red', font='consolas').pack
btn=Button(root, text='Click', width=15, height=2, bg='white', command=click).pack
root.mainloop()
