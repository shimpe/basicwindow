from PySide2 import QtWidgets
from PySide2.QtCore import Signal
from PySide2.QtGui import QMouseEvent


class MyGraphicsView(QtWidgets.QGraphicsView):

    click_mouse_position_signal = Signal(float, float)
    move_mouse_position_signal = Signal(float, float)

    def __init__(self, *args):
        super(MyGraphicsView, self).__init__(*args)
        self.setMouseTracking(True)

    def mousePressEvent(self, event) -> None:
        p = event.pos()  # relative to widget
        gp = self.mapToGlobal(p)  # relative to screen
        rw = self.window().mapFromGlobal(gp)  # relative to window
        self.click_mouse_position_signal.emit(rw.x(), rw.y())
        super(MyGraphicsView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event:QMouseEvent) -> None:
        p = event.pos()  # relative to widget
        gp = self.mapToGlobal(p)  # relative to screen
        rw = self.window().mapFromGlobal(gp)  # relative to window
        self.move_mouse_position_signal.emit(rw.x(), rw.y())
        super(MyGraphicsView, self).mousePressEvent(event)
