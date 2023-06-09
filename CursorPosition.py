import pyautogui
import time
import winsound
screenWidth, screenHeight = pyautogui.size()
print("Ctrl-C for Abort")

# beep
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
# win warning
time.sleep(1)
print('\007')
#

try:
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print("X: " + str(currentMouseX) + " | Y: " + str(currentMouseY))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
