from PyQt5 import QtCore, QtGui, QtWidgets
import time
import keyboard
import os
from bs4 import BeautifulSoup
import requests
import GaticPhoneBotClass
import Gartic
import PaintBotClass
import SkribbleIO


class Ui_DrawBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.Image_Folder = "Img"
        self.Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

        self.u_agnt = {
            # User Agent eintragen (Google: My User agent) Text Copy paste
            'User-Agent': ' ',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive', }

        self.Current_Image_X = 1
        self.Current_Image_Y = 1

    def setupUi(self, DrawBot_window):
        DrawBot_window.resize(1131, 631)

        self.DrawBot_Background = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Background.setGeometry(QtCore.QRect(0, 0, 1131, 631))

        self.DrawBot_Background.setTextFormat(QtCore.Qt.AutoText)
        self.DrawBot_Background.setPixmap(QtGui.QPixmap("Bilder/Cover_2.0.jpg"))
        self.DrawBot_Background.setScaledContents(True)

        self.DrawBot_OutputFrame = QtWidgets.QLineEdit(DrawBot_window)
        self.DrawBot_OutputFrame.setGeometry(QtCore.QRect(380, 560, 361, 61))
        self.DrawBot_OutputFrame.setStyleSheet("font: 57 11pt \"MagdaClean\";\n"
                                               "color: darkred;\n"
                                               "background-color: Black;\n"
                                               "border-style: Outset;\n"
                                               "border-color: Darkred;\n"
                                               "border-width:2px;\n"
                                               "border-radius: 4px")
        self.DrawBot_OutputFrame.setReadOnly(True)
        self.DrawBot_OutputFrame.setAlignment(QtCore.Qt.AlignVCenter)
        self.DrawBot_OutputFrame.setAlignment(QtCore.Qt.AlignHCenter)

        self.DrawBot_CommandButton = QtWidgets.QPushButton(DrawBot_window)
        self.DrawBot_CommandButton.setGeometry(QtCore.QRect(380, 530, 210, 25))
        self.DrawBot_CommandButton.setStyleSheet("background-color:black;\n"
                                                 "color:darkred;\n"
                                                 "border-style: outset;\n"
                                                 "border-width:2px;\n"
                                                 "border-radius: 4px;\n"
                                                 "font: 57 13pt \"MagdaClean\";")

        self.DrawBot_Converted = QtWidgets.QCheckBox(DrawBot_window)
        self.DrawBot_Converted.setGeometry(QtCore.QRect(610, 530, 131, 25))
        self.DrawBot_Converted.setStyleSheet("background-color:black;\n"
                                             "color:darkred;\n"
                                             "border-style: outset;\n"
                                             "border-width:2px;\n"
                                             "border-radius: 4px;\n"
                                             "font: 57 13pt \"MagdaClean\";")

        self.DrawBot_LineMaxLCD = QtWidgets.QLCDNumber(DrawBot_window)
        self.DrawBot_LineMaxLCD.setGeometry(QtCore.QRect(0, 570, 131, 41))
        self.DrawBot_LineMaxLCD.setStyleSheet("font: 57 13pt \"MagdaClean\";\n"
                                              "color: darkred;\n"
                                              "background-color: Black;\n"
                                              "border-style: Outset;\n"
                                              "border-color: Darkred;\n"
                                              "border-width:2px;\n"
                                              "border-radius: 4px;\n")
        self.DrawBot_LineMaxLCD.setMode(QtWidgets.QLCDNumber.Dec)
        self.DrawBot_LineMaxLCD.setProperty("intValue", 0)

        self.DrawBot_Linecall = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Linecall.setGeometry(QtCore.QRect(10, 545, 151, 21))
        self.DrawBot_Linecall.setStyleSheet("background-color:black;\n"
                                            "color:darkred;\n"
                                            "font: 57 13pt \"MagdaClean\";")

        self.DrawBot_CurrentGame = QtWidgets.QComboBox(DrawBot_window)
        self.DrawBot_CurrentGame.setGeometry(QtCore.QRect(890, 550, 211, 22))
        self.DrawBot_CurrentGame.setStyleSheet("font: 57 13pt \\\"MagdaClean\\\";\n"
                                               "color: darkred;\n"
                                               "background-color: black;\n"
                                               "border-style: outset;\n"
                                               "border-width:2px;\n"
                                               "border-radius: 4px;\n"
                                               "border-color: darkred;")

        self.DrawBot_CurrentGame.addItem("Gartic Phone")
        self.DrawBot_CurrentGame.addItem("Skribble Io")
        self.DrawBot_CurrentGame.addItem("Paint Windows")
        self.DrawBot_CurrentGame.addItem("Gartic IO")
        self.DrawBot_CurrentGame.addItem("Skribble Io")
        self.DrawBot_CurrentGame.addItem("Gartic Bot Test")
        self.DrawBot_CurrentGame.setCurrentIndex(0)

        self.DrawBot_Preview1 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview1.setGeometry(QtCore.QRect(20, 40, 351, 191))
        self.DrawBot_Preview1.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview1.setScaledContents(True)

        self.DrawBot_Preview2 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview2.setGeometry(QtCore.QRect(390, 40, 351, 191))
        self.DrawBot_Preview2.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview2.setScaledContents(True)

        self.DrawBot_Preview3 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview3.setGeometry(QtCore.QRect(760, 40, 351, 191))
        self.DrawBot_Preview3.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview3.setScaledContents(True)

        self.DrawBot_Preview4 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview4.setGeometry(QtCore.QRect(20, 260, 351, 191))
        self.DrawBot_Preview4.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview4.setScaledContents(True)

        self.DrawBot_Preview5 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview5.setGeometry(QtCore.QRect(390, 260, 351, 191))
        self.DrawBot_Preview5.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview5.setScaledContents(True)

        self.DrawBot_Preview6 = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Preview6.setGeometry(QtCore.QRect(760, 260, 351, 191))
        self.DrawBot_Preview6.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.DrawBot_Preview6.setScaledContents(True)

        self.DrawBot_Name = QtWidgets.QLabel(DrawBot_window)
        self.DrawBot_Name.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.DrawBot_Name.setStyleSheet("color:darkred;\n"
                                        "font: 57 13pt \"MagdaClean\";")

        self.DrawBot_DrawButton = QtWidgets.QPushButton(DrawBot_window)
        self.DrawBot_DrawButton.setGeometry(QtCore.QRect(884, 582, 221, 41))
        self.DrawBot_DrawButton.setStyleSheet("background-color:black;\n"
                                              "color:darkred;\n"
                                              "border-style: outset;\n"
                                              "border-width:2px;\n"
                                              "border-radius: 4px;\n"
                                              "font: 57 13pt \"MagdaClean\";")
        self.DrawBot_DrawButton.clicked.connect(self.DrawBot)

        self.DrawBot_LineMinLCD = QtWidgets.QLCDNumber(DrawBot_window)
        self.DrawBot_LineMinLCD.setGeometry(QtCore.QRect(-10, 570, 91, 41))
        self.DrawBot_LineMinLCD.setStyleSheet(("font: 57 13pt \"MagdaClean\";\n"
                                               "color: darkred;\n"
                                               "background-color: Black;\n"
                                               "border-style: Outset;\n"
                                               "border-color: Darkred;\n"
                                               "border-width:2px;\n"
                                               "border-radius: 4px;\n"))

        self.retranslateUi(DrawBot_window)
        QtCore.QMetaObject.connectSlotsByName(DrawBot_window)

    def DrawBot(self):
        for file in os.listdir('Img'):
            location = "Img"
            new_file = os.path.join(location, file)
            os.remove(new_file)
        print(os.listdir)
        self.Download_Image()
        print(self.ok)
        if self.ok:
            self.DrawBot_selectTimer = QtCore.QTimer()
            self.DrawBot_selectTimer.timeout.connect(self.Select_Image)
            self.DrawBot_OutputFrame.setText("Drücke Y um deine Auswahl zu bestätigen")
            if not self.DrawBot_selectTimer.isActive():
                self.DrawBot_selectTimer.start(50)
            else:
                pass
        else:
            print("rip")

    def Download_Image(self):
        data, self.ok = QtWidgets.QInputDialog.getText(self, "Data 6", "Enter Keyword:")
        if self.ok:
            self.DrawBot_LineMinLCD.display(6)
            Number_of_Images = 6

            search_url = self.Google_Image + 'q=' + data

            response = requests.get(search_url, headers=self.u_agnt)
            html = response.text

            b_soup = BeautifulSoup(html, 'html.parser')
            results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
            Current_Image = 0
            imagelinks = []

            for result in results:
                try:
                    link = result['data-src']
                    imagelinks.append(link)
                    Current_Image = Current_Image + 1
                    if Current_Image >= Number_of_Images:
                        break
                except KeyError:
                    continue
            self.DrawBot_LineMaxLCD.display(len(imagelinks))
            self.downloaded_images_Pixmap = []
            for download, imagelink in enumerate(imagelinks):
                response = requests.get(imagelink)
                self.imagename = self.Image_Folder + '/' + data + str(download + 1) + '.bmp'
                with open(self.imagename, 'wb') as file:
                    file.write(response.content)
                self.downloaded_images_Pixmap.append(self.imagename)
        else:
            self.DrawBot_OutputFrame.setText(f"Error kein Bild gefunden mit dem Namen:  {data}")

    def Select_Image(self):
        self.DrawBot_Preview1.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[0]))
        self.DrawBot_Preview2.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[1]))
        self.DrawBot_Preview3.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[2]))
        self.DrawBot_Preview4.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[3]))
        self.DrawBot_Preview5.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[4]))
        self.DrawBot_Preview6.setPixmap(QtGui.QPixmap(self.downloaded_images_Pixmap[5]))

        if keyboard.is_pressed("d"):
            self.Current_Image_X = self.Current_Image_X + 1
            time.sleep(0.2)
        elif keyboard.is_pressed("a"):
            self.Current_Image_X = self.Current_Image_X - 1
            time.sleep(0.2)
        elif keyboard.is_pressed("w"):
            self.Current_Image_Y = self.Current_Image_Y + 1
            time.sleep(0.2)
        elif keyboard.is_pressed("s"):
            self.Current_Image_Y = self.Current_Image_Y - 1
            time.sleep(0.2)

        if self.Current_Image_X > 3:
            self.Current_Image_X = 1
        elif self.Current_Image_X < 1:
            self.Current_Image_X = 3

        if self.Current_Image_Y > 2:
            self.Current_Image_Y = 1
        elif self.Current_Image_Y < 1:
            self.Current_Image_Y = 2

        if self.Current_Image_X == 1 and self.Current_Image_Y == 1:
            self.DrawBot_Preview1.setFrameShape(QtWidgets.QFrame.Box)
            self.DrawBot_Preview1.setMidLineWidth(3)
            self.DrawBot_Preview1.setStyleSheet("border: 2px solid red;")

            self.DrawBot_Preview2.setStyleSheet("")
            self.DrawBot_Preview3.setStyleSheet("")
            self.DrawBot_Preview4.setStyleSheet("")
            self.DrawBot_Preview5.setStyleSheet("")
            self.DrawBot_Preview6.setStyleSheet("")
            if keyboard.is_pressed("y"):
                # self.ChoosenImg = self.downloaded_images_Pixmap[0]
                print("1")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

        elif self.Current_Image_X == 2 and self.Current_Image_Y == 1:
            self.DrawBot_Preview2.setStyleSheet("border: 2px solid red;")
            self.DrawBot_Preview2.setLineWidth(3)

            self.DrawBot_Preview1.setStyleSheet("")
            self.DrawBot_Preview3.setStyleSheet("")
            self.DrawBot_Preview4.setStyleSheet("")
            self.DrawBot_Preview5.setStyleSheet("")
            self.DrawBot_Preview6.setStyleSheet("")
            if keyboard.is_pressed("y"):
                self.ChoosenImg = self.downloaded_images_Pixmap[1]
                print("2")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

        elif self.Current_Image_X == 3 and self.Current_Image_Y == 1:
            self.DrawBot_Preview3.setStyleSheet("border: 2px solid red;")
            self.DrawBot_Preview3.setLineWidth(3)

            self.DrawBot_Preview1.setStyleSheet("")
            self.DrawBot_Preview2.setStyleSheet("")
            self.DrawBot_Preview4.setStyleSheet("")
            self.DrawBot_Preview5.setStyleSheet("")
            self.DrawBot_Preview6.setStyleSheet("")
            if keyboard.is_pressed("y"):
                self.ChoosenImg = self.downloaded_images_Pixmap[2]
                print("3")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

        if self.Current_Image_X == 1 and self.Current_Image_Y == 2:
            self.DrawBot_Preview4.setStyleSheet("border: 2px solid red;")
            self.DrawBot_Preview4.setLineWidth(3)

            self.DrawBot_Preview1.setStyleSheet("")
            self.DrawBot_Preview2.setStyleSheet("")
            self.DrawBot_Preview3.setStyleSheet("")
            self.DrawBot_Preview5.setStyleSheet("")
            self.DrawBot_Preview6.setStyleSheet("")
            if keyboard.is_pressed("y"):
                self.ChoosenImg = self.downloaded_images_Pixmap[3]
                print("4")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

        elif self.Current_Image_X == 2 and self.Current_Image_Y == 2:
            self.DrawBot_Preview5.setStyleSheet("border: 2px solid red;")
            self.DrawBot_Preview5.setLineWidth(3)

            self.DrawBot_Preview1.setStyleSheet("")
            self.DrawBot_Preview2.setStyleSheet("")
            self.DrawBot_Preview3.setStyleSheet("")
            self.DrawBot_Preview4.setStyleSheet("")
            self.DrawBot_Preview6.setStyleSheet("")
            if keyboard.is_pressed("y"):
                self.ChoosenImg = self.downloaded_images_Pixmap[4]
                print("5")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

        elif self.Current_Image_X == 3 and self.Current_Image_Y == 2:
            self.DrawBot_Preview6.setStyleSheet("border: 2px solid red;")
            self.DrawBot_Preview6.setLineWidth(3)
            self.DrawBot_Preview1.setStyleSheet("")
            self.DrawBot_Preview2.setStyleSheet("")
            self.DrawBot_Preview3.setStyleSheet("")
            self.DrawBot_Preview4.setStyleSheet("")
            self.DrawBot_Preview5.setStyleSheet("")
            if keyboard.is_pressed("y"):
                self.ChoosenImg = self.downloaded_images_Pixmap[5]
                print("6")
                self.DrawBot_selectTimer.stop()
                self.BotModus()

    def BotModus(self):
        if self.DrawBot_CurrentGame.currentIndex() == 0:
            self.GarticPhoneBot()

        elif self.DrawBot_CurrentGame.currentIndex() == 1:
            self.SkribbleIoBot()

        elif self.DrawBot_CurrentGame.currentIndex() == 2:
            self.PaintBot()

        elif self.DrawBot_CurrentGame.currentIndex() == 3:
            self.GarticIoBot()

        elif self.DrawBot_CurrentGame.currentIndex() == 4:
            self.SkribbleIoBot()

        elif self.DrawBot_CurrentGame.currentIndex() == 5:
            self.GarticBot()

    def GarticBot(self):
        self.DrawBot_OutputFrame.setText("Paint Bot aktiviert")
        GarticB = Gartic.GarticBotTest()
        GarticB.Bot(self.ChoosenImg)
        self.DrawBot_OutputFrame.setText("fertig")


    def PaintBot(self):
        self.DrawBot_OutputFrame.setText("Paint Bot aktiviert")
        PaintBot = PaintBotClass.Paint_BOT()
        PaintBot.Bot(self.ChoosenImg)
        self.DrawBot_OutputFrame.setText("fertig")

    def GarticPhoneBot(self):
        self.DrawBot_OutputFrame.setText("Stille Post Bot aktiviert")
        GarticBot = GaticPhoneBotClass.Gartic_Phone_BOT()
        GarticBot.Bot(self.ChoosenImg)
        self.DrawBot_OutputFrame.setText("fertig")

    def SkribbleIoBot(self):
        self.DrawBot_OutputFrame.setText("Skribble Io Bot aktiviert")
        SkribbleBot = SkribbleIO.Skribble_BOT()
        SkribbleBot.Bot(self.ChoosenImg)
        self.DrawBot_OutputFrame.setText("fetig")

    def GarticIoBot(self):
        self.DrawBot_OutputFrame.setText("Gartic IO Bot aktiviert")
        GarticIOBot = Gartic_ioClassification.GarticIOBot()
        GarticIOBot.Bot(self.ChoosenImg)
        self.DrawBot_OutputFrame.setText("fertig")

    def retranslateUi(self, DrawBot_window):
        _translate = QtCore.QCoreApplication.translate
        DrawBot_window.setWindowTitle(_translate("DrawBot_window", "DrawBot: Abonieren kostet nichts XD"))
        self.DrawBot_CommandButton.setText(_translate("DrawBot_window", "Commands"))
        self.DrawBot_Linecall.setText(_translate("DrawBot_window", "Downloaded:"))
        self.DrawBot_Converted.setText(_translate("DrawBot_window", "Converted"))
        self.DrawBot_Name.setText(_translate("DrawBot_window", "Draw Bot by Raider "))
        self.DrawBot_DrawButton.setText(_translate("DrawBot_window", "Draw"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DrawBot_window = QtWidgets.QDialog()
    ui = Ui_DrawBot()
    ui.setupUi(DrawBot_window)
    DrawBot_window.show()
    sys.exit(app.exec_())
