from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QWidget, QVBoxLayout, QLineEdit, QHBoxLayout,
                             QListWidget)
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosta Lista Zadań")
        self.resize(300, 400)

        # 1. Główny układ
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        # 2. Lista zadań (QListWidget robi całą robotę za nas)
        self.tasksList = QListWidget()
        self.mainLayout.addWidget(self.tasksList)

        # 3. Panel dolny (pole wpisywania i przyciski)
        self.inputLayout = QHBoxLayout()

        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Wpisz zadanie...")

        self.addButton = QPushButton("Dodaj")
        self.deleteButton = QPushButton("Usuń")  # Nowy przycisk

        self.inputLayout.addWidget(self.inputField)
        self.inputLayout.addWidget(self.addButton)
        self.inputLayout.addWidget(self.deleteButton)

        # Dodajemy panel dolny do głównego układu
        self.mainLayout.addLayout(self.inputLayout)

        # 4. Podłączenie przycisków
        self.addButton.clicked.connect(self.addTodo)
        self.deleteButton.clicked.connect(self.removeTodo)

        # Opcjonalnie: dodawanie enterem
        self.inputField.returnPressed.connect(self.addTodo)
    def addTodo(self):
        text = self.inputField.text()

        if text:
            self.tasksList.addItem(text)  # QListWidget ma gotową metodę addItem
            self.inputField.clear()

    def removeTodo(self):
        # Pobieramy numer wiersza, który jest zaznaczony
        row = self.tasksList.currentRow()
        if row >= 0:

            self.tasksList.takeItem(row)
        else:
            print("Zaznacz zadanie do usunięcia!")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
