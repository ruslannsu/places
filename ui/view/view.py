from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow





class View(QMainWindow):
    def __init__(self, view_width: int, view_height: int) -> None:
        super().__init__()
        self.setWindowTitle("PLACES")
        self.setFixedSize(view_width, view_height)
        self.show()




