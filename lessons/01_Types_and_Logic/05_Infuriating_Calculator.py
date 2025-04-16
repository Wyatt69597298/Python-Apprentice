"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
first = simpledialog.askinteger('Calculator', "First Didgit")
# Ask the user for the second number
second = simpledialog.askinteger('Calculator', "Second Didgit")
# Ask the user for the math operation
defer = simpledialog.askstring('Math Symbol',"Add a math symbol")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if defer == "*":
    messagebox.showinfo("Multiplication", first*second)
elif defer == "/":
    messagebox.showinfo("Division", first/second)
elif defer == "+":
    messagebox.showinfo("Addition", first+second)
elif defer == "-":
    messagebox.showinfo("Subtraction", first-second)
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
