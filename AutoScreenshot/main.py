import pyautogui
import keyboard

num = 1


while True:
    if keyboard.is_pressed('print screen'):
        pyautogui.screenshot("Photo" + str(num) + ".png")
        num += 1
