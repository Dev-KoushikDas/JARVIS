#from _typeshed import Self
from jarvisqtUI import Ui_jarvisui
from PyQt5 import QtCore , QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import random
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(self):

    speak("allow me to introduce myself.    I am Jarvis !!       a virtual       artificial intelligence  !!!        and      I am here   to assist you       in a variety of tasks!!   as best as I can!!! .        Twenty four hours a day.......      seven days a week!!!")
    speak("importing all database from main server!! ,...................................")
    speak("systems now fully operational")
    hour = (datetime.datetime.now().hour)
    if hour>=7 and hour<12:
        speak("Good Morning sir!")

    elif hour>=4 and hour<7:
        speak("It's too early in the morning sir!")        

    elif hour>=0 and hour<4:
        speak("It seems you are working late night sir!")      

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir !")  

    speak("how may I help you?")    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




class MainThread(QThread):
    def _init_(self):
        super(MainThread,self).__init__()


    def run(self):
        self.Task_Gui()
    


    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return self.query


    def Task_Gui(self):
        
        if __name__ == "__main__":
            wishMe(self)
            while True:
            # if 1:
                self.query = self.takeCommand().lower()

                # Logic for executing tasks based on query
                if ('who is' or'what is') in self.query:
                    speak('Searching ...')
                    self.query = self.query.replace("wikipedia", "")
                    self.query = self.query.replace("jarvis", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                
                elif ('youtube search' or 'search youtube') in self.query:
                    
                    self.query = self.query.replace("jarvis", "")
                    self.query = self.query.replace("youtube", "")
                    self.query = self.query.replace("search", "")
                    self.query = self.query.replace("for", "")
                    result = "https://www.youtube.com/results?search_query=" + self.query
                    webbrowser.open(result)
                    speak('Searching')
                    speak(self.query)
                    speak("this is what I found sir!")
                    pywhatkit.playonyt(result)

                elif ('amazon search ' or 'search amazon') in self.query:
                    
                    self.query = self.query.replace("jarvis", "")
                    self.query = self.query.replace("amazon", "")
                    self.query = self.query.replace("search", "")
                    self.query = self.query.replace("for", "")
                    result = "https://www.amazon.in/s?k="+ self.query+"&ref=nb_sb_noss_2" 
                    speak('Searching')
                    speak(self.query)
                    webbrowser.open(result)
                    speak("this is what I found sir!")  
                
                elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")

                elif 'open google' in self.query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com")   


                elif ('play music' or 'play song') in self.query:
                    music_dir = 'C:\\Users\\joy\\Downloads\\music'
                    songs = os.listdir(music_dir)
                    print(songs)  
                    #os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in self.query:
                    codePath = "C:\\Users\\joy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                ##chrome automation , normal interaction, maths ans science, imporved gui
                elif 'email to Joy' in self.query:
                    try:
                        speak("What should I say?")
                        content = self.takeCommand()
                        to = "das.koushik881@gmail.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        #print(e)
                        speak("Sorry sir. I am not able to send this email")     

startFunction = MainThread()


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisui(object):
    def setupUi(self, jarvisui):
        jarvisui.setObjectName("jarvisui")
        jarvisui.resize(1920, 1080)
        self.label = QtWidgets.QLabel(jarvisui)
        self.label.setGeometry(QtCore.QRect(-20, -80, 2181, 1231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\black.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(jarvisui)
        self.label_3.setGeometry(QtCore.QRect(510, 200, 571, 861))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\download.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(jarvisui)
        self.label_2.setGeometry(QtCore.QRect(1560, -30, 341, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\212f727d1a5f117947db9a7403a4f7aa.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(jarvisui)
        self.label_4.setGeometry(QtCore.QRect(0, -70, 491, 251))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\T8bahf.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(jarvisui)
        self.label_5.setGeometry(QtCore.QRect(1060, 330, 311, 251))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\9e759fd37ccd98da121b670249f34afa.gif"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(jarvisui)
        self.label_7.setGeometry(QtCore.QRect(540, -70, 601, 261))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\704e26aa3f8b06f0c367a25c0874ba4b.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(jarvisui)
        self.label_8.setGeometry(QtCore.QRect(-40, 780, 361, 221))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\SpotlessWelloffAtlanticridleyturtle-max-1mb.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(jarvisui)
        self.label_6.setGeometry(QtCore.QRect(-10, 120, 461, 321))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\MImN.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(jarvisui)
        self.label_9.setGeometry(QtCore.QRect(-30, 410, 541, 361))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\7a517efee6880af7aa39f0aa707281a1.gif"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(jarvisui)
        self.label_10.setGeometry(QtCore.QRect(1200, 30, 331, 251))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\ceb11f58fa11f9b8c151cc3a4ce49b71.gif"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(jarvisui)
        self.label_11.setGeometry(QtCore.QRect(1000, 560, 411, 471))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\giphy (1).gif"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(jarvisui)
        self.label_12.setGeometry(QtCore.QRect(320, 690, 371, 361))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\06.gif"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(jarvisui)
        self.label_13.setGeometry(QtCore.QRect(1380, 340, 491, 181))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\normal-heart-rate1.gif"))
        self.label_13.setObjectName("label_13")
        self.pushButton_2 = QtWidgets.QPushButton(jarvisui)
        self.pushButton_2.setGeometry(QtCore.QRect(1720, 980, 141, 61))
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 175, 195, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_14 = QtWidgets.QLabel(jarvisui)
        self.label_14.setGeometry(QtCore.QRect(1530, 560, 351, 91))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\btn3.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(jarvisui)
        self.label_15.setGeometry(QtCore.QRect(1640, 620, 2181, 1231))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\black.png"))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(jarvisui)
        self.label_16.setGeometry(QtCore.QRect(1530, 670, 351, 91))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\btn3.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(jarvisui)
        self.label_17.setGeometry(QtCore.QRect(1530, 790, 351, 91))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\btn3.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(jarvisui)
        self.label_18.setGeometry(QtCore.QRect(1540, 920, 351, 91))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("C:\\Users\\joy\\c programming\\JARVIS\\btn3.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.pushButton = QtWidgets.QPushButton(jarvisui)
        self.pushButton.setGeometry(QtCore.QRect(1650, 810, 121, 41))
        self.pushButton.setStyleSheet("font: 75 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Wide Latin\";\n"
"background-color: rgb(0, 96, 144);\n"
"background-color: rgb(21, 122, 153);\n"
"font: 75 18pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(jarvisui)
        self.pushButton_3.setGeometry(QtCore.QRect(1640, 940, 161, 41))
        self.pushButton_3.setStyleSheet("font: 75 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Wide Latin\";\n"
"background-color: rgb(0, 96, 144);\n"
"background-color: rgb(21, 122, 153);\n"
"font: 75 18pt \"Segoe UI\";")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(jarvisui)
        QtCore.QMetaObject.connectSlotsByName(jarvisui)

    def retranslateUi(self, jarvisui):
        _translate = QtCore.QCoreApplication.translate
        jarvisui.setWindowTitle(_translate("jarvisui", "MainWindow"))
        #self.pushButton_2.setText(_translate("jarvisui", "FINISH"))
        self.pushButton.setText(_translate("jarvisui", "START"))
        self.pushButton_3.setText(_translate("jarvisui", "TERMINATE"))






class Gui_Start(QMainWindow):

    def _init_(self):

        super()._init_()
        self.jarvis_ui = Ui_jarvisui()  
        self.jarvis_ui.setupUi(self)

        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_3.clicked.connect(self.close)
        
    def startFunc(self):

        self.jarvis_ui.movies_3 = QtWidgets.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\download.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()


startFunction.start()

app = QtWidgets.QApplication(sys.argv)
jarvisui = QtWidgets.QWidget()




ui = Ui_jarvisui()
ui.setupUi(jarvisui)

ui.movies_3 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\download.gif")
ui.label_3.setMovie(ui.movies_3)
ui.movies_3.start()

ui.movies_2 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\212f727d1a5f117947db9a7403a4f7aa.gif")
ui.label_2.setMovie(ui.movies_2)
ui.movies_2.start()

ui.movies_4 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\T8bahf.gif")
ui.label_4.setMovie(ui.movies_4)
ui.movies_4.start()

ui.movies_5 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\9e759fd37ccd98da121b670249f34afa.gif")
ui.label_5.setMovie(ui.movies_5)
ui.movies_5.start()

ui.movies_7 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\704e26aa3f8b06f0c367a25c0874ba4b.gif")
ui.label_7.setMovie(ui.movies_7)
ui.movies_7.start()

ui.movies_8 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\SpotlessWelloffAtlanticridleyturtle-max-1mb.gif")
ui.label_8.setMovie(ui.movies_8)
ui.movies_8.start()

ui.movies_6 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\MImN.gif")
ui.label_6.setMovie(ui.movies_6)
ui.movies_6.start()

ui.movies_9 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\7a517efee6880af7aa39f0aa707281a1.gif")
ui.label_9.setMovie(ui.movies_9)
ui.movies_9.start()

ui.movies_11 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\giphy (1).gif")
ui.label_11.setMovie(ui.movies_11)
ui.movies_11.start()

ui.movies_10 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\ceb11f58fa11f9b8c151cc3a4ce49b71.gif")
ui.label_10.setMovie(ui.movies_10)
ui.movies_10.start()

ui.movies_12 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\06.gif")
ui.label_12.setMovie(ui.movies_12)
ui.movies_12.start()

ui.movies_13 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\normal-heart-rate1.gif")
ui.label_13.setMovie(ui.movies_13)
ui.movies_13.start()




#Gui_Start().show()
jarvisui.show()
sys.exit(app.exec_())


#Gui_App =QtWidgets.QApplication(sys.argv) 
#Gui_Jarvis = QtWidgets.Gui_Start()
#ui = Ui_jarvisui()
#ui.setupUi(jarvisui)
#Gui_Jarvis.show()
#sys.exit(Gui_App.exec_())        