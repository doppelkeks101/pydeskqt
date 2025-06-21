from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel,
)
from PyQt6.QtCore import QTimer, QDateTime


class ClockWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.clock_label = QLabel()
        self.clock_label.setObjectName("Clock")
        layout.addWidget(self.clock_label)

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)
        self.update_clock()

    def update_clock(self):
        now = QDateTime.currentDateTime()
        self.clock_label.setText(now.toString("dd.MM.yyyy hh:mm:ss"))
