from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QSpinBox, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
import sys
from module import Alarm

class AlarmApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm App")
        self.setFixedSize(250, 150)

        layout = QVBoxLayout()

        title = QLabel("Alarm")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        time_layout = QHBoxLayout()

        self.hour_spin = QSpinBox()
        self.hour_spin.setRange(0, 23)
        self.hour_spin.setPrefix("Hour: ")
        self.hour_spin.setFixedWidth(100)

        self.minute_spin = QSpinBox()
        self.minute_spin.setRange(0, 59)
        self.minute_spin.setPrefix("Min: ")
        self.minute_spin.setFixedWidth(100)

        time_layout.addWidget(self.hour_spin)
        time_layout.addWidget(self.minute_spin)
        layout.addLayout(time_layout)

        button = QPushButton("Set Alarm")
        button.setStyleSheet("background-color: #007BFF; color: white; font-weight: bold;")
        button.clicked.connect(self.set_alarm)
        layout.addWidget(button)

        self.setLayout(layout)

    def set_alarm(self):
        alarm = Alarm()
        hour = self.hour_spin.value()
        minute = self.minute_spin.value()

        user_value = alarm.get_user_time(hour, minute)
        alarm.set_alarm(user_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlarmApp()
    window.show()
    sys.exit(app.exec())

