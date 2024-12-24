import sys
import qrcode
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene
from GenecQR import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("QR Generator")

        # Bind button event
        self.ui.btn_Gen.clicked.connect(self.genec)

    def genec(self):
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # receive data
        data = self.ui.lEdit.text()
        map = self.ui.l_Png.text()

        qr.add_data(data)
        qr.make(fit=True)

        # Create and save QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(map)

        # Show QR code on screen
        self.display_image(map)

    def display_image(self, image_path):
        # Create QGraphicsScene
        scene = QGraphicsScene()

        # Upload image
        pixmap = QPixmap(image_path)
        
        # Add pixmap to scene
        scene.addPixmap(pixmap)

        # Assign scene to QGraphicsView
        self.ui.img_View.setScene(scene)
        self.ui.img_View.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)  

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
