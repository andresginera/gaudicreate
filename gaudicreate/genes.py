from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QHBoxLayout,
    QScrollArea,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QLineEdit,
    QFileDialog,
    QCheckBox,
    QDockWidget,
    QGroupBox,
)
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from company import CollapsibleBox
import os


class GenesTab(QWidget):
    def __init__(self, *args, **kwargs):
        super(GenesTab, self).__init__(*args, **kwargs)

        main_layout = QHBoxLayout()
        scroll = QScrollArea()
        scroll_content = QWidget(scroll)
        scroll.setWidgetResizable(True)
        self.scroll_layout = QVBoxLayout(scroll_content)

        but_layout = QVBoxLayout()
        molecule = QPushButton("Molecule")
        molecule.clicked.connect(self.add_molecule)
        mutamer = QPushButton("Mutamer")
        normalmodes = QPushButton("Normal Modes")
        rotamers = QPushButton("Rotamers")
        search = QPushButton("Search")
        torsion = QPushButton("Torsion")
        trajectory = QPushButton("Trajectory")

        but_layout.addWidget(molecule)
        but_layout.addWidget(mutamer)
        but_layout.addWidget(normalmodes)
        but_layout.addWidget(rotamers)
        but_layout.addWidget(search)
        but_layout.addWidget(torsion)
        but_layout.addWidget(trajectory)

        main_layout.addWidget(scroll)
        main_layout.addLayout(but_layout)

        scroll.setWidget(scroll_content)

        self.setLayout(main_layout)

    def add_molecule(self):
        self.scroll_layout.addWidget(Molecule())
        self.scroll_layout.setAlignment(Qt.AlignTop)


class Molecule(QGroupBox):
    def __init__(self, *args, **kwargs):
        super(Molecule, self).__init__(*args, **kwargs)

        self.setTitle("Molecule")

        group_box_vbl = QVBoxLayout()
        group_box_vbl.setAlignment(Qt.AlignTop)
        group_box_vbl.addSpacing(-16)
        delete_button_hbl = QHBoxLayout()
        delete_button_cb = QCheckBox()
        delete_button_cb.setFixedSize(15, 15)
        delete_button_cb.setIcon(
            QtGui.QIcon(
                "/home/andres/practicas/gaudicreate/gaudicreate/icons/close.png"
            )
        )
        # delete_button_cb.setStyleSheet("border:0px")
        delete_button_cb.clicked.connect(self.delete_event)
        delete_button_hbl.setAlignment(Qt.AlignRight)
        delete_button_hbl.addWidget(delete_button_cb)
        delete_button_hbl.addSpacing(-13)
        group_box_vbl.addLayout(delete_button_hbl)

        layout = QVBoxLayout()
        layout.addLayout(group_box_vbl)
        path_layout = QHBoxLayout()
        path_label = QPushButton("Path...")
        self.path_edit = QLineEdit()
        path_label.clicked.connect(self.save_path)
        name = QLineEdit()
        name.setPlaceholderText("Name")
        name.setFixedWidth(100)
        name.setAlignment(Qt.AlignCenter)
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(name)
        layout.addLayout(path_layout)

        adv = CollapsibleBox("Advanced options")
        adv_layout = QHBoxLayout()
        adv_layout.addStretch(1)
        hydrogens = QCheckBox("Hydrogens")
        adv_layout.addWidget(hydrogens)
        adv_layout.addStretch(1)
        pdbfix = QCheckBox("PDBFix")
        adv_layout.addWidget(pdbfix)
        adv_layout.addStretch(1)
        adv.setContentLayout(adv_layout)

        layout.addWidget(adv)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

    def save_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            QWidget(), "Save As", "", options=options
        )
        if filename:
            self.path_edit.setText(filename)

    def delete_event(self):
        self.close()

