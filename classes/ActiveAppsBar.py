from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton
)


class ActiveAppsBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # In einer echten App würde diese Klasse Methoden haben wie
        # add_app(title), remove_app(title), set_active(title)
        active_app_1 = QPushButton("Aktive App 1")
        active_app_1.setCheckable(True)
        active_app_1.setChecked(True)
        layout.addWidget(active_app_1)

        active_app_2 = QPushButton("Aktive App 2")
        active_app_2.setCheckable(True)
        layout.addWidget(active_app_2)
