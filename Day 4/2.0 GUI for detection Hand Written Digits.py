import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import PIL
import numpy as np
import cv2
from matplotlib import pyplot as plt

win=tk.Tk()

width=300
height=300
font1='Helvetica 12 bold'

def clear():

    canvas1.delete("all")
    global img_draw,img1

    img1 = PIL.Image.new("RGB", (width, height), (255,255,255))
    img_draw = ImageDraw.Draw(img1)
    
def draw(event):

    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    canvas1.create_oval(x1, y1, x2, y2, fill="black",width=10)
    img_draw.ellipse((x1, y1, x2, y2), fill = 'black', outline ='black')

def save():

    global img_draw,img1
    
    filename = "image.png"
    img_array=np.array(img1)
    img_rez=cv2.resize(img_array,(28,28))

    cv2.imwrite('IMG.jpg',img_rez)
    plt.imshow(img_rez,cmap='binary')
    plt.show()

    img1 = PIL.Image.new("RGB", (width, height), (255,255,255))
    img_draw = ImageDraw.Draw(img1)

canvas1=tk.Canvas(win,width=width,height=height,bg='white')

canvas1.grid(row=0,column=0,columnspan=4)
button_save=tk.Button(win,text='SAVE',bg='green',fg='white',font=font1,command=save)
button_save.grid(row=1,column=0,pady=5)

button_predict=tk.Button(win,text='PREDICT',bg='blue',fg='white',font=font1)
button_predict.grid(row=1,column=1,pady=5)

button_clear=tk.Button(win,text='CLEAR',bg='gray10',fg='white',font=font1,command=clear)
button_clear.grid(row=1,column=2,pady=5)

button_exit=tk.Button(win,text='EXIT',bg='red',fg='white',font=font1,command=win.destroy)
button_exit.grid(row=1,column=3,pady=5)

label_predict=tk.Label(win,text='PREDICTED DIGIT : NONE ',bg='white',font=font1)
label_predict.grid(row=2,column=0,columnspan=4)

canvas1.bind("<B1-Motion>",draw)

img1 = PIL.Image.new("RGB", (width, height), (255,255,255))
img_draw = ImageDraw.Draw(img1)
