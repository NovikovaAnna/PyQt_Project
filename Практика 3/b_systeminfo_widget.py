"""
Реализовать виджет,  который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации  о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt
from a_threads import SystemInfo


class SystemInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Info Widget")

        # Создание элементов интерфейса
        self.delay_label = QLabel("Задержка (сек):")
        self.delay_input = QLineEdit()
        self.cpu_label = QLabel("Загрузка CPU:")
        self.cpu_value = QLabel()
        self.ram_label = QLabel("Загрузка RAM:")
        self.ram_value = QLabel()

        # Создание компоновщика
        layout = QVBoxLayout()
        layout.addWidget(self.delay_label)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_value)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_value)

        self.setLayout(layout)

        # Создание и запуск потока SystemInfo
        self.system_info_thread = SystemInfo()
        self.system_info_thread.systemInfoReceived.connect(self.update_system_info)
        self.system_info_thread.start()

        # Подключение сигнала изменения текста в поле ввода времени задержки
        self.delay_input.textChanged.connect(self.set_delay)

    def update_system_info(self, system_info):
        cpu_load, ram_load = system_info
        self.cpu_value.setText(f"{cpu_load}%")
        self.ram_value.setText(f"{ram_load}%")

    def set_delay(self, delay):
        try:
            delay = float(delay)
            self.system_info_thread.delay = delay
        except ValueError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = SystemInfoWidget()
    widget.show()

    sys.exit(app.exec())


