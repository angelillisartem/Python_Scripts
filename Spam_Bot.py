import pyautogui as p #Install library "pyautogui" with [pip install pyautogui]
import time

name = input(str("Insert name of contact: "))
text = input(str("Insert the text: "))

def stop():
    time.sleep(1)

def enter():
    p.press("Enter")

p.press("shift", presses=2)
p.write("whatsapp")
enter()
stop()
p.press("command", "f")
p.write(name)
enter()
p.write(text)
enter()