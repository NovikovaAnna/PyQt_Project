"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в  консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from ui1.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["dec", "bin", "oct", "hex"])

        self.settings = QtCore.QSettings("myapp", "d_eventfilter_settings")
        self.ui.comboBox.setCurrentIndex(self.settings.value("display_mode", 0))
        self.ui.lcdNumber.display(self.settings.value("lcd_value", 0))
        self.ui.dial.setValue(self.settings.value("dial_value", 0))
        self.ui.horizontalSlider.setValue(self.settings.value("horizontalSlider_value", 0))

        self.ui.dial.installEventFilter(self)
        self.ui.dial.valueChanged.connect(self.valueChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.displayModeChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.valueChanged)

    def eventFilter(self, watched, event):
        if watched == self.ui.dial:
            if event.type() == QtCore.QEvent.KeyPress:
                key = event.key()
                if key == QtCore.Qt.Key_Plus:
                    self.ui.dial.setValue(self.ui.dial.value() + 1)
                    return True
                elif key == QtCore.Qt.Key_Minus:
                    self.ui.dial.setValue(self.ui.dial.value() - 1)
                    return True
        return super().eventFilter(watched, event)

    def valueChanged(self, value):
        self.ui.lcdNumber.display(value)
        self.saveValues()

    def displayModeChanged(self, index):
        self.saveValues("display_mode", index)
        self.updateLCDNumberFormat()

    def updateLCDNumberFormat(self):
        display_mode = self.settings.value("display_mode", 0)
        if display_mode == 0:
            self.ui.lcdNumber.setDecMode()
        elif display_mode == 1:
            self.ui.lcdNumber.setBinMode()
        elif display_mode == 2:
            self.ui.lcdNumber.setOctMode()
        elif display_mode == 3:
            self.ui.lcdNumber.setHexMode()

    def saveValues(self, key=None, value=None):
        if key is not None and value is not None:
            self.settings.setValue(key, value)
        else:
            self.settings.setValue("lcd_value", self.ui.lcdNumber.value())
            self.settings.setValue("dial_value", self.ui.dial.value())
            self.settings.setValue("horizontalSlider_value", self.ui.horizontalSlider.value())
            self.settings.setValue("display_mode", self.ui.comboBox.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


