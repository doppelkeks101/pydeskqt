import sys
from PyQt6.QtWidgets import QApplication
from classes.PanelWindow import PanelWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PanelWindow()

    # Standard-Theme beim Start anwenden
    window.apply_theme("Dark (Standard)")

    window.show()
    sys.exit(app.exec())
