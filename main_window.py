import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from scoreboard_ui import Ui_MainWindow


class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

    def show(self):
        self.main_win.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


   


