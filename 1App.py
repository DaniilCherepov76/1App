from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title ("Mini app")
window.geometry("720x360")
window.resizable(True, True)

last_num = []
                                #defs#
def size5_chek():
    if len(last_num)==5 :
        last_num.clear()

def rand_int():
    num = random.randint(1,10)
    messagebox.showinfo(None, num)
    last_num.insert(0, num)
    history.config(text=' '.join(map(str, last_num)))
    size5_chek()
                              #Elements#
lbl = Label(window,
            text='Добавить число',
            font=('Arial bold', 16),
            fg='black',                  # Цвет текста
            bg='white')                # Цвет фона
lbl.place(x=290, y=25)

history = Label(window,
            text=' ',
            font=('Arial bold', 22),
            fg='black',
            width=12,
            height=1,                  # Цвет текста
            bg='green')                # Цвет фона
history.place(x=290, y=290)


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
