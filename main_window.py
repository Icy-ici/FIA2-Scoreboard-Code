import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from scoreboard_ui import Ui_MainWindow

class MainWindow:
    def __init__(self):

        ## --- setup UI elements --- ##
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        ## --- Initialise scoreboard variables --- ##
        self.Team1_name = ""
        self.Team2_name = ""
        self.Team1_logo = ""
        self.Team2_logo = ""
        self.Team1_score = 0
        self.Team2_score = 0
        self.Presets = 0
        ## --- Initialise the UI with starting values --- ###
        



    def show(self):
        self.main_win.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


   


