import sys
from PyQt5 import QtGui, QtCore


class DeleteButtonExample(QtGui.QWidget):
    def __init__(self):
        super(DeleteButtonExample, self).__init__()

        delete_gb = QtGui.QGroupBox("QGroupBox with Delete Button")
        group_box_vbl = QtGui.QVBoxLayout()
        group_box_vbl.setAlignment(QtCore.Qt.AlignTop)
        group_box_vbl.addSpacing(-14)
        delete_button_hbl = QtGui.QHBoxLayout()
        delete_button_cb = QtGui.QCheckBox()
        delete_button_cb.clicked.connect(self.delete_event)
        delete_button_cb.setStyleSheet(
            "QCheckBox::indicator:hover {image: url(del_btn_hover.png);}"
            "QCheckBox::indicator:!hover {image: url(del_btn_no_hover.png);}"
        )
        delete_button_hbl.setAlignment(QtCore.Qt.AlignRight)
        delete_button_hbl.addWidget(delete_button_cb)
        delete_button_hbl.addSpacing(-13)
        group_box_vbl.addLayout(delete_button_hbl)
        delete_gb.setLayout(group_box_vbl)

        window_vbl = QtGui.QVBoxLayout()
        window_vbl.addWidget(delete_gb)
        self.setLayout(window_vbl)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QGroupBox with Delete Button")
        self.show()

    # @QtCore.Slot()
    def delete_event(self):
        msg = "Define the code to delete the QGroupBox here!"
        QtGui.QMessageBox().information(self, "Trying to delete the QGroupBox", msg)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    example = DeleteButtonExample()
    sys.exit(app.exec_())
