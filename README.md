# Calculator
A simple calculator built with Python. 

## Modules used:
This calculator was created using the **Tkinter** module for the user interface and the **SimpleEval** module for safely evaluating mathematical expressions.  
- **Tkinter** is used to create the buttons, input field, and overall layout.  
- **SimpleEval** is used inside the calculator’s logic to evaluate the expressions entered by the user. This makes the evaluation process both safe and reliable.  

## Defined functions:
The calculator uses a few helper functions to make the buttons work: 
- **`a_var(num)`**: Takes a number as input and inserts it into the entry field.  
- **`the_operations(operation)`**: Takes an arithmetic symbol (like `+`, `-`, `*`, `/`, or `.`) and inserts it into the entry field.  
- **`clear_all()`**: Clears everything in the entry field.  
- **`undo()`**: Works like backspace—removes the last character in the entry field.  
- **`equals()`**: Uses `simple_eval` from the SimpleEval module to evaluate the entire expression entered in the field and displays the result.  

## How the Functions are used:
- Number buttons call the **`a_var(num)`** function.  
- Operation buttons call the **`the_operations(operation)`** function.  
- The clear and backspace buttons call **`clear_all()`** and **`undo()`**.  
- The equals button calls **`equals()`**, which evaluates the expression using SimpleEval.    

## Layout:
The calculator includes:  
- A display screen for entering numbers and expressions.  
- Buttons for numbers (`0–9`) and basic arithmetic operations (`+`, `-`, `*`, `/`, `.`).  
- Special buttons: **Clear**, **Backspace**, and **Equals (`=`)**.  

## Improvements: 
- The project previously used the deprecated **parser** module for evaluating expressions. It has now been updated to use **SimpleEval**, which is safer and actively maintained.

## Requirements  
All dependencies are listed in **`requirements.txt`**. Install them with:  

```bash
pip install -r requirements.txt
