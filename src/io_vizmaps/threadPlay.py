import logging
import threading
import time
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
)


def openWindow():
    app = QApplication([])

    window = MainWindow()
    window.setWindowTitle("A little test of Qt5")
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)

    window.show()

    sys.exit(app.exec())


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

    def thread_function(name):
        logging.info("Thread %s: starting", name)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    # openWindow()
    if 1:
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

        logging.info("Main    : before creating thread")
        x = threading.Thread(target=openWindow, args=())
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")
