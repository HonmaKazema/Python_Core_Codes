# Create background image in PyQt6 window.
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap, QPalette, QBrush

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # core code
        pixmap = QPixmap(url)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
