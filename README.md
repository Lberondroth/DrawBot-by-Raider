# DrawBot-by-Raider
Dies ist ein Drawbot, welcher von mir in Python geschrieben worden ist. Er funktioniert in jedem Spiel.
Wahrscheinlich müsst ihr euch noch ein paar Sachen mit pip instalieren aber das solltet ihr selber hinbekommen

In dem Ordner Drawbot gibt es 2 Hauptprogramme einmal den Drawbot und einmal test color. 
Test color verwendet man um eine weitere Klasse für den zu programieren.

Vorsicht könnte kompliziert werden btw. der Code ist nicht gerade optimiert also ich glaub da an euch XD
Um den Bot zu starten Drawbot.py starten Modus wählen (1920*1080 bemessen). Anschließend auf Draw clicken und den Namen eingeben mit W A S D Bild wechseln Y bestätigen.
Nach kurzer Zeit öffnet sich das gewünschte Bild und der Bot fängt von der aktuellen Mausposition an zu zeichen.

Neue Klasse erstellen:
Schritt 1:
test color starten

Schritt 2:
über die gewünschten Farbe eines Spiels hovern und B für jede Farbe clicken

Schritt 3:
Datei mit dem Namen "ka was auch immer" wählen: Vorsicht dabei nicht die Tasten "d" "p" oder "p" clicken

Schritt 4: 
die Skribble IO Datei öffnen und in die vorherige Datei kopieren

Schritt 5:
Positionen löschen und "p" drücken

Schritt 6:
Farben löschen und "c" drücken

Schritt 7:
Wörterbuch löschen und "d" drücken. Anschließend könnt ihr test colors wieder schließen 

Schritt 8:
die Buchstaben aus der Datei löschen, welche vor den Variabeln stehen "p","c","d"

Schritt 9:
Falls man mehr als 21 Farben hat in self.Colors die Farben hinzufügen mit Color_22, Color_23 usw. Hat man weniger als 21 Farben die übrigen einfach löschen

Schritt 10:
Anschließend die Klasse umbennen damit sie nicht mehr "Skribble_BOT" heißt

in der Datei vom Drawbot:

User Agent eintragen (Google: My User agent) Text Copy paste
Schritt 11:
import (die eben erstellte Datei)

Schritt 12:
self.DrawBot_CurrentGame.addItem("gewünschtes Spiel")

Schritt 13:
in der Funktion BotModus
        elif self.DrawBot_CurrentGame.currentIndex() == nächste Zahl:
            self."neueFunktion"
eintippen
Schritt 14:
neueFunktion erstellen

BSP:
    def Malen(self):
        self.DrawBot_OutputFrame.setText("Mal bot aktiviert")
        MalBot = MalBot.BotMal()  #eben importiertes Modul mit der Klasse aufrufen
        MalBot.Bot(self.ChoosenImg) 
        self.DrawBot_OutputFrame.setText("fertig")

Schritt 15:
gegebenfalls im neuerstellten Modul die time.sleep Zahlen erhöhen oder niedriger stellen. Je nach dem wie schnell das System oder die Seite ist variert die Zeit 

zwischen 10 Sekunden und 15 Minuten um ein Bild zu malen.
Grund dafür ist das der Bot zwischen jedem Pixel warten muss und bei 5600Pxl kann das ganz schön lange dauern.
