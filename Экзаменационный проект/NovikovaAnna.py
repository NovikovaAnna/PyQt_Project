"""
Реализовать приложение для работы с заметками
Обязательные функции в приложении:
* Добавление, изменение, удаление заметок
* Сохранение времени добавления заметки и отслеживание времени до дэдлайна.
* Реализация хранения заметок остаётся на ваш выбор (БД, json и т.д.).
"""

import datetime
import json

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QColor, QMovie
from Ex1_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """Инициализация основного окна приложения."""
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.notes = []  # Список для хранения заметок

        self.load_notes()  # Загрузка заметок из файла JSON

        self.ui.saveButton.clicked.connect(self.save_note)
        self.ui.delete_Button.clicked.connect(self.delete_note)

        self.update_tree_widget()

        self.setStyleSheet(
            "background-color: #FFE4E1; color: #800080;"
        )  # Установка цвета фона - розовый, цвета текста - пурпурный

        self.ui.saveButton.setStyleSheet(
            "background-color: #FF69B4; color: #FFFFFF;"
        )  # Установка цвета кнопки сохранения - ярко-розовый, цвета текста - белый
        self.ui.delete_Button.setStyleSheet(
            "background-color: #FF1493; color: #FFFFFF;"
        )  # Установка цвета кнопки удаления - тёмно-розовый, цвета текста - белый

        # Создание QLabel для отображения анимации GIF
        self.gif_label = QtWidgets.QLabel(self)
        self.gif_label.setGeometry(300, 300, 400, 400)
        self.gif_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gif_label.setStyleSheet("background-color: transparent;")

        # Загрузка анимации GIF
        movie = QMovie("dog.gif")
        self.gif_label.setMovie(movie)
        movie.start()

        # Задержка отображения формы на 3 секунды
        QtCore.QTimer.singleShot(3000, self.hide_gif)

    def load_notes(self):
        """Загрузка заметок из файла JSON."""
        try:
            with open("notes.json") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        """Сохранение заметок в файл JSON."""
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)

    def update_tree_widget(self):
        """Обновление виджета дерева заметок."""
        self.ui.treeWidget.clear()

        for note in self.notes:
            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, note["note"])
            item.setText(1, note["date"])
            item.setText(2, note["deadline"])
            self.ui.treeWidget.addTopLevelItem(item)

    def save_note(self):
        """Сохранение новой заметки."""
        note_text = self.ui.lineEdit.text()
        deadline = self.ui.dateTimeEdit.dateTime().toString("dd/MM/yyyy HH:mm")
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        note = {
            "note": note_text,
            "date": current_date,
            "deadline": deadline,
        }

        self.notes.append(note)
        self.save_notes()

    def delete_note(self):
        """Удаление выбранной заметки."""
        selected_indexes = self.ui.treeWidget.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            note_index = selected_index.row()

            if 0 <= note_index < len(self.notes):
                del self.notes[note_index]
                self.save_notes()
                self.update_tree_widget()

    def hide_gif(self):
        """Скрытие анимации GIF."""
        self.gif_label.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()






