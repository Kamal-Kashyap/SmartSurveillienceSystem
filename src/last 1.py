import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
global root 
root = Tk()
canvas = Canvas(root,width = 850,height = 470, bg = 'black')
canvas.grid(column = 0 , row = 1)
img = PhotoImage(file="lastt.png")
canvas.create_image(50,10,image=img,anchor=NW)
