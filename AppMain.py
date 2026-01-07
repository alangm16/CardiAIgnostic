import sys
import time
from PyQt6 import QtCore, QtWidgets
from loading_screen import Ui_loading_screen
from main import Ui_CuadroMain

class LoadingScreen(QtWidgets.QWidget, Ui_loading_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progress_value = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Actualiza cada 50 ms

    def update_progress(self):
        self.progress_value += 2
        self.progressBar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.open_main_window()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class MainWindow(QtWidgets.QWidget, Ui_CuadroMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Mostrar la pantalla de carga
    loading_screen = LoadingScreen()
    loading_screen.show()
    
    sys.exit(app.exec())