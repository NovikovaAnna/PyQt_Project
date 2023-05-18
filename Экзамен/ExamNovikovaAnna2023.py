import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, \
    QPushButton, QListWidget, QMessageBox, QDialog, QDateTimeEdit
from PySide6.QtCore import Qt, QDateTime

class Note:
    def __init__(self, title, content, deadline):
        self.title = title
        self.content = content
        self.deadline = deadline
        self.created_at = QDateTime.currentDateTime().toString(Qt.ISODate)

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'deadline': self.deadline,
            'created_at': self.created_at
        }

class AddNoteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Добавить заметку')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel('Заголовок:')
        self.layout.addWidget(self.title_label)

        self.title_edit = QLineEdit()
        self.layout.addWidget(self.title_edit)

        self.content_label = QLabel('Содержимое:')
        self.layout.addWidget(self.content_label)

        self.content_edit = QTextEdit()
        self.layout.addWidget(self.content_edit)

        self.deadline_label = QLabel('Дедлайн:')
        self.layout.addWidget(self.deadline_label)

        self.deadline_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.layout.addWidget(self.deadline_edit)

        self.button_box = QDialog.ButtonBox(QDialog.ButtonBox.Ok | QDialog.ButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

#     def get_note_data(self):
#         title = self.title_edit.text()
#         content = self.content_edit.toPlainText()
#         deadline = self.deadline_edit.dateTime().toString(Qt.ISODate)
#         return title, content, deadline
#
# class NotesApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Заметки')
#         self.resize(400, 300)
#
#         self.notes = []
#
#         self.init_ui()
#
#     def init_ui(self):
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#
#         self.layout = QVBoxLayout()
#         self.central_widget.setLayout(self.layout)
#
#         self.notes_list = QListWidget()
#         self.layout.addWidget(self.notes_list)
#
#         self.add_button = QPushButton('Добавить заметку')
#         self.add_button.clicked.connect(self.add_note)
#         self.layout.addWidget(self.add_button)
#
#         self.edit_button = QPushButton('Редактировать заметку')
#         self.edit_button.clicked.connect(self.edit_note)
#         self.layout.addWidget(self.edit_button)
#
#         self.delete_button = QPushButton('Удалить заметку')
#         self.delete_button.clicked.connect(self.delete_note)
#         self.layout.addWidget(self.delete_button)
#
#         self.load_notes()

    # def load_notes(self):
    #     try:
    #         with open('notes.json', 'r') as file:
    #             notes_data =


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()