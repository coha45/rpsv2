from PyQt5 import QtCore, QtGui, QtWidgets
from pages.MainPage import Ui_MainWindow as MainWindow
from pages.test import Ui_MainWindow as TestWindow
from pages.GamePage import Ui_MainWindow as GameWindow

class Controller:
    def __init__(self):
        self.stack_widget = QtWidgets.QStackedWidget()

        self.rounds = 3
        self.wins = 0
        self.losses = 0
        self.log = [] # Clash Royale Reference

        for W in (MainWindow, GameWindow):
            window = QtWidgets.QMainWindow()
            page = W(self)
            self.stack_widget.addWidget(window)
            page.setupUi(window)

    def set_window(self, index):
        self.stack_widget.setCurrentIndex(index)

    def start(self):
        self.set_window(0)
        self.stack_widget.resize(800, 600)
        self.stack_widget.show()

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Controller()
    ui.start()
    sys.exit(app.exec_())