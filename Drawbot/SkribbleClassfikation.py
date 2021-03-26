import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image
import keyboard

def click(New_X, New_Y):
    win32api.SetCursorPos((New_X, New_Y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, New_X, New_Y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, New_X, New_Y, 0, 0)



while True:
    if keyboard.is_pressed("h"):
        x, y = pyautogui.position()

        click(967, 63)
        click(x,y)