from .calculate import calculate
from PyQt6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(500, 500)
        self.setMinimumSize(500, 500)
        self.ui()

    def ui(self):
        self.vbox = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.vbox)
        self.setCentralWidget(self.vbox)
        self.expr = ''

        # result label
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setText(self.expr)
        self.result_label.setStyleSheet("""
                font-size: 24px;
                color: black;
                border: 1px solid black;
                """)
        self.result_label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.result_label, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # nums and oper
        self.btn_layout = QtWidgets.QGridLayout()
        self.main_layout.addLayout(self.btn_layout)

        validChar = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('AC', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        self.buttons = {}
        for text, row, col in validChar:
            btn = QtWidgets.QPushButton(text)
            btn.setStyleSheet("font-size: 18px; padding: 20px;")
            btn.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
            btn.clicked.connect(lambda checked, t=text: self.process(t))
            self.btn_layout.addWidget(btn, row, col)
            self.buttons[text] = btn

    def resizeEvent(self, event):
        new_width = self.width()
        new_height = self.height()

        self.result_label.setFixedSize(int(new_width * 0.9), int(new_height * 0.15))

        new_font_size = max(12, int(new_width * 0.05))
        self.result_label.setStyleSheet(f"""
            font-size: {new_font_size}px;
            color: black;
            border: 1px solid black;
        """)
        super().resizeEvent(event)
    
    def process(self, t: str):
        if t == '=':
            self.expr = calculate(self.expr)
        elif t == 'AC':
            self.expr = ''
        else:
            self.expr += t
        self.result_label.setText(self.expr)

