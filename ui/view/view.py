from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel, QTextEdit

class View(QMainWindow):
    def __init__(self, app_title: str, view_width: int, view_height: int) -> None:
        super().__init__()
        self.setWindowTitle(app_title)  
        self.setFixedSize(view_width, view_height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        title = QLabel('Что-нибудь надо написать...')
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)
        
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText(' ') 
        layout.addWidget(self.text_input)
        
        self.output_area = QTextEdit()
        self.output_area.setPlaceholderText("//")
        layout.addWidget(self.output_area)
        
        central_widget.setLayout(layout)

        self.show()

    def set_text_input_handler(self, handler):
        pass
