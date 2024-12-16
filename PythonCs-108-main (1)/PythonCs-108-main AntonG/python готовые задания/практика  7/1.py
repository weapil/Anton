import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Приложение для заметок')
        self.setGeometry(100, 100, 600, 400)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.create_menu()
    def create_menu(self):
        menu_bar = self.menuBar()
        new_note_action = QAction('Новая заметка', self)
        new_note_action.triggered.connect(self.new_note)
        save_note_action = QAction('Сохранить заметку', self)
        save_note_action.triggered.connect(self.save_note)
        file_menu = menu_bar.addMenu('Файл')
        file_menu.addAction(new_note_action)
        file_menu.addAction(save_note_action)
    def new_note(self):
        self.text_edit.clear()
    def save_note(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить заметку", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    note_app = NoteApp()
    note_app.show()
    sys.exit(app.exec_())
