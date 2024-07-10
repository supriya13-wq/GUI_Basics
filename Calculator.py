from tkinter import *

root=Tk()

def print_no(n):
    current = result_label['text']
    new = str(current) + str(n)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

first_number=None
second_number=None
operator=None
def operators(op):
    global first_number,operator
    first_number=int(result_label['text'])
    operator=op
    result_label.config(text='')

def equals(op):
    global first_number,second_number,operator
    second_number=result_label['text']
    if operator=='+':
        result_label.config(text=int(first_number) + int(second_number))
    elif operator=='-':
        result_label.config(text=int(first_number)-int(second_number))
    elif operator=='x':
        result_label.config(text=int(first_number)*int(second_number))
    else:
        result_label.config(text=round(int(first_number)/int(second_number),2))


root.geometry('300x390')
root.resizable(False,False)
root.title('Calculator')
root.configure(background='grey')

result_label = Label(root,text='')
result_label.grid(row=0,column=0,pady=(50,2),columnspan=8,sticky='w')
result_label.config(fg='white',bg='grey',font=('verdana',35))

btn7 = Button(root,text='7',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',15))

btn8 = Button(root,text='8',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',15))

btn9 = Button(root,text='9',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',15))

btn_add = Button(root,text='+',bg='pink',fg='white',width=5,height=2,command=lambda :operators('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',15))

btn4 = Button(root,text='4',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',15))

btn5 = Button(root,text='5',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',15))

btn6 = Button(root,text='6',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',15))

btn_sub = Button(root,text='-',bg='pink',fg='white',width=5,height=2,command=lambda :operators('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',15))


btn1 = Button(root,text='1',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',15))


btn2= Button(root,text='2',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',15))


btn3 = Button(root,text='3',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',15))


btn_mul = Button(root,text='x',bg='pink',fg='white',width=5,height=2,command=lambda :operators('x'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',15))


btn_clear = Button(root,text='C',bg='pink',fg='white',width=5,height=2,command=lambda :clear())
btn_clear.grid(row=4,column=0)
btn_clear.config(font=('verdana',15))


btn0 = Button(root,text='0',bg='pink',fg='white',width=5,height=2,command=lambda :print_no(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',15))


btn_equal = Button(root,text='=',bg='pink',fg='white',width=5,height=2,command=lambda :equals(operator))
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',15))


btn_div = Button(root,text='/',bg='pink',fg='white',width=5,height=2,command=lambda :operators('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',15))

root.mainloop()



