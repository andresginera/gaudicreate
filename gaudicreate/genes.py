from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QHBoxLayout,
    QScrollArea,
    QVBoxLayout,
    QPushButton,
)


class GenesTab(QWidget):
    def __init__(self, *args, **kwargs):
        super(GenesTab, self).__init__(*args, **kwargs)

        main_layout = QHBoxLayout()
        scroll = QScrollArea()

        but_layout = QVBoxLayout()
        molecule = QPushButton("Molecule")
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

        self.setLayout(main_layout)
