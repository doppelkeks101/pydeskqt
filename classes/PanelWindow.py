from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout
)

from PyQt6.QtCore import Qt
from classes.StartMenu import StartMenu
from classes.QuickLaunchBar import QuickLaunchBar
from classes.ActiveAppsBar import ActiveAppsBar
from classes.SystemTray import SystemTray
from classes.ClockWidget import ClockWidget
from classes.ThemeManager import ThemeManager


class PanelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setObjectName("Taskbar")
        self.setGeometry(0, 900, 1920, 40)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(5, 0, 5, 0)
        layout.setSpacing(5)

        # StartMenu erstellen und Signal mit Slot verbinden
        start_menu = StartMenu(self)
        start_menu.theme_changed.connect(self.apply_theme)  # HIER DIE VERBINDUNG

        layout.addWidget(start_menu)
        layout.addSpacing(10)
        layout.addWidget(QuickLaunchBar(self))
        layout.addStretch(1)
        layout.addWidget(ActiveAppsBar(self))
        layout.addStretch(1)
        layout.addWidget(SystemTray(self))
        layout.addSpacing(10)
        layout.addWidget(ClockWidget(self))

    # NEU: Der Slot, der das Theme anwendet
    def apply_theme(self, name):
        print(f"Theme '{name}' wird angewendet...")
        stylesheet = ThemeManager.get_theme_stylesheet(name)
        QApplication.instance().setStyleSheet(stylesheet)

    def quitApp(self):
        QApplication.quit()
