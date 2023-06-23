import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

# 0. screen resolution 1920x1080
# 1. spustit a prekliknout na anonymni zalozku firefoxu

# todo
# ziskani odkazu
#


def getLink():
    prezence = "https://docs.google.com/spreadsheets/d/1v4eGzIoUpESoeCLom1oC6mm_veFffLuJMey5FnY8hs0/edit"

    # nova zalozka a napsani odkazu
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')
    for ch in prezence:
        pyautogui.press(ch)
    pyautogui.press('enter')
    time.sleep(7)

    # najeti na konkretni radek? risk, ze se neco zmeni
    for i in range(66):
        pyautogui.press('down')
        time.sleep(0.5)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    time.sleep(0.5)
    pyautogui.press('c')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')


def connect():
    # start a prekliknuti na firefox
    n = 5
    for s in reversed(range(n + 1)):
        print(s)
        time.sleep(1)
    print("---Connect-Start---")
    link = "https://join.skype.com/C9BVh7RdV2RK"
    # link = "https://www.w3schools.com/python/python_for_loops.asp" # TEST

    # nova zalozka a napsani odkazu
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    # for ch in link:
    #     pyautogui.press(ch)
    # pyautogui.press('enter')
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

    # delay
    print("sledovani zacina... odpocet 13200s")
    time.sleep(13200)

    # zavreni zalozky a konec funkce, vraceni do loopu a cekani na cas2
    print("---End---")
    print('\007')
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    # konec


# def connectTest():
#     # start a prekliknuti na firefox
#     n = 5
#     for s in reversed(range(n + 1)):
#         print(s)
#         time.sleep(1)
#     print("---Start---")
#     link = "https://www.w3schools.com/python/python_for_loops.asp"  # TEST
#     screenWidth, screenHeight = pyautogui.size()
#     currentMouseX, currentMouseY = pyautogui.position()

#     # nova zalozka a napsani odkazu
#     pyautogui.keyDown('ctrl')
#     pyautogui.press('t')
#     pyautogui.keyUp('ctrl')
#     for ch in link:
#         pyautogui.press(ch)
#     pyautogui.press('enter')
#     time.sleep(7)

#     print("sledovani zacina... odpocet 12600s")
#     time.sleep(12600)
#     print("---End---")
#     print('\007')
#     # konec

# TESTING
# # cas pripojeni Test
# cas1 = "17:32"
# cas2 = "17:33"

# while True:
#     watch = time.localtime()
#     current_time = time.strftime("%H:%M", time.localtime())
#     print(str(watch.tm_hour) + ":" + str(watch.tm_min) + ":" + str(watch.tm_sec))
#     if current_time == cas1:
#         print('\007')
#         print("Connecting in 3")
#         time.sleep(1)
#         print('\007')
#         print("Connecting in 2")
#         time.sleep(1)
#         print('\007')
#         print("Connecting in 1")
#         time.sleep(1)
#         connectTest()
#     if current_time == cas2:
#         print('\007')
#         print("Connecting in 3")
#         time.sleep(1)
#         print('\007')
#         print("Connecting in 2")
#         time.sleep(1)
#         print('\007')
#         print("Connecting in 1")
#         time.sleep(1)
#         connectTest()
#     # time.sleep(10)
#     time.sleep(1)


# cas pripojeni
cas1 = "08:05"
cas2 = "11:50"


# loop na cas
while True:
    watch = time.localtime()
    current_time = time.strftime("%H:%M", time.localtime())
    print(str(watch.tm_hour) + ":" + str(watch.tm_min) + ":" + str(watch.tm_sec))
    if current_time == cas1:
        print('\007')
        time.sleep(1)
        print('\007')
        time.sleep(1)
        print('\007')
        time.sleep(1)
        connect()
    if current_time == cas2:
        print('\007')
        time.sleep(1)
        print('\007')
        time.sleep(1)
        print('\007')
        time.sleep(1)
        connect()
    time.sleep(10)

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
