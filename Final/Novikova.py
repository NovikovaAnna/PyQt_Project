"""
Реализовать приложение для работы с заметками
Обязательные функции в приложении:
* Добавление, изменение, удаление заметок
* Сохранение времени добавления заметки и отслеживание времени до дэдлайна.
* Реализация хранения заметок остаётся на ваш выбор (БД, json и т.д.).
                """


import datetime
import json

from PySide6 import QtWidgets
from PySide6.QtGui import QColor
from Ex_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.notes = []  # List to store notes

        self.load_notes()  # Load notes from JSON file

        self.ui.saveButton.clicked.connect(self.save_note)
        self.ui.delete_Button.clicked.connect(self.delete_note)

        self.update_tree_widget()

        self.setStyleSheet(
            "background-color: #FFC0CB; color: #800080;")  # Set background color to pink and text color to purple

        self.ui.saveButton.setStyleSheet(
            "background-color: #FF69B4; color: #FFFFFF;")  # Set save button color to hot pink and text color to white
        self.ui.delete_Button.setStyleSheet(
            "background-color: #FF1493; color: #FFFFFF;")  # Set delete button color to deep pink and text color to white
        self.ui.newNoteButton.setStyleSheet(
            "background-color: #FFB6C1; color: #800080;")  # Set new note button color to light pink and text color to purple

    def load_notes(self):
        try:
            with open('notes.json') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file)

    def update_tree_widget(self):
        self.ui.treeWidget.clear()

        for note in self.notes:
            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, note['note'])
            item.setText(1, note['date'])
            item.setText(2, note['deadline'])
            self.ui.treeWidget.addTopLevelItem(item)

    def save_note(self):
        note_text = self.ui.lineEdit.text()
        deadline = self.ui.dateTimeEdit.dateTime().toString("dd/MM/yyyy HH:mm")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        note = {
            'note': note_text,
            'date': current_date,
            'deadline': deadline
        }

        self.notes.append(note)
        self.save_notes()
        self.update_tree_widget()

    def delete_note(self):
        selected_items = self.ui.treeWidget.selectedItems()
        if selected_items:
            item = selected_items[0]
            note_text = item.text(0)
            for note in self.notes:
                if note['note'] == note_text:
                    self.notes.remove(note)
                    self.save_notes()
                    self.update_tree_widget()
                    break


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()

