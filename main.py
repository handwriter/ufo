from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QKeyEvent
import sys
from PIL.ImageQt import ImageQt
from PIL import Image


class App(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = Image.open("data\\ufo.png")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == 16777235:
            self.label.move(self.label.pos().x(), self.label.pos().y() - 10)
        elif a0.key() == 16777237:
            self.label.move(self.label.pos().x(), self.label.pos().y() + 10)
        elif a0.key() == 16777234:
            self.label.move(self.label.pos().x() - 10, self.label.pos().y())
        elif a0.key() == 16777236:
            self.label.move(self.label.pos().x() + 10, self.label.pos().y())
        if self.label.pos().x() <= -20:
            self.label.move(1006, self.label.pos().y())
        elif self.label.pos().x() >= 1016:
            self.label.move(-10, self.label.pos().y())
        if self.label.pos().y() <= -20:
            self.label.move(self.label.pos().x(), 623)
        elif self.label.pos().y() >= 633:
            self.label.move(self.label.pos().x(), -10)

app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())