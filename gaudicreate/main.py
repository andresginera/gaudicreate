import sys, os
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTabWidget,
    QDialogButtonBox,
    QMenuBar,
    QAction,
    QProgressBar,
    QCheckBox,
    QLineEdit,
)

import genes, objectives, company
from PyQt5.QtCore import Qt, QResource


QResource.registerResource(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources.rrc")
)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)

        self.setWindowTitle("GaudiCreate")
        self.setMinimumSize(900, 600)
        self.setMenuBar(MenuBar())

        wid = QWidget()
        self.setCentralWidget(wid)
        self.main_layout = QVBoxLayout()
        wid.setLayout(self.main_layout)

        self.set_tabwidget()
        execution_layout = QHBoxLayout()

        execution_layout.addWidget(QProgressBar())

        pgaudi_layout = QVBoxLayout()
        self.pgaudi = QCheckBox("Parallelize")
        pgaudi_layout.addWidget(self.pgaudi)
        self.cores = QLineEdit()
        self.cores.setAlignment(Qt.AlignCenter)
        self.cores.setPlaceholderText("Cores")
        self.cores.setMaximumWidth(80)
        self.cores.setEnabled(False)
        pgaudi_layout.addWidget(self.cores)

        self.pgaudi.pressed.connect(self.cores_enabled)

        execution_layout.addLayout(pgaudi_layout)
        execution_layout.addWidget(QPushButton("RUN"))

        self.main_layout.addWidget(self.tabs)
        self.main_layout.addLayout(execution_layout)

    def cores_enabled(self):
        if self.pgaudi.isChecked():
            self.cores.setEnabled(False)
        else:
            self.cores.setEnabled(True)

    def set_tabwidget(self):
        self.tabs = QTabWidget()
        self.genes = genes.GenesTab()
        self.objectives = objectives.ObjectivesTab()
        self.company = company.CompanyTab()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.genes, "GENES")
        self.tabs.addTab(self.objectives, "OBJECTIVES")
        self.tabs.addTab(self.company, "AND COMPANY")


class MenuBar(QMenuBar):
    def __init__(self, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)

        file_menu = self.addMenu("File")
        file_menu.addAction("New")
        file_menu.addSeparator()
        file_menu.addAction("Save")
        file_menu.addAction("Save as...")

        help_menu = self.addAction("Help")

        self.triggered[QAction].connect(self.processtrigger)

    def processtrigger(self, q):
        print(q.text())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
