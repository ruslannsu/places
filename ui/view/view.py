from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel, QTextEdit

class View(QMainWindow):
    def __init__(self, app_title: str, view_width: int, view_height: int) -> None:
        super().__init__()
        self.setWindowTitle(app_title)  
        self.setFixedSize(view_width, view_height)

        _central_widget = QWidget()
        self.setCentralWidget(_central_widget)
        
        _layout = QVBoxLayout()
        
        title = QLabel('Что-нибудь надо написать...')
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        _layout.addWidget(title)
        
        self._text_input = QLineEdit()
        self._text_input.setPlaceholderText('Сюда нужно что-то написать') 
        _layout.addWidget(self._text_input)

        self._text_button = QPushButton()
        self._text_button.setText('Искать')
        _layout.addWidget(self._text_button)
        
        self.output_area = QTextEdit()
        self.output_area.setPlaceholderText("......... ")
        _layout.addWidget(self.output_area)
        
        _central_widget.setLayout(_layout)

        self.show()

    def set_text_button_handler(self, handler) -> None:
        self._text_button.clicked.connect(handler)

    def get_text_input(self) -> str:
        return self._text_input.text()
    
    def get_text_input_placeholder(self):
        return self._text_input.placeholderText()
    
    def set_text_placeholder(self, text: str) -> None:
        self._text_input.clear()
        self._text_input.setPlaceholderText(text)
        
    def set_area_text(self, text: str):
        self.output_area.setText(text)    