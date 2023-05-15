from PyQt6.QtCore import QTimer

class Timer:
    def __init__(self, configuration, soundManager, seccondsLabel, minuetsLabel):
        self.currentTime = configuration.time
        self.maxTime = self.maxTime
        self.active = False
        self.soundManager = soundManager

        self.miuetsLabel = minuetsLabel
        self.seccondsLabel = seccondsLabel 

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    def showTime(self):
        if self.active:
            self.currentTime -= 1 
            
            if self.currentTime == 0:
                self.endTimer()
        
        self.seccondslabel.setproperty("intValue", int(self.currentTime/60))
        self.minuetsLabel.setproperty("intValue", int(self.currentTime%60))


        






        



        pass