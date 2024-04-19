import tkinter as tk
from tkinter import ttk
from app.operations import add, subtract, multiply, divide, percent, square_root

# Dictionary to store the operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": percent,
    "root": square_root
}

# Flag to track if a calculation has been performed
calculation_done = False

def on_enter(event):
    event.widget.config(bg="gray")

def on_leave(event):
    event.widget.config(bg="black")

# Function to update the entry field when a button is clicked
def button_click(value):
    global calculation_done
    
    if calculation_done:
        entry.delete(0, tk.END)
        calculation_done = False
    
    current = entry.get()
    
    # If the maximum number of operations is already reached, perform the calculation first
    if len(current.split()) == 3:
        calculate()
        current = entry.get()
    
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)


# Function to perform calculations when the "=" button is clicked
def calculate():
    global calculation_done

    try:
        expression = entry.get()
        for operator in operations:
            if operator in expression:
                num1, num2 = expression.split(operator)
                result = operations[operator](float(num1), float(num2))
                if result == int(result):
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, int(result))
                else:
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, result)
                calculation_done = True
                break


    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        calculation_done = False

    except ZeroDivisionError as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error: {e}")
        calculation_done = False

def square_root(value):
    global calculation_done

    try:
        result = operations["root"](float(value))
        if result == int(result):
            entry.delete(0, tk.END)
            entry.insert(tk.END, int(result))
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        calculation_done = True
        

    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        calculation_done = False

    except ZeroDivisionError as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error: {e}")
        calculation_done = False

# Function to clear the entry field when the "CE" button is clicked
def clear():
    global calculation_done
    
    entry.delete(0, tk.END)
    calculation_done = False

root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")
root.resizable(False, False)
root.configure(bg="#222222")

entry = tk.Entry(
    root, 
    width=30,
    font=("Courier", 11, "bold"), 
    bg="green",
    fg="black",
    borderwidth=1,
    relief="flat"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button size and padding
button_width = 5
button_height = 2
button_padx = 5
button_pady = 5


# Button organization: numbers, operators, special functions
buttons = [
    # Row 1
    ("CE", 1, 0, clear),
    ("√", 1, 1, lambda: square_root(entry.get())),
    ("%", 1, 2, lambda: button_click(" % ")),
    ("÷", 1, 3, lambda: button_click(" / ")),

    # Row 2
    ("7", 2, 0, lambda: button_click("7")),
    ("8", 2, 1, lambda: button_click("8")),
    ("9", 2, 2, lambda: button_click("9")),
    ("×", 2, 3, lambda: button_click(" * ")),

    # Row 3
    ("4", 3, 0, lambda: button_click("4")),
    ("5", 3, 1, lambda: button_click("5")),
    ("6", 3, 2, lambda: button_click("6")),
    ("-", 3, 3, lambda: button_click(" - ")),

    # Row 4
    ("1", 4, 0, lambda: button_click("1")),
    ("2", 4, 1, lambda: button_click("2")),
    ("3", 4, 2, lambda: button_click("3")),
    ("+", 4, 3, lambda: button_click(" + ")),

    # Row 5
    ("0", 5, 0, lambda: button_click("0")),
    (".", 5, 1, lambda: button_click(".")),
    ("=", 5, 2, calculate),
]


# Create and place buttons
for text, row, col, command in buttons:
    button = tk.Button(
        root, 
        text=text, 
        width=button_width, 
        height=button_height, 
        command=command,
        relief="flat",
        bg="#000000", 
        fg="white", 
        font=("Courier", 10, "bold"), 
        borderwidth=5
    )
    button.grid(row=row, column=col, padx=button_padx, pady=button_pady)
    button.bind('<Enter>', on_enter)
    button.bind('<Leave>', on_leave)


root.mainloop()
