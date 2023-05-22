import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtCore import QTimer, QUrl
from PyQt6.QtMultimedia import QSoundEffect
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("FIA2_Design.ui", self)  

         # Connect buttons to their respective functions
        self.resetScoresButton.clicked.connect(self.reset_scores)
        self.resetTimerButton.clicked.connect(self.reset_timer)
        self.resetAllButton.clicked.connect(self.reset_all)
        self.team1Add1Button.clicked.connect(lambda: self.change_score(1, 1))
        self.team1Add2Button.clicked.connect(lambda: self.change_score(1, 2))
        self.team1SubtractButton.clicked.connect(lambda: self.change_score(1, -1))
        self.team2Add1Button.clicked.connect(lambda: self.change_score(2, 1))
        self.team2Add2Button.clicked.connect(lambda: self.change_score(2, 2))
        self.team2SubtractButton.clicked.connect(lambda: self.change_score(2, -1))
        self.addMinuteButton.clicked.connect(self.add_minute)
        self.addSecondButton.clicked.connect(self.add_second)
        self.startButton.clicked.connect(self.start_clock)
        self.pauseButton.clicked.connect(self.pause_clock)

        # Initialize variables
        self.team1Score = 0
        self.team2Score = 0
        self.clock = QTimer()
        self.clock.timeout.connect(self.change_time)
        self.timeInSeconds = 0

    def reset_scores(self):
        self.team1Score = 0
        self.team2Score = 0
        self.team1ScoreLabel.display(self.team1Score)
        self.team2ScoreLabel.display(self.team2Score)

    def reset_timer(self):
        self.timeInSeconds = 0
        self.update_time()

    def reset_all(self):
        self.reset_scores()
        self.reset_timer()



    def start_clock(self):
        self.clock.stop()

        self._start_clock_with_sound()

    def _start_clock_with_sound(self):
        # Play a sound every seccond before starting 
        for i in range(1, 4):
            QTimer.singleShot(i * 1000, self._play_tick_sound)
            print(i)

        #play a different sound when the timer starts 
        QTimer.singleShot(4000, self. _play_start_sound)

        #Start the timer
        QTimer.singleShot(4000, lambda:self.clock.start(1000))
    
    def _play_tick_sound(self):
        tick_sound = QSoundEffect()
        tick_sound.setSource(QUrl.fromLocalFile("Beep.wav")) 
        tick_sound.play()

    def _play_start_sound(self):
        start_sound = QSoundEffect()
        start_sound.setSource(QUrl.fromLocalFile("Buzzer.wav"))
        start_sound.play()

    
    
    

    def change_score(self, team, points):
        if team == 1:
            self.team1Score += points
            self.team1ScoreLabel.display(self.team1Score)
        elif team == 2:
            self.team2Score += points
            self.team2ScoreLabel.display(self.team2Score)

    def change_time(self):
        self.timeInSeconds -=1
        self.update_time()

    def update_time(self):
        minutes = self.timeInSeconds // 60
        seconds = self.timeInSeconds % 60
        self.clockLabel.display(f"{minutes:02d}:{seconds:02d}")
        

    def add_minute(self):
        self.timeInSeconds += 60
        self.update_time()

    def add_second(self):
        self.timeInSeconds += 1
        self.update_time()

    def start_clock2(self):
        self.clock.start(1000)  # Update every second

    def pause_clock(self):
        self.clock.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())