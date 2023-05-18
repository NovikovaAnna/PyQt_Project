"""
Реализовать окно, которое будет   объединять в себе сразу два предыдущих виджета
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from b_systeminfo_widget import SystemInfoWidget
from c_weatherapi_widget import WeatherWidget


class CombinedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combined Widget")

        b_systeminfo_widget = SystemInfoWidget()
        c_weatherapi_widget = WeatherWidget()

        layout = QVBoxLayout()
        layout.addWidget(b_systeminfo_widget)
        layout.addWidget(c_weatherapi_widget)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        combined_widget = CombinedWidget()
        self.setCentralWidget(combined_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
