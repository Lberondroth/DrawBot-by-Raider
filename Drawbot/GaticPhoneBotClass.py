import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image
from numba import cuda, jit

# pos
black_pos = (432, 282)
grey_pos = (481, 386)
dark_blue_pos = (533, 388)

white_pos = (437, 435)
light_grey_pos = (486, 438)
light_blue_pos = (528, 443)

dark_green_pos = (428, 484)
dark_brown_pos = (483, 483)
brown_pos = (532, 488)

green_pos = (438, 544)
red_pos = (486, 542)
orange_pos = (534, 543)

golden_pos = (432, 581)
purple_pos = (484, 594)
skin_color_pos = (527, 592)

yellow_pos = (433, 641)
pink_pos = (490, 634)
another_skin_pos = (533, 641)

# color rgb
black = (0, 0, 0)
grey = (102, 102, 102)
dark_blue = (0, 80, 205)

white = (255, 255, 255)
light_grey = (170, 170, 170)
light_blue = (38, 201, 255)

dark_green = (1, 116, 32)
dark_brown = (105, 21, 6)
brown = (150, 65, 18)

green = (17, 176, 60)
red = (255, 0, 19)
orange = (255, 120, 41)

golden = (176, 112, 28)
purple = (153, 0, 78)
skin_color = (203, 90, 87)

yellow = (255, 193, 38)
pink = (255, 0, 143)
another_skin = (254, 175, 168)


class Gartic_Phone_BOT():
    def __init__(self):
        super().__init__()
        self.zeit = 1/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.ColorWithCoords = {}
        self.COLORS = (  # white
            black, grey, dark_blue,
            white, light_grey, light_blue,
            dark_green, dark_brown, brown,
            green, red, orange,
            golden, purple, skin_color,
            yellow, pink, another_skin)

        self.Color_Pos = {"(0, 0, 0)": black_pos,
                          "(102, 102, 102)": grey_pos,
                          "(0, 80, 205)": dark_blue_pos,

                          "(255, 255, 255)": white_pos,
                          "(170, 170, 170)": light_grey_pos,
                          "(38, 201, 255)": light_blue_pos,

                          "(1, 116, 32)": dark_green_pos,
                          "(105, 21, 6)": dark_brown_pos,
                          "(150, 65, 18)": brown_pos,

                          "(17, 176, 60)": green_pos,
                          "(255, 0, 19)": red_pos,
                          "(255, 120, 41)": orange_pos,

                          "(176, 112, 28)": golden_pos,
                          "(153, 0, 78)": purple_pos,
                          "(203, 90, 87)": skin_color_pos,

                          "(255, 193, 38)": yellow_pos,
                          "(255, 0, 143)": pink_pos,
                          "(254, 175, 168)": another_skin_pos,
                          }

        self.SameColor = 1
        self.Image_Folder = 'Img'

    def Change_Color(self, xyT):
        x, y = xyT
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def click(self, New_X, New_Y):
        win32api.SetCursorPos((New_X, New_Y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, New_X, New_Y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, New_X, New_Y, 0, 0)

    def closest_color(self, rgb) -> object:
        r, g, b = rgb
        color_diffs = []
        for color in self.COLORS:
            cr, cg, cb = color
            color_diff = math.sqrt(abs(r - cr) ** 2 + abs(g - cg) ** 2 + abs(b - cb) ** 2)
            color_diffs.append((color_diff, color))
        return min(color_diffs)[1]

    def match_color(self, rgb):
        return self.Color_Pos.get(rgb, white_pos)

    def Bot(self, ChoosenImg):
        if not os.path.exists(self.Image_Folder):
            os.mkdir(self.Image_Folder)

        Drawing = Image.open(str(ChoosenImg))
        Drawing.show()
        Drawing = Drawing.convert('RGB')
        width = Drawing.size[0]
        height = Drawing.size[1]

        print(width)
        print(height)
        time.sleep(3)
        self.x1, self.y1 = pyautogui.position()
        print(self.x1, self.y1)

        for y in range(0, height):
            print("Linie:", y, "von: ", height)
            for x in range(0, width):
                Coords = (x, y)
                rgb = Drawing.getpixel(Coords)
                closest_rgb = self.closest_color(rgb)
                self.ColorWithCoords[str(Coords)] = str(closest_rgb)

        print(len(self.ColorWithCoords), "\t", width * height)
        time.sleep(2)
        self.ColorWithCoordsSorted = sorted(self.ColorWithCoords.items(), key=lambda t: t[1])
        for coords, Color in self.ColorWithCoordsSorted:
            coords = coords.strip("(", )
            coords = coords.strip(" ")
            coords = coords.strip(")")
            x, y = coords.split(",")

            if Color != self.SameColor:
                self.SameColor = Color
                print("Change Color")
                time.sleep(0.1)
                self.Change_Color(self.match_color(str(Color)))
            New_X = self.x1 + int(x)
            New_Y = self.y1 + int(y)
            try:
                self.click(New_X, New_Y)
            except Exception:
                print("error")
                break

        print("done")
