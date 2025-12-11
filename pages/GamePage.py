from Game import Game
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, controller):
        self.controller = controller
        self.game = Game(self.controller)


    def setupUi(self, MainWindow):

        def next_round():
            pass
        if not self.game: 
            MainWindow.setVisible(False)
        else:
            MainWindow.setVisible(True)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(110, 160, 591, 221))
        self.horizontalFrame.setStyleSheet("background-color: #33658A;\n"
"padding: 1em;\n"
"border-radius: 15px;\n"
"")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playBtn_2 = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.playBtn_2.setFont(font)
        self.playBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playBtn_2.setStyleSheet("background-color: white;")
        self.playBtn_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/rock.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn_2.setIcon(icon)
        self.playBtn_2.setIconSize(QtCore.QSize(250, 250))
        self.playBtn_2.setObjectName("playBtn_2")
        self.horizontalLayout.addWidget(self.playBtn_2)
        self.playBtn_3 = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.playBtn_3.setFont(font)
        self.playBtn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playBtn_3.setStyleSheet("background-color: #c7c0b2;")
        self.playBtn_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/paper.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn_3.setIcon(icon1)
        self.playBtn_3.setIconSize(QtCore.QSize(250, 250))
        self.playBtn_3.setObjectName("playBtn_3")
        self.horizontalLayout.addWidget(self.playBtn_3)
        self.playBtn_4 = QtWidgets.QPushButton(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.playBtn_4.setFont(font)
        self.playBtn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playBtn_4.setAutoFillBackground(False)
        self.playBtn_4.setStyleSheet("border-radius: 15px; overflow: hidden;\n"
"background-color: white;")
        self.playBtn_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/scissors.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn_4.setIcon(icon2)
        self.playBtn_4.setIconSize(QtCore.QSize(200, 200))
        self.playBtn_4.setObjectName("playBtn_4")
        self.horizontalLayout.addWidget(self.playBtn_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("assets/plank_bg.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 460, 181, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "Choose Strategically..."))
        self.pushButton.setText(_translate("MainWindow", "Next Round >"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
