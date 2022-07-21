from platform import java_ver
from jarvisqtUI import Ui_jarvisui
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import jarvis


class MainThread(QThread):
    def _init_(self):
        super(MainThread,self).__init__()

    def run(self):
        jarvis.condnfunc()

   
        

startFunction = MainThread()

class Gui_Start(QMainWindow):

    def _init_(self):
        super()._init_()
        self.gui = Ui_jarvisui()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startFunc)
        self.gui.pushButton_3.clicked.connect(self.close)
        
    def startFunc(self):

        self.gui.movies3 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\download.gif")
        self.gui.label_3.setMovie(self.gui.movies3)
        self.gui.movies3.start()

        
        self.gui.movies2 = QtGui.QMovie("C:\\Users\\joy\\c programming\\JARVIS\\212f727d1a5f117947db9a7403a4f7aa.gif")
        self.gui.label_3.setMovie(self.gui.movies2)
        self.gui.movies2.start()



startFunction.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())                  