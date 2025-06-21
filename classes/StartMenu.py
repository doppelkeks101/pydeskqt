from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QPushButton, QMenu, QStyle
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import pyqtSignal
from classes.AppLauncher import AppLauncher
from classes.ThemeManager import ThemeManager


class StartMenu(QWidget):
    # Signal, das den Namen des gewählten Themes sendet
    theme_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        start_button = QPushButton("Start")
        start_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))

        # Hauptmenü
        start_menu = QMenu()

        # ... (Anwendungs-Actions bleiben gleich)
        action_terminal = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon), "Terminal", self)
        action_terminal.triggered.connect(lambda: AppLauncher.launch('x-terminal-emulator'))
        action_files = QAction(self.style().standardIcon(QStyle.StandardPixmap.SP_DirIcon), "Dateimanager", self)
        action_files.triggered.connect(lambda: AppLauncher.launch('nautilus'))
        start_menu.addAction(action_terminal)
        start_menu.addAction(action_files)

        start_menu.addSeparator()

        # NEU: Untermenü für Themes
        theme_menu = QMenu("Erscheinungsbild", self)
        for theme_name in ThemeManager.get_theme_names():
            action = QAction(theme_name, self)
            # Wichtig: Lambda verwenden, um den korrekten Namen zu binden
            action.triggered.connect(lambda checked=False, name=theme_name: self.theme_changed.emit(name))
            theme_menu.addAction(action)

        start_menu.addMenu(theme_menu)  # Untermenü hinzufügen

        start_menu.addSeparator()

        # Beenden-Action
        action_exit = QAction("Panel beenden", self)
        if self.parent() and isinstance(self.parent().parent(), QMainWindow):
            action_exit.triggered.connect(self.parent().parent().close)
        start_menu.addAction(action_exit)

        start_button.setMenu(start_menu)
        layout.addWidget(start_button)
