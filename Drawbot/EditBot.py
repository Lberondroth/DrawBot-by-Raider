from PyQt5 import QtCore, QtGui, QtWidgets
import time
import pyautogui
import keyboard
import os
import sys


class Ui_EditBot(object):
    def __init__(self):
        self.AllowExit = False

    def EditBotUI(self, EditBot):
        EditBot.setObjectName("EditBot")
        EditBot.resize(373, 330)

        self.Background = QtWidgets.QLabel(EditBot)
        self.Background.setGeometry(QtCore.QRect(-10, -10, 391, 351))
        self.Background.setPixmap(
            QtGui.QPixmap("Bilder/Cover_2.0.jpg"))
        self.Background.setScaledContents(True)

        self.EditBot_DrawModeButton = QtWidgets.QPushButton(EditBot)
        self.EditBot_DrawModeButton.setGeometry(QtCore.QRect(170, 260, 131, 51))
        self.EditBot_DrawModeButton.setStyleSheet("background-color:black;\n"
                                                  "color:darkred;\n"
                                                  "border-style: outset;\n"
                                                  "border-width:2px;\n"
                                                  "border-radius: 4px;\n"
                                                  "font: 57 13pt \"MagdaClean\";")
        self.EditBot_DrawModeButton.clicked.connect(self.Exit)

        self.EditBot_RdyBox = QtWidgets.QPushButton(EditBot)
        self.EditBot_RdyBox.setGeometry(QtCore.QRect(30, 40, 310, 51))
        self.EditBot_RdyBox.setStyleSheet("background-color:black;\n"
                                          "color:darkred;\n"
                                          "border-style: outset;\n"
                                          "border-width:2px;\n"
                                          "border-radius: 4px;\n"
                                          "font: 57 13pt \"MagdaClean\";")

        self.EditBot_CrntColor = QtWidgets.QLabel(EditBot)
        self.EditBot_CrntColor.setGeometry(QtCore.QRect(150, 100, 120, 90))
        self.EditBot_CrntColor.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.EditBot_currentColorLabel = QtWidgets.QLabel(EditBot)
        self.EditBot_currentColorLabel.setGeometry(QtCore.QRect(30, 90, 120, 71))
        self.EditBot_currentColorLabel.setStyleSheet("background-color:black;\n"
                                                     "color:darkred;\n"
                                                     "border-style: outset;\n"
                                                     "border-width:2px;\n"
                                                     "border-radius: 4px;\n"
                                                     "font: 57 13pt \"MagdaClean\";")

        self.EditBot_Label = QtWidgets.QLabel(EditBot)
        self.EditBot_Label.setGeometry(QtCore.QRect(20, 10, 90, 16))
        self.EditBot_Label.setStyleSheet("background-color:black;\n"
                                         "color:darkred;\n"
                                         "border-style: outset;\n"
                                         "border-width:2px;\n"
                                         "border-radius: 4px;\n"
                                         "font: 57 13pt \"MagdaClean\";")

        self.EditBot_BotName = QtWidgets.QLineEdit(EditBot)
        self.EditBot_BotName.setGeometry(QtCore.QRect(20, 220, 281, 20))
        self.EditBot_BotName.setStyleSheet("font: 57 11pt \"MagdaClean\";\n"
                                           "color: darkred;\n"
                                           "background-color: Black;\n"
                                           "border-style: Outset;\n"
                                           "border-color: Darkred;\n"
                                           "border-width:2px;\n"
                                           "border-radius: 4px")

        self.EditBot_BotName.setText("test")

        self.EditBot_BotLabel = QtWidgets.QLabel(EditBot)
        self.EditBot_BotLabel.setGeometry(QtCore.QRect(20, 190, 170, 16))
        self.EditBot_BotLabel.setStyleSheet("background-color:black;\n"
                                            "color:darkred;\n"
                                            "font: 57 13pt \"MagdaClean\";")

        self.EditBot_ActiveButton = QtWidgets.QPushButton(EditBot)
        self.EditBot_ActiveButton.setGeometry(QtCore.QRect(20, 260, 131, 51))
        self.EditBot_ActiveButton.setStyleSheet("background-color:black;\n"
                                                "color:darkred;\n"
                                                "border-style: outset;\n"
                                                "border-width:2px;\n"
                                                "border-radius: 4px;\n"
                                                "font: 57 13pt \"MagdaClean\";")
        self.EditBot_ActiveButton.clicked.connect(self.ActivateEditBot)

        self.retranslateUi(EditBot)
        QtCore.QMetaObject.connectSlotsByName(EditBot)

    def ActivateEditBot(self):
        if self.EditBot_BotName.text() == "":
            print("pls enter a name for the bot")
        else:
            print(self.EditBot_BotName.text())
            self.AllowExit = True
            self.botName = self.EditBot_BotName.text()
            self.Position = []
            self.Colors = []
            self.ActiveTimer = QtCore.QTimer()
            self.C_ok = 1

            self.EditBot_RdyBox.setStyleSheet("background-color:black;\n"
                                              "color:green;\n"
                                              "border-style: outset;\n"
                                              "border-width:2px;\n"
                                              "border-radius: 4px;\n"
                                              "font: 57 13pt \"MagdaClean\";")
            self.ActiveTimer.timeout.connect(self.CollectData)
            self.ActiveTimer.start(50)

    def CollectData(self):
        if keyboard.is_pressed("c") and self.C_ok == 1:
            self.C_ok = 0
            self.EditBot_RdyBox.setStyleSheet("background-color:black;\n"
                                              "color:darkred;\n"
                                              "border-style: outset;\n"
                                              "border-width:2px;\n"
                                              "border-radius: 4px;\n"
                                              "font: 57 13pt \"MagdaClean\";")
            self.delay = QtCore.QTimer()
            self.delay.setSingleShot(True)
            self.delay.timeout.connect(self.GetPosition)
            self.delay.start(1000)

    def GetPosition(self):

        MOUSE_X, MOUSE_Y = pyautogui.position()
        COLOR = pyautogui.pixel(MOUSE_X, MOUSE_Y)

        self.Position.append((MOUSE_X, MOUSE_Y))

        self.Colors.append((COLOR.__str__()))
        self.EditBot_CrntColor.setStyleSheet("background-color: rgb%s;" % str((COLOR)))
        print(self.Colors)
        print(self.Position)

        self.C_ok = 1
        self.EditBot_RdyBox.setStyleSheet("background-color:black;\n"
                                          "color:green;\n"
                                          "border-style: outset;\n"
                                          "border-width:2px;\n"
                                          "border-radius: 4px;\n"
                                          "font: 57 13pt \"MagdaClean\";")

    def Exit(self):
        if self.AllowExit:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            Speicher = dir_path + "\Speicher"
            Botname = self.CheckName(Speicher)
            Botname = str(Botname)
            if Botname == "None" or None:
                print(f"{self.botName} ist ok create new Bot")
                Botfiledir = os.path.join(Speicher, self.botName)
                Botfile = open(Botfiledir, "w")
            else:
                print(f"File existed new Botname is {Botname}")
                Botfiledir = os.path.join(Speicher, Botname)
                Botfile = open(Botfiledir, "w")
            print("Bot got created")
            print(self.Colors)
            print(self.Position)
            for colums in range(0, len(self.Colors)):
                Botfile.write(f"{self.Colors[colums]} | {self.Position[colums]} \n")
            Botfile.close()

        else:
            print("Activate the Bot first")

    def CheckName(self, Speicher, number=0):
        for i in os.listdir(Speicher):
            print(i)
            if i == self.botName:
                print(f"Error {self.botName} already exists!")
                self.botName = self.botName + str(number)
                number = number + 1
                self.CheckName(Speicher, number)
                return self.botName
            else:
                pass

    def retranslateUi(self, EditBot):
        _translate = QtCore.QCoreApplication.translate
        EditBot.setWindowTitle(_translate("EditBot", "EditBot: Abonieren kostet nichts"))
        self.EditBot_DrawModeButton.setText(_translate("EditBot", "DrawMode"))
        self.EditBot_RdyBox.setText(_translate("EditBot", "New Color can be selected with \"c\""))
        self.EditBot_CrntColor.setText(_translate("EditBot", ""))
        self.EditBot_currentColorLabel.setText(_translate("EditBot", "Current Color:"))
        self.EditBot_Label.setText(_translate("EditBot", "Edit Mode:"))
        self.EditBot_BotLabel.setText(_translate("EditBot", "Name of the Bot:"))
        self.EditBot_ActiveButton.setText(_translate("EditBot", "Aktivate:"))


