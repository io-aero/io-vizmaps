import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
)


class MainWindow(QWidget):
    def __init__(self):
        # call super class constructor
        super(MainWindow, self).__init__()
        # build the objects one by one
        layout = QVBoxLayout(self)
        self.pb_load = QPushButton("Load")
        self.pb_clear = QPushButton("Clear")
        self.edit = QTextEdit()
        layout.addWidget(self.edit)
        layout.addWidget(self.pb_load)
        layout.addWidget(self.pb_clear)
        # connect the callbacks to the push-buttons
        self.pb_load.clicked.connect(self.callback_pb_load)
        self.pb_clear.clicked.connect(self.callback_pb_clear)

    def callback_pb_load(self):
        self.edit.append("hello world")

    def callback_pb_clear(self):
        self.edit.clear()


# def mythread():
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     app.exec_()


# def show():
#     import threading

#     t = threading.Thread(target=mythread)
#     t.daemon = True
#     t.start()


# if __name__ == "__main__":
if QApplication.instance() is None:
    app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.callback_pb_load()

# sys.exit(app.exec())
