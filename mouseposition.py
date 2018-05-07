# -*- coding:utf-8 -*-
import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

#  current screen resolution（w, h）
print(pyautogui.size())
pyautogui.alert('dialog with text + OK button')
#  current position of the mouse
for i in range(10):
    time.sleep(1)
    print (pyautogui.position())

#locateCenterOnScreen() return picture center x y values on the screen
#pyautogui.locateCenterOnScreen('pyautogui/looks.png')


