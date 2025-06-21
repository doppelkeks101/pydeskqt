from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QStyle
)
from classes import AppLauncher


class QuickLaunchBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        quick_launch_web = QPushButton()
        quick_launch_web.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        quick_launch_web.setToolTip("Webbrowser starten")
        quick_launch_web.clicked.connect(lambda: AppLauncher.launch('firefox'))
        layout.addWidget(quick_launch_web)

        quick_launch_files = QPushButton()
        quick_launch_files.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DirHomeIcon))
        quick_launch_files.setToolTip("Dateimanager")
        quick_launch_files.clicked.connect(lambda: AppLauncher.launch('nautilus'))
        layout.addWidget(quick_launch_files)
