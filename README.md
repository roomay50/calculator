# calculator
a simple calculator

**#modules used:**
This is a calculator was made using the **tkinter module, and the parser module.** It also made use of global expressions in defining the functions.
from the tkinter module, the Button function was used to create the buttons, and they were arranged by the grid method.
the Entry function also arranged by the grid method, was used to create the entry frame where the numbers appears

**#defined functions:**
five functions were defined to help the buttons work: 
**a_var(num):** this function takes one arguement, a number. So that when the button in which the command for the function is given, it pops upon the entry field
**the_operation(operation):** this also takes one arguement, but this time the arithmetic sign, or the decimal point. if either button is clicked, it displays whats on the button.
**clear_all():** takes no arguement,and wipes every thing on screen when called.
**undo():** takes no arguement, and also erases what is present on the screen from the right whenever it is called
**equals():** this calculates the whole expression in the entry field, and returns the answer.

**#how the functions were used:**
the numbers uses the **a_var(num)** function
the signs use the **the_operations(operation)** function
the clear all and backspace buttons use the **clear_all()** and **undo()** function respectively
and the equals button uses the **equals()** function.

**#layout:**
It consisting of a screen, numbers, undo buttons and the basic arithimetic functions.
**+** for addition,
**-** for subtraction,
**/** for division,
**x** for multiplication,
**=** to calculate the code on the screen.
