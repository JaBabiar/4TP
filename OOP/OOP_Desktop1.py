
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciastko klikacz")
        self.resize(700,600)
        self.layout = QVBoxLayout()
        self.score = 0
        self.mnoznik = 1
        self.button = QPushButton("Ciastko")
        self.wynik = QLabel(f"Punkty: {self.score}")
        self.input =QLineEdit()
        self.input.setStyleSheet("max-height: 40px")
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.wynik)

        self.button.clicked.connect(self.licznik)
        self.input.editingFinished.connect(self.setMnoznik)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.mainWidget)

    def licznik(self):
        self.score += 1*self.mnoznik
        self.wynik.setText(f"Punkty: {self.score}")
        #self.wynik.setStyleSheet(f"font-size: {self.score}px")
    def setMnoznik(self):
        print("Edit Finished")
        try:
            num = int(self.input.text())
            if num != self.mnoznik:
                self.mnoznik = num
        except ValueError:
            print(ValueError)

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()


