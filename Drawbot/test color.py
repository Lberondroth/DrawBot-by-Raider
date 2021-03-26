import time
import keyboard
import pyautogui

number = 0
number2 = 0
number3 = 0
number4 = 0
Postiton = []
Colors = []
while True:
    if keyboard.is_pressed("b"):
        START = time.time()
        SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
        MOUSE_X, MOUSE_Y = pyautogui.position()
        PIXEL = pyautogui.screenshot(
            region=(
                MOUSE_X, MOUSE_Y, 1, 1
            )
        )
        COLOR = PIXEL.getcolors()
        END = time.time()

        Postiton.append((MOUSE_X, MOUSE_Y))
        Colors.append((COLOR[0][1].__str__()))

        print(number)
        number = number + 1
        print("Mouse: (%d,%d)" % (MOUSE_X, MOUSE_Y))
        print("RGB: %s" % (COLOR[0][1].__str__()))

        print(".....................................")

        time.sleep(0.5)

    if keyboard.is_pressed("p"):
        for X in Postiton:
            keyboard.write(f"POS_{number2} = {X} \n")
            number2 = number2 + 1
        number2 = 0
        time.sleep(1)

    if keyboard.is_pressed("c"):
        for X in Colors:
            keyboard.write(f"Color_{number3} = {X} \n")
            number3 = number3 + 1
        number3 = 0
        time.sleep(1)

    if keyboard.is_pressed("d"):
        for X in Colors:
            keyboard.write(f'"{X}": POS_{number4},\n')
            number4 = number4 + 1
        number4 = 0
        time.sleep(1)

