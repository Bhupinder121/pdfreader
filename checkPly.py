import keyboard
import os
stop = False

def pauseAndPlay():
    global stop
    while True:
        if keyboard.is_pressed('q'):
            return True
        else:
            return False

lines = os.listdir('D:\\pdfreader\\static\\')
print(lines)