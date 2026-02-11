from tkinter import *
from tkinter import messagebox
import random


def rand_int():
    messagebox.showinfo(None,random.randint(1,10) )


window = Tk()
window.title ("Mini app")
window.geometry("720x360")
window.resizable(True, True)

lbl = Label(window,
            text='Добавить число',
            font=('Arial bold', 16),
            fg='black',                  # Цвет текста
            bg='white')                # Цвет фона
lbl.place(x=290, y=25)


# enter_text = Entry(window,
#                    bg='light green',
#                    width=5, 
#                    font=('Arial', 25)
#                                 )
# enter_text.place(x=300, y=65)


btn_rand = Button(window,
                 text='Случайное число',
                 width=16,
                 height=2,
                 bg='black',
                 fg='white',
                 font=('Arial',20),
                 command=rand_int)
btn_rand.place(x=225, y=110)




window.mainloop()
