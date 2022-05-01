from tkinter import *

window = Tk()
window.geometry('500x354')
window.title('Calculator')
window.resizable(0, 0)


def click(item) :
    global expression
    expression += str(item)
    input_text.set(expression)


def clear() :
    global expression
    expression = ""
    input_text.set("")


def equals() :
    try :
        global expression
        rezultat = str(eval(expression))
        input_text.set(rezultat)
        expression = ""
    except Exception :
        expression = ""
        input_text.set("Error! Please click C button")


input_text = StringVar()
expression = ''

input_frame = Frame(window, width=312, height=50, bd=0, highlightcolor='black', highlightbackground='black', bg='grey')
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg='#eee', bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()
frame_button = Frame(window, width=300, height=300, bg='grey')
frame_button.pack()

button_clear = Button(frame_button, text='C', fg='black', width=57, height=3, bd=1, bg='#eee', cursor='hand2',
                      command=lambda : clear()).grid(row=0, column=0, columnspan=3)


def divided_method() :
    Button(frame_button, text='/', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : click('/')).grid(row=0, column=3)


def prod_method() :
    Button(frame_button, text='*', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : click('*')).grid(row=1, column=3)


def number_method() :
    Button(frame_button, text='0', fg='black', width=38, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('0')).grid(row=4, column=0, columnspan=2)

    Button(frame_button, text='1', fg='black', width=19, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('1')).grid(row=3, column=0)
    Button(frame_button, text='2', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('2')).grid(row=3, column=1)
    Button(frame_button, text='3', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('3')).grid(row=3, column=2)
    Button(frame_button, text='4', fg='black', width=19, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('4')).grid(row=2, column=0)
    Button(frame_button, text='5', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('5')).grid(row=2, column=1)
    Button(frame_button, text='6', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('6')).grid(row=2, column=2)
    Button(frame_button, text='7', fg='black', width=19, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('7')).grid(row=1, column=0)
    Button(frame_button, text='8', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('8')).grid(row=1, column=1)
    Button(frame_button, text='9', fg='black', width=18, height=3, bd=1, bg='#eee', cursor='hand2',
           command=lambda : click('9')).grid(row=1, column=2)


def sub_method() :
    Button(frame_button, text='-', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : click('-')).grid(row=2, column=3)


def add_method() :
    Button(frame_button, text='+', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : click('+')).grid(row=3, column=3)


def other_method() :
    Button(frame_button, text=',', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : click('.')).grid(row=4, column=2)
    Button(frame_button, text='=', fg='black', width=18, height=3, bd=1, bg='#FFA500', cursor='hand2',
           command=lambda : equals()).grid(row=4, column=3)


if __name__ == '__main__' :
    divided_method()
    prod_method()
    number_method()
    sub_method()
    add_method()
    other_method()
    window.mainloop()
