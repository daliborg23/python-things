import pyautogui
import time
# 1. cmd: cd C:\Kurs\Python     py SkypeConnect
# 2. prekliknout na anonymni zalozku firefoxu
# 3. cekat

# TODO: - nejaky loop na kontrolu casu (asi dalsi script?) a kdyz bude 7:55 tak se pripoji, a pak kolem 11:20 treba, probehne druhe opacko
#       - start / stop na klavesu?

# start a prekliknuti na firefox
n = 5
for s in reversed(range(n + 1)):
    print(s)
    time.sleep(1)
print("SkypeConnect Start")
link = "https://join.skype.com/GtZFtMijYJ4z"
# link = "https://www.w3schools.com/python/python_for_loops.asp" # TEST
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

# nova zalozka a napsani odkazu
pyautogui.keyDown('ctrl')
pyautogui.press('t')
pyautogui.keyUp('ctrl')
for ch in link:
    pyautogui.press(ch)
pyautogui.press('enter')
time.sleep(7)

# Blokovat mikrofon
pyautogui.moveTo(1117, 247)
pyautogui.click()
time.sleep(3)

# Pripojit se
pyautogui.moveTo(960, 555)
pyautogui.click()
time.sleep(8)

# Blokovat mikrofon II.
pyautogui.moveTo(666, 208)
pyautogui.click()
time.sleep(2)

# Pripojit se II.
pyautogui.moveTo(1000, 744)
pyautogui.click()
time.sleep(2)

# Kliknout do kolonky jmena
pyautogui.moveTo(960, 725)
pyautogui.click()
time.sleep(2)

# Napis jmeno
name = "Dalibor Glajcar"
for ch in name:
    pyautogui.press(ch)
pyautogui.press('enter')
time.sleep(2)

# Pripojit k hovoru
pyautogui.moveTo(1111, 888)
pyautogui.click()
time.sleep(5)

# Otevre chat
pyautogui.moveTo(1675, 968)
pyautogui.click()
time.sleep(2)

# Napis do chatu "ahoj"
hello = "Ahoj"
for ch in hello:
    pyautogui.press(ch)
pyautogui.press('enter')

print("SkypeConnect End")
print('\007')
# konec

# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.click()  # Click the mouse at its current location.
# pyautogui.click(200, 220)  # Click the mouse at the x, y coordinates 200, 220.
# # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.move(None, 10)
# pyautogui.doubleClick()  # Double click the mouse at the
# # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# # Type with quarter-second pause in between each key.
# pyautogui.write('Hello world!', interval=0.25)
# pyautogui.press('esc')  # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
