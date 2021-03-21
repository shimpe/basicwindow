import sys
from PySide2.QtWidgets import QApplication
from mymainwindow import MyMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec_())
