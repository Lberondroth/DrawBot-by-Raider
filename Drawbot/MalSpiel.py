import math
import os
import time
import pyautogui
import win32api
import win32con
from PIL import Image
import numpy


class MalSpiel_BOT():
    def __init__(self):
        super().__init__()
        self.ColorWithCoordsSorted = None
        self.COLORS = []
        self.Positions = []
        self.ColorWithCoords = {}

        self.SameColor = 1
        self.Image_Folder = 'Img'

    def sleep(self, duration, get_now=time.perf_counter):
        if duration == 0: return
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def Change_Color(self, xyT):
        print(xyT)
        x, y = xyT.split(",")
        x = x.strip(" ")
        x = x.strip("(")
        x = int(x)

        y = y.strip(" ")
        y = y.strip(")")
        y = int(y)

        win32api.SetCursorPos((x, y))
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def click(self, New_X, New_Y, delay):

        win32api.SetCursorPos((New_X, New_Y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, New_X, New_Y, 0, 0)
        self.sleep(delay * 100 / 1000000.0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, New_X, New_Y, 0, 0)

    def closest_color(self, rgb):
        r, g, b = rgb
        color_diffs = []
        for color in self.COLORS:
            cr, cg, cb = color.split(",")
            cr = cr.strip('(')
            cg = cg.strip(' ')
            cb = cb.strip(' ')
            cb = cb.strip(')')

            color_diff = math.sqrt(abs(r - int(cr)) ** 2 + abs(g - int(cg)) ** 2 + abs(b - int(cb)) ** 2)
            color_diffs.append((color_diff, color))
        return min(color_diffs)[1]

    def match_color(self, rgb):
        return self.Color_Pos.get(rgb)

    def Bot(self, ChoosenImg, delay, selectedBotName):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.Speicher = self.dir_path + "\Speicher"
        Botpath = self.Speicher + f"\\{selectedBotName}"
        Botfile = open(Botpath, "r")
        n = 0
        for data in Botfile:
            try:
                data.strip("\n")
                OnHoldList = data.split("|")
                Color = OnHoldList[0]
                Position = OnHoldList[1]
                Position = Position.strip("\n")
                self.COLORS.append((str(Color)))
                self.Positions.append(Position)
            except Exception:
                pass
        self.Color_Pos = dict(zip(self.COLORS, self.Positions))
        Botfile.close()

        if not os.path.exists(self.Image_Folder):
            os.mkdir(self.Image_Folder)

        Drawing = Image.open(str(ChoosenImg))
        Drawing = Drawing.convert('RGB')
        width = Drawing.size[0]
        height = Drawing.size[1]

        print(width)
        print(height)
        time.sleep(3)
        self.x1, self.y1 = pyautogui.position()
        print(self.x1, self.y1)

        for y in numpy.arange(0, height):
            print("Linie:", y, "von: ", height)
            for x in numpy.arange(0, width):
                Coords = (x, y)
                rgb = Drawing.getpixel(Coords)
                closest_rgb = self.closest_color(rgb)
                self.ColorWithCoords[str(Coords)] = str(closest_rgb)

        print(len(self.ColorWithCoords), "\t", width * height)
        print(f"Estimated Time: {[int(len(self.ColorWithCoords)) * delay / 10000.0]} ")

        time.sleep(2)
        self.ColorWithCoordsSorted = sorted(self.ColorWithCoords.items(), key=lambda t: t[1])
        for coords, Color in self.ColorWithCoordsSorted:

            coords = str(coords).strip("(", )
            coords = coords.strip(" ")
            coords = coords.strip(")")
            x, y = coords.split(",")

            White = 0
            if Color != self.SameColor:
                self.SameColor = Color
                print("change Color")
                time.sleep(1.5)
                self.Change_Color(self.match_color(str(Color)))
                print(Color, "weiß pls")
                print(Color[:9])

            elif Color[:15] == "(255, 255, 255)":
                White = 1

            if not White:
                New_X = self.x1 + int(x)
                New_Y = self.y1 + int(y)
                try:
                    print(New_Y - height)
                    self.click(New_X, New_Y, delay)
                except Exception:
                    print("error")
                    break
            else:
                pass

        print("done")


if __name__ == "__main__":
    malen = MalSpiel_BOT()
    malen.Bot(
        r"C:\Users\louis\Desktop\DrawBot-by-Raider-main (1)\DrawBot-by-Raider-main\Drawbot\Img\1232.bmp", 1, "Paint")
