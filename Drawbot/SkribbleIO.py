import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image

# pos
POS_0 = (603, 863)
POS_1 = (606, 886)
POS_2 = (630, 888)
POS_3 = (629, 864)
POS_4 = (651, 861)
POS_5 = (655, 889)
POS_6 = (677, 890)
POS_7 = (676, 860)
POS_8 = (696, 863)
POS_9 = (701, 885)
POS_10 = (726, 886)
POS_11 = (725, 862)
POS_12 = (752, 863)
POS_13 = (750, 887)
POS_14 = (780, 888)
POS_15 = (778, 856)
POS_16 = (792, 857)
POS_17 = (795, 894)
POS_18 = (816, 887)
POS_19 = (822, 860)
POS_20 = (847, 865)
POS_21 = (846, 890)


# color
Color_0 = (255, 255, 255)
Color_1 = (0, 0, 0)
Color_2 = (76, 76, 76)
Color_3 = (193, 193, 193)
Color_4 = (239, 19, 11)
Color_5 = (116, 11, 7)
Color_6 = (194, 56, 0)
Color_7 = (255, 113, 0)
Color_8 = (255, 228, 0)
Color_9 = (232, 162, 0)
Color_10 = (0, 85, 16)
Color_11 = (0, 204, 0)
Color_12 = (0, 178, 255)
Color_13 = (0, 86, 158)
Color_14 = (14, 8, 101)
Color_15 = (35, 31, 211)
Color_16 = (163, 0, 186)
Color_17 = (85, 0, 105)
Color_18 = (167, 85, 116)
Color_19 = (211, 124, 170)
Color_20 = (160, 82, 45)
Color_21 = (99, 48, 13)



class Skribble_BOT():
    def __init__(self):
        super().__init__()

        self.ColorWithCoords = {}
        self.COLORS = (Color_0, Color_1, Color_2, Color_3, Color_4, Color_5,
                       Color_6, Color_7, Color_8, Color_9, Color_10, Color_12,
                       Color_13, Color_14, Color_15, Color_16, Color_17,
                       Color_18, Color_19, Color_20, Color_21)

        self.Color_Pos = {"(255, 255, 255)": POS_0,
                          "(0, 0, 0)": POS_1,
                          "(76, 76, 76)": POS_2,
                          "(193, 193, 193)": POS_3,
                          "(239, 19, 11)": POS_4,
                          "(116, 11, 7)": POS_5,
                          "(194, 56, 0)": POS_6,
                          "(255, 113, 0)": POS_7,
                          "(255, 228, 0)": POS_8,
                          "(232, 162, 0)": POS_9,
                          "(0, 85, 16)": POS_10,
                          "(0, 204, 0)": POS_11,
                          "(0, 178, 255)": POS_12,
                          "(0, 86, 158)": POS_13,
                          "(14, 8, 101)": POS_14,
                          "(35, 31, 211)": POS_15,
                          "(163, 0, 186)": POS_16,
                          "(85, 0, 105)": POS_17,
                          "(167, 85, 116)": POS_18,
                          "(211, 124, 170)": POS_19,
                          "(160, 82, 45)": POS_20,
                          "(99, 48, 13)": POS_21,
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
                time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000001)
                self.click(New_X, New_Y)
            except Exception:
                print("error")
                break

        print("done")

