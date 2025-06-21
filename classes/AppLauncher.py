from PyQt6.QtCore import QProcess


class AppLauncher:
    @staticmethod
    def launch(program):
        process = QProcess()
        process.startDetached(program)
        print(f"Versuche, '{program}' zu starten...")
