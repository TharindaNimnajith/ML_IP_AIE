import tkinter as tk
window=tk.Tk()

def btnprs():

    label1.config(bg='red',text='ClICKED')
    button1.config(text='clicked')
    
font1='Helvetica 20 bold italic'
font2='Helvetica 15 bold'
label1=tk.Label(window,text='HELLO TKINTER GUI',fg='white',bg='green',font=font1)
label1.grid(row=0,column=0)

button1=tk.Button(window,text='CLICK ME ',font=font2,command=btnprs)
button1.grid(row=1,column=0,pady=10)

