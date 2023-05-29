from PySide6 import QtWidgets, QtCore


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #self.setFixedSize(250, 150)
        #size = QtCore.QSize(250, 150)
        # self.setFixedSize(size)
    def initUi(self)-> None
    """
    Доинициализация UI
    :return None 
    """
        self.setWindowTitle("Моя первая программа")
        self.setFixedSize(450, 200)
    def initSignals(self)-> None
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win_1 = MyFirstWindow()
    win_1.show()

    app.exec()