import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image

# pos
POS_0 = (646, 522)
POS_1 = (672, 524)
POS_2 = (699, 525)
POS_3 = (645, 552)
POS_4 = (675, 552)
POS_5 = (699, 553)
POS_6 = (700, 587)
POS_7 = (678, 581)
POS_8 = (651, 579)
POS_9 = (651, 610)
POS_10 = (676, 610)
POS_11 = (711, 610)
POS_12 = (706, 631)
POS_13 = (678, 631)
POS_14 = (649, 630)
POS_15 = (651, 665)
POS_16 = (671, 668)
POS_17 = (699, 664)



# color
Color_0 = (0, 0, 0)
Color_1 = (102, 102, 102)
Color_2 = (0, 23, 246)
Color_3 = (255, 255, 255)
Color_4 = (170, 170, 170)
Color_5 = (38, 201, 255)
Color_6 = (150, 65, 18)
Color_7 = (169, 35, 12)
Color_8 = (0, 141, 38)
Color_9 = (0, 255, 77)
Color_10 = (255, 0, 19)
Color_11 = (255, 120, 41)
Color_12 = (147, 104, 103)
Color_13 = (153, 0, 78)
Color_14 = (176, 112, 28)
Color_15 = (255, 201, 38)
Color_16 = (255, 0, 143)
Color_17 = (254, 175, 168)



class GarticBotTest():
    def __init__(self):
        super().__init__()

        self.ColorWithCoords = {}
        self.COLORS = (Color_0, Color_1, Color_2, Color_3, Color_4, Color_5,
                       Color_6, Color_7, Color_8, Color_9, Color_10, Color_12,
                       Color_13, Color_14, Color_15, Color_16, Color_17)

        self.Color_Pos = {
            "(0, 0, 0)": POS_0,
            "(102, 102, 102)": POS_1,
            "(0, 23, 246)": POS_2,
            "(255, 255, 255)": POS_3,
            "(170, 170, 170)": POS_4,
            "(38, 201, 255)": POS_5,
            "(150, 65, 18)": POS_6,
            "(169, 35, 12)": POS_7,
            "(0, 141, 38)": POS_8,
            "(0, 255, 77)": POS_9,
            "(255, 0, 19)": POS_10,
            "(255, 120, 41)": POS_11,
            "(147, 104, 103)": POS_12,
            "(153, 0, 78)": POS_13,
            "(176, 112, 28)": POS_14,
            "(255, 201, 38)": POS_15,
            "(255, 0, 143)": POS_16,
            "(254, 175, 168)": POS_17,
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
        return self.Color_Pos.get(rgb, Color_0)

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
                print("change Color")
                time.sleep(1)
                self.Change_Color(self.match_color(str(Color)))
                time.sleep(1)
            New_X = self.x1 + int(x)
            New_Y = self.y1 + int(y)
            try:
                self.click(New_X, New_Y)
            except Exception:
                print("error")
                break

        print("done")

