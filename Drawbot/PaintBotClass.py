import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image

# pos
POS_0 = (881, 62)
POS_1 = (906, 62)
POS_2 = (926, 63)
POS_3 = (945, 63)
POS_4 = (967, 63)
POS_5 = (994, 63)
POS_6 = (1018, 62)
POS_7 = (1041, 64)
POS_8 = (1057, 61)
POS_9 = (1079, 63)
POS_10 = (881, 86)
POS_11 = (902, 86)
POS_12 = (931, 84)
POS_13 = (947, 85)
POS_14 = (969, 88)
POS_15 = (994, 83)
POS_16 = (1013, 85)
POS_17 = (1038, 85)
POS_18 = (1058, 87)
POS_19 = (1082, 87)

# color
Color_0 = (0, 0, 0)
Color_1 = (127, 127, 127)
Color_2 = (136, 0, 21)
Color_3 = (237, 28, 36)
Color_4 = (255, 127, 39)
Color_5 = (255, 242, 0)
Color_6 = (34, 177, 76)
Color_7 = (0, 162, 232)
Color_8 = (63, 72, 204)
Color_9 = (163, 73, 164)
Color_10 = (255, 255, 255)
Color_11 = (195, 195, 195)
Color_12 = (185, 122, 87)
Color_13 = (255, 174, 201)
Color_14 = (255, 201, 14)
Color_15 = (239, 228, 176)
Color_16 = (181, 230, 29)
Color_17 = (153, 217, 234)
Color_18 = (112, 146, 190)
Color_19 = (200, 191, 231)


class Paint_BOT():
    def __init__(self):
        super().__init__()

        self.ColorWithCoords = {}
        self.COLORS = (Color_0, Color_1, Color_2, Color_3, Color_4, Color_5,
                       Color_6, Color_7, Color_8, Color_9, Color_10, Color_12,
                       Color_13, Color_14, Color_15, Color_16, Color_17,
                       Color_18, Color_19)

        self.Color_Pos = {"(0, 0, 0)": POS_0,
                          "(127, 127, 127)": POS_1,
                          "(136, 0, 21)": POS_2,
                          "(237, 28, 36)": POS_3,
                          "(255, 127, 39)": POS_4,
                          "(255, 242, 0)": POS_5,
                          "(34, 177, 76)": POS_6,
                          "(0, 162, 232)": POS_7,
                          "(63, 72, 204)": POS_8,
                          "(163, 73, 164)": POS_9,
                          "(255, 255, 255)": POS_10,
                          "(195, 195, 195)": POS_11,
                          "(185, 122, 87)": POS_12,
                          "(255, 174, 201)": POS_13,
                          "(255, 201, 14)": POS_14,
                          "(239, 228, 176)": POS_15,
                          "(181, 230, 29)": POS_16,
                          "(153, 217, 234)": POS_17,
                          "(112, 146, 190)": POS_18,
                          "(200, 191, 231)": POS_19}

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
        return self.Color_Pos.get(rgb, Color_10)

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
