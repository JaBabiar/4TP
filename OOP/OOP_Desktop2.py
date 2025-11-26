
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zadania")
        self.mainLayout = QVBoxLayout()
        self.inputLayout = QHBoxLayout()


        self.mainWidget = QWidget()
        self.inputWidget = QWidget()
        self.inputField = QLineEdit()
        self.submitButton = QPushButton("Dodaj")

        self.inputLayout.addWidget(self.inputField)
        self.inputLayout.addWidget(self.submitButton)
        self.mainWidget.setLayout(self.mainLayout)
        self.inputWidget.setLayout(self.inputLayout)

        self.mainLayout.addWidget(self.inputWidget)

        self.setCentralWidget(self.mainWidget)

        self.submitButton.clicked.connect(self.addTodo)

    def addTodo(self):
        labelText = self.inputField.text()
        self.mainLayout.addWidget(QLabel(labelText))
        self.inputField.setText("")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()


