import tkinter as tk #importing the tkinter library as tk (standard python library for creating GUIs)

window = tk.Tk() #calling the Tk() constructor in the tk class

def buttonPress():
    print('Button Press')
    label1.config(bg = 'red', text = 'Clicked') #config = modify
    button1.config(text = 'CLICKED!')
    
font1 = 'Helvetica 20 bold italic'
font2 = 'Helvetica 15 bold'

#if some of the parameters are not given (eg: fg, bg, font etc.), default values are assigned automatically
label1 = tk.Label(window, text = 'HELLO TKINTER GUI', fg = 'white', bg = 'green', font = font1) #fg = font color, bg = background color

#3 methods to give the widget location in the window (1.grid  2.pack  3.?)
label1.grid(row = 0, column = 0)

button1 = tk.Button(window, text = 'CLICK ME', font = font2, command = buttonPress) #command = triggering event function
button1.grid(row = 1, column = 0, pady = 10) #pady = padding in y axis direction between 2 widgets
