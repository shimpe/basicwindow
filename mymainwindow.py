from PySide2.QtWidgets import QMainWindow, QAction
from PySide2.QtGui import QIcon, QKeySequence
from ui_mainwindow import Ui_MainWindow



class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonMonitorX.clicked.connect(self.handleMonitorXButton)
        self.ui.buttonMonitorY.clicked.connect(self.handleMonitorYButton)

        self.monitor_x_checked = False
        self.monitor_y_checked = False

        self.ui.graphicsView.click_mouse_position_signal.connect(self.handleClickMousePositionSignal)
        self.ui.graphicsView.move_mouse_position_signal.connect(self.handleMoveMousePositionSignal)

        exit_action = QAction(QIcon(":/images/exit.png"), '&Quit', self)
        exit_action.setShortcuts(QKeySequence.Quit)
        exit_action.setStatusTip('Quit application')
        exit_action.triggered.connect(self.close)
        self.ui.menuFile.addAction(exit_action)

    def handleMonitorXButton(self):
        self.monitor_x_checked = self.ui.buttonMonitorX.isChecked()
        self.ui.statusbar.showMessage(f"{self.monitor_x_checked=}")

    def handleMonitorYButton(self):
        self.monitor_y_checked = self.ui.buttonMonitorY.isChecked()
        self.ui.statusbar.showMessage(f"{self.monitor_x_checked=}")

    def handleClickMousePositionSignal(self, x, y):
        if not self.monitor_y_checked and not self.monitor_x_checked:
            return

        status_msg = "clicked on window on position (relative to window)"
        if self.monitor_x_checked:
            status_msg += f" {x=}"
        if self.monitor_y_checked:
            status_msg += f" {y=}"
        self.ui.statusbar.showMessage(status_msg)

    def handleMoveMousePositionSignal(self, x, y):
        if not self.monitor_y_checked and not self.monitor_x_checked:
            return

        status_msg = "moved mouse to position (relative to window)"
        if self.monitor_x_checked:
            status_msg += f" {x=}"
        if self.monitor_y_checked:
            status_msg += f" {y=}"
        self.ui.statusbar.showMessage(status_msg)





