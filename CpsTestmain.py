import time
from tkinter import *
import tkinter as tk
import os.path
import requests
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image


def windowconfig():
    window = tk.Tk()
    window.geometry("500x500")
    window.resizable(0,0)
    window.title("")
    window.mainloop()

def countdown():
    time_left = 60
    while time_left > 0:
        print('倒计时(s):',time_left)
        time.sleep(1)
        time_left = time_left - 1

def runmain():
    windowconfig()

runmain()