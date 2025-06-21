class ThemeManager:
    THEMES = {
        "Dark (Standard)": """
            #Taskbar { background-color: #282c34; color: white; }
            QPushButton { background-color: transparent; color: white; border: 1px solid #444; padding: 5px; min-width: 30px; }
            QPushButton:hover { background-color: #3e4451; }
            QPushButton:pressed, QPushButton:checked { background-color: #528bff; border: 1px solid #528bff; }
            QPushButton::menu-indicator { image: none; }
            QMenu { background-color: #282c34; color: white; border: 1px solid #444; }
            QMenu::item:selected { background-color: #528bff; }
            #Clock { padding: 0 10px; }
        """,
        "Light": """
            #Taskbar { background-color: #f0f0f0; color: black; }
            QPushButton { background-color: #e1e1e1; color: black; border: 1px solid #b0b0b0; padding: 5px; min-width: 30px; }
            QPushButton:hover { background-color: #e5f1fb; }
            QPushButton:pressed, QPushButton:checked { background-color: #0078d7; color: white; border: 1px solid #005a9e; }
            QPushButton::menu-indicator { image: none; }
            QMenu { background-color: #f0f0f0; color: black; border: 1px solid #b0b0b0; }
            QMenu::item:selected { background-color: #0078d7; color: white; }
            #Clock { padding: 0 10px; }
        """,
        "Windows 2000 Classic": """
            #Taskbar { background-color: #c0c0c0; color: black; font-family: Tahoma, sans-serif; }
            QPushButton { 
                background-color: #c0c0c0; 
                color: black; 
                border-width: 1px;
                border-style: outset;
                border-color: #f0f0f0 #808080 #808080 #f0f0f0;
                padding: 5px; 
                min-width: 30px;
            }
            QPushButton:hover { /* Kein Hover-Effekt im Classic-Theme */ }
            QPushButton:pressed, QPushButton:checked { 
                border-style: inset;
                border-color: #808080 #f0f0f0 #f0f0f0 #808080;
            }
            QPushButton::menu-indicator { image: none; }
            QMenu { background-color: #c0c0c0; color: black; border: 1px solid #808080; }
            QMenu::item:selected { background-color: #000080; color: white; }
            #Clock { padding: 0 10px; border: 1px inset #808080; }
        """
    }

    @staticmethod
    def get_theme_stylesheet(name):
        return ThemeManager.THEMES.get(name, ThemeManager.THEMES["Dark (Standard)"])

    @staticmethod
    def get_theme_names():
        return list(ThemeManager.THEMES.keys())
