from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QHBoxLayout,
    QScrollArea,
    QVBoxLayout,
    QPushButton,
)


class ObjectivesTab(QWidget):
    def __init__(self, *args, **kwargs):
        super(ObjectivesTab, self).__init__(*args, **kwargs)

        main_layout = QHBoxLayout()
        scroll = QScrollArea()

        but_layout = QVBoxLayout()
        angle = QPushButton("Angle")
        contacts = QPushButton("Contacs")
        coordination = QPushButton("Coordination")
        distance = QPushButton("Distance")
        dsx = QPushButton("Dsx")
        energy = QPushButton("Energy")
        gold = QPushButton("Gold")
        hbonds = QPushButton("Hydrogen Bonds")
        inertia = QPushButton("Inertia")
        ligscore = QPushButton("Lig Score")
        nwchem = QPushButton("Nwchem")
        solvation = QPushButton("Solvation")
        vina = QPushButton("Vina")
        volumen = QPushButton("Volumen")

        but_layout.addWidget(angle)
        but_layout.addWidget(contacts)
        but_layout.addWidget(coordination)
        but_layout.addWidget(distance)
        but_layout.addWidget(dsx)
        but_layout.addWidget(energy)
        but_layout.addWidget(gold)
        but_layout.addWidget(hbonds)
        but_layout.addWidget(inertia)
        but_layout.addWidget(ligscore)
        but_layout.addWidget(nwchem)
        but_layout.addWidget(solvation)
        but_layout.addWidget(vina)
        but_layout.addWidget(volumen)

        main_layout.addWidget(scroll)
        main_layout.addLayout(but_layout)

        self.setLayout(main_layout)
