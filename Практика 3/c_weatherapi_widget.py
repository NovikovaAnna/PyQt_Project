"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как  в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы  (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from PySide6.QtCore import Qt
from a_threads import WeatherHandler


class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather Widget")

        # Создание элементов интерфейса
        self.latitude_label = QLabel("Широта:")
        self.latitude_input = QLineEdit()
        self.longitude_label = QLabel("Долгота:")
        self.longitude_input = QLineEdit()
        self.delay_label = QLabel("Задержка (сек):")
        self.delay_input = QLineEdit()
        self.weather_label = QLabel("Погода:")
        self.weather_output = QTextEdit()
        self.start_stop_button = QPushButton("Старт")

        # Создание компоновщика
        layout = QVBoxLayout()
        layout.addWidget(self.latitude_label)
        layout.addWidget(self.latitude_input)
        layout.addWidget(self.longitude_label)
        layout.addWidget(self.longitude_input)
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.weather_output)
        layout.addWidget(self.start_stop_button)

        self.setLayout(layout)

        # Создание потока WeatherHandler
        self.weather_handler_thread = None

        # Подключение сигналов и слотов
        self.start_stop_button.clicked.connect(self.toggle_weather_thread)

    def toggle_weather_thread(self):
        if self.weather_handler_thread is None or not self.weather_handler_thread.isRunning():
            # Создание и запуск потока WeatherHandler
            lat = self.latitude_input.text()
            lon = self.longitude_input.text()
            delay = float(self.delay_input.text())

            self.weather_handler_thread = WeatherHandler(lat, lon)
            self.weather_handler_thread.setDelay(delay)
            self.weather_handler_thread.weatherDataReceived.connect(self.update_weather_info)
            self.weather_handler_thread.start()

            # Блокировка полей ввода после запуска потока
            self.latitude_input.setEnabled(False)
            self.longitude_input.setEnabled(False)
            self.delay_input.setEnabled(False)
            self.start_stop_button.setText("Стоп")
        else:
            # Остановка потока WeatherHandler
            self.weather_handler_thread.quit()
            self.weather_handler_thread.wait()
            self.weather_handler_thread = None

            # Разблокировка полей ввода после остановки потока
            self.latitude_input.setEnabled(True)
            self.longitude_input.setEnabled(True)
            self.delay_input.setEnabled(True)
            self.start_stop_button.setText("Старт")

    def update_weather_info(self, weather_data):
        # Обновление информации о погоде в поле вывода
        self.weather_output.setPlainText(str(weather_data))



if __name__ == "__main__":
    app = QApplication()

    widget = WeatherWidget()
    widget.show()

    sys.exit(app.exec())

