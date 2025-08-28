from simpleeval import simple_eval 
from tkinter import *

root = Tk()
root.geometry('400x330')
root.resizable(0, 0)
root.title('calculator')

#designing the buttons
#creating input field
inputfield = Entry(root, bg='black',font = ('calbri', 16), width=32, borderwidth=5, fg='blue')
inputfield.grid(column=0,row=0)
#creating buttons
#row 1
clear_alls = Button(root, text= 'CLEAR_ALL', bg='blue',font= ('calbri', 16, 'bold'), width= 15, height=1, command= lambda:clear_all())
clear_alls.grid(column=0, row=2, sticky=W)
clear1 = Button(root, text='BACKSPACE', bg='blue', font=('calbri', 16, 'bold'), width= 15, height=1,command = lambda:undo())
clear1.grid(column=0, row=2, sticky=E)


#row 2
seven = Button(root, text='7', bg='blue', font=('calbri', 16, 'bold'), width=11,height=1,command = lambda:a_var(7))
seven.grid(column=0, row=5, sticky=W)
eight= Button(root, text='8', bg='blue', font=('calbri', 16, 'bold'), width=11, height=1,command = lambda:a_var(8))
eight.grid(column=0, row=5)
nine =  Button(root, text='9', bg='blue', font=('calbri', 16, 'bold'), width=10,height=1,command = lambda:a_var(9))
nine.grid(column=0, row=5, sticky=E)

#row 4
six= Button(root, text='6', bg='blue', font=('calbri', 16, 'bold'), width=11, height=1,command = lambda:a_var(6))
six.grid(column=0, row=6, sticky=W)
five= Button(root, text='5', bg='blue', font=('calbri', 16, 'bold'), width=11, height=1,command = lambda:a_var(5))
five.grid(column=0, row=6)
four= Button(root, text='4', bg='blue', font=('calbri', 16, 'bold'), width=10, height=1,command = lambda:a_var(4))
four.grid(column=0, row=6, sticky=E)
#row5
one= Button(root, text='1', bg='blue', font=('calbri', 16, 'bold'), width=11, height=1,command = lambda:a_var(1))
one.grid(column=0, row=7, sticky=W)
two= Button(root, text='2', bg='blue', font=('calbri', 16, 'bold'), width=11, height=1,command = lambda:a_var(2))
two.grid(column=0, row=7)
three= Button(root, text='3', bg='blue', font=('calbri', 16, 'bold'), width=10, height=1,command = lambda:a_var(3))
three.grid(column=0, row=7, sticky=E)
#the signs
dot = Button(root, text='.', bg='blue', font=('calbri', 16, 'bold'), width=11, height= 1,command = lambda:the_operations('.'))
dot.grid(column=0,row= 8,sticky=W)
zero = Button(root, text='0', bg='blue', font=('calbri', 16, 'bold'), width=11, height= 1,command = lambda:a_var(0))
zero.grid(column=0,row= 8)
divide = Button(root, text='/', bg='blue', font=('calbri', 16, 'bold'), width=10, height= 1,command = lambda:the_operations('/'))
divide.grid(column=0,row= 8,sticky=E)
multiply= Button(root, text='*', bg='blue', font=('calbri', 16, 'bold'), width=11, height= 1,command = lambda:the_operations('*'))
multiply.grid(column=0,row= 9,sticky=W)
minus = Button(root, text='-', bg='blue', font=('calbri', 16, 'bold'), width=11, height= 1,command = lambda:the_operations('-'))
minus.grid(column=0,row= 9)
plus = Button(root, text='+', bg='blue', font=('calbri', 16, 'bold'), width=10, height= 1,command = lambda:the_operations('+'))
plus.grid(column=0,row=9,sticky=E)
equal = Button(root, text='=', bg='blue', font=('calbri', 16, 'bold'), width=30, height= 1,command = lambda:equals())
equal.grid(column=0,row= 10, sticky=W)
#creating functions
i = 0
def a_var(num):
        global i
        inputfield.insert(i, num)
        i+=1

def the_operations(operator):
        global i
        length = len(operator)
        inputfield.insert(i, operator)
        i+=length
def clear_all():
        inputfield.delete(0, END)

def undo():
        entire_entry = inputfield.get()
        if len(entire_entry):
                new_entry = entire_entry[:-1]
                clear_all()
                inputfield.insert(0, new_entry)
        else:
                clear_all()
                inputfield.insert(0,'Error')

def equals():
        entire_string = inputfield.get()
        try:
                result = simple_eval(entire_string)
                clear_all()
                inputfield.insert(0, result)
        except Exception:
                clear_all()
                inputfield.insert(0, "Error")



root.mainloop()
