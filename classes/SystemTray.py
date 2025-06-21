from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton,  QStyle
)
from PyQt6.QtCore import QSize


class SystemTray(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        tray_icon_1 = QPushButton()
        tray_icon_1.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaVolume))
        tray_icon_1.setFixedSize(QSize(24, 24))
        layout.addWidget(tray_icon_1)

        tray_icon_2 = QPushButton()
        tray_icon_2.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DriveNetIcon))
        tray_icon_2.setFixedSize(QSize(24, 24))
        layout.addWidget(tray_icon_2)
