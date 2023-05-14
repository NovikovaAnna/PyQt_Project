"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""



import time

from PySide6 import QtWidgets, QtGui
from ui1.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.moveOnCoord)
        self.ui.pushButtonLT.clicked.connect(self.moveLeftTop)
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.ui.pushButtonLB.clicked.connect(self.moveLeftBottom)
        self.ui.pushButtonRB.clicked.connect(self.moveRightBottom)
        self.ui.pushButtonCenter.clicked.connect(self.moveCenter)
        self.ui.pushButtonGetData.clicked.connect(self.currentTime)
        self.ui.pushButtonGetData.clicked.connect(self.screenCount)
        self.ui.pushButtonGetData.clicked.connect(self.currentWindow)
        self.ui.pushButtonGetData.clicked.connect(self.screenResolutinon)
        self.ui.pushButtonGetData.clicked.connect(self.currentScreen)
        self.ui.pushButtonGetData.clicked.connect(self.currentSizeWindow)
        self.ui.pushButtonGetData.clicked.connect(self.minSizeWindow)
        self.ui.pushButtonGetData.clicked.connect(self.currentCoordWindow)
        self.ui.pushButtonGetData.clicked.connect(self.centerCoordWindow)
        self.ui.pushButtonGetData.clicked.connect(self.currentStateWindow)

    def moveOnCoord(self):
        x = int(self.ui.spinBoxX.text())
        y = int(self.ui.spinBoxY.text())
        self.move(x, y)


    def moveLeftTop(self):
        self.move(0, 0)

    def moveRightTop(self):
        self.move(1060, 0)

    def moveLeftBottom(self):
        self.move(0, 400)

    def moveRightBottom(self):
        self.move(1060, 400)

    def moveCenter(self):
        self.move(500, 200)

    def currentTime(self):
        self.ui.plainTextEdit.appendPlainText(f"Отчет сформирован: {time.ctime()}")

    def screenCount(self):
        screencount = QtGui.QGuiApplication.screens()
        self.ui.plainTextEdit.appendPlainText(f"Количество экранов: {len(screencount)}")

    def currentWindow(self):
        current_main_window = str(QtWidgets.QApplication.activeWindow())
        self.ui.plainTextEdit.appendPlainText(f"Текущее основное окно: {current_main_window}")

    def screenResolutinon(self):
        desktop = QtGui.QGuiApplication.primaryScreen()
        self.ui.plainTextEdit.appendPlainText(f"Разрешение экрана: {desktop.size()}")
        primary_screen = QtGui.QGuiApplication.primaryScreen()

    def currentScreen(self):
        desktop = QtWidgets.QApplication.screenAt(self.pos())
        self.ui.plainTextEdit.appendPlainText(f"Наименование текущего экрана: {desktop.name()}")

    def currentSizeWindow(self):
        self.ui.plainTextEdit.appendPlainText("Текущий размер окна: " + str(self.size()))

    def minSizeWindow(self):
        self.ui.plainTextEdit.appendPlainText("Минимальный размер окна: " + str(self.minimumSize()))

    def currentCoordWindow(self):
        self.ui.plainTextEdit.appendPlainText("Текущие координаты окна: " + str(self.pos()))

    def centerCoordWindow(self):
        centerX = self.pos().x() / 2
        centerY = self.pos().y() / 2
        self.ui.plainTextEdit.appendPlainText(f"Координаты центра приложения: ({centerX}, {centerY})")

    def currentStateWindow(self):
        winstate = str(self.windowState())
        state = []





        if windowState == "WindowState.WindowMaximized":
            state.append("Развернуто во весь экран")
        elif windowState == "WindowState.WindowMinimized":
            state.append("Свернуто")
        else:
            state.append("Развернуто ")

        if self.isActiveWindow():
            state.append("Активно")
        if not self.isActiveWindow():
            state.append("НеАктивно")

        if self.isVisible():
            state.append("Отображено")
        if not self.isVisible():
            state.append("Скрыто")

        self.ui.plainTextEdit.appendPlainText(f"Состояние окна: {state}")


        def moveEvent(self, event: PySide6.QtGui.QMoveEvent) -> None:
            print(event.oldPosition(),"->", event.position, time.ctime())

        def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
            print(event.size())





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
