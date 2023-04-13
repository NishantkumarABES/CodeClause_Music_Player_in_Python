from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer
from song_path import songs
mixer.init()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.switch=1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(50, 230, 101, 17))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.setChecked(True)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 260, 91, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 290, 101, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 320, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 350, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(350, 230, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(350, 260, 91, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(350, 290, 91, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(350, 320, 121, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(350, 350, 91, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 111, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/allah-de-bande-gumraah-500-500.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 490, 91, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 520, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 420, 51, 61))
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/play_pause_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.play_pause)

        
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(310, 420, 51, 61))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/next_button.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.forward)
        
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(130, 420, 61, 51))
        self.commandLinkButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/previous_button.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon2)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(self.backward)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 380, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.play_song)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " MUSIC PLAYER"))
        self.radioButton_1.setText(_translate("MainWindow", "Allah de Banda"))
        self.radioButton_2.setText(_translate("MainWindow", "Yaad Aati Hai"))
        self.radioButton_3.setText(_translate("MainWindow", "Never Together"))
        self.radioButton_4.setText(_translate("MainWindow", "Dotara"))
        self.radioButton_5.setText(_translate("MainWindow", "Tere Mere"))
        self.radioButton_6.setText(_translate("MainWindow", "Numaani"))
        self.radioButton_7.setText(_translate("MainWindow", "Dil hai Bholaa"))
        self.radioButton_8.setText(_translate("MainWindow", "Tell Me Once"))
        self.radioButton_9.setText(_translate("MainWindow", "Jee Rahe The Hum"))
        self.radioButton_10.setText(_translate("MainWindow", "Daiyya Daiyya"))
        self.pushButton.setText(_translate("MainWindow", "Loop Play"))
        self.pushButton_2.setText(_translate("MainWindow", "Shuffle Playback"))
        self.pushButton_3.setText(_translate("MainWindow", "Play Song"))
        
    def check(self):
        if self.radioButton_1.isChecked():
            return 1
        elif self.radioButton_2.isChecked():
            return 2
        elif self.radioButton_3.isChecked():
            return 3
        elif self.radioButton_4.isChecked():
            return 4
        elif self.radioButton_5.isChecked():
            return 5
        elif self.radioButton_6.isChecked():
            return 6
        elif self.radioButton_7.isChecked():
            return 7
        elif self.radioButton_8.isChecked():
            return 8
        elif self.radioButton_9.isChecked():
            return 9
        else:
            return 10

    def move(self,n):
        if n==1:
            self.radioButton_1.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/allah-de-bande-gumraah-500-500.jpg"))
        elif n==2:
            self.radioButton_2.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/Yaad-Aati-Hai-Harrdy-Sandhu-500-500.jpg"))
        elif n==3:
            self.radioButton_3.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/never-together-manan-bhardwaj-500-500.jpg"))
        elif n==4:
            self.radioButton_4.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/Dotara-Jubin-Nautiyal-500-500.jpg"))
        elif n==5:
            self.radioButton_5.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/Tere-Mere-Stebin-Ben-500-500.jpg"))
        elif n==6:
            self.radioButton_6.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/numaani-faridkot-500-500.jpg"))
        elif n==7:
            self.radioButton_7.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/dil-hai-bholaa-bholaa-80-80.png"))
        elif n==8:
            self.radioButton_8.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/Tell-Me-Once-Alfaaz-500-500.jpg"))
        elif n==9:
            self.radioButton_9.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/Jee-Rahe-The-Hum-Falling-in-Love-Kisi-Ka-Bhai-Kisi-Ki-Jaan-500-500.jpg"))
        else:
            self.radioButton_10.setChecked(True)
            self.label_2.setPixmap(QtGui.QPixmap("image/daiyya-daiyya-hunter-500-500.jpg"))

    def play_song(self):
        n=self.check()
        mixer.music.load(songs[n])
        mixer.music.play()
    
    def play_pause(self):
        if self.switch==1:
            mixer.music.pause()
            self.switch=0
        elif self.switch==0:
            mixer.music.unpause()
            self.switch=1
        
    
    def forward(self):
        n=self.check()
        if n==10:
            n=0
        print(n)
        self.move(n+1)
        self.play_song()
        
    def backward(self):
        n=self.check()
        if n==1:
            n=11
        self.move(n-1)
        self.play_song()

    def loop(self):
        pass
            
    def shuffle_play(self):
        pass
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
#8130746310
