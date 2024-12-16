import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Нажмите кнопку', self)
        self.button = QPushButton('Нажми на меня', self)
        self.button.setStyleSheet("background-color: lightblue;")
        self.label.setStyleSheet("font-size: 20px; color: darkgreen;")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.on_button_click)
        self.setWindowTitle('Простое приложение')
        self.setGeometry(100, 100, 300, 200)
        self.show()
    def on_button_click(self):
        self.label.setText("Кнопка нажата!")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleApp()
    sys.exit(app.exec_())
