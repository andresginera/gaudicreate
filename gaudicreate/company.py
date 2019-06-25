from PyQt5.QtWidgets import (
    QScrollArea,
    QWidget,
    QHBoxLayout,
    QScrollArea,
    QVBoxLayout,
    QPushButton,
    QGroupBox,
    QGridLayout,
    QLineEdit,
    QLabel,
    QFrame,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class CompanyTab(QWidget):
    def __init__(self, *args, **kwargs):
        super(CompanyTab, self).__init__(*args, **kwargs)

        main_layout = QVBoxLayout()

        ga = QGroupBox()
        ga.setTitle("Genetical Algorithm")
        main_layout.addWidget(ga)

        self.layout_ga = QVBoxLayout()
        ga_fl = QHBoxLayout()
        population_label = QLabel("Population: ")
        population_edit = QLineEdit()
        ga_fl.addWidget(population_label)
        ga_fl.addWidget(population_edit)

        ga_fl.addStretch(1)

        generations_label = QLabel("Generations: ")
        generations_edit = QLineEdit()
        ga_fl.addWidget(generations_label)
        ga_fl.addWidget(generations_edit)

        ga_fl.addStretch(1)

        self.layout_ga.addLayout(ga_fl)

        self.more_options_ga = QPushButton("  Advanced options")
        self.more_options_ga.setIcon(QIcon(":/icons/add.png"))
        self.more_options_ga.setMaximumWidth(180)
        self.more_options_ga.clicked.connect(self.more_ga)
        self.layout_ga.addWidget(self.more_options_ga)

        self.advanced_options = QFrame()
        ga_sl = QGridLayout()
        self.advanced_options.setLayout(ga_sl)
        self.layout_ga.addWidget(self.advanced_options)

        ga.setLayout(self.layout_ga)

        similarity = QGroupBox()
        similarity.setTitle("Similarity")
        main_layout.addWidget(similarity)

        output = QGroupBox()
        output.setTitle("Output")
        main_layout.addWidget(output)

        self.setLayout(main_layout)

    def more_ga(self):
        if self.more_options_ga.text() == "  Advanced options":
            self.more_options_ga.setIcon(QIcon(":/icons/less.png"))
            self.more_options_ga.setText("  Less")
            self.more_options_ga.setMaximumWidth(80)

            self.advanced_options.show()

        else:
            self.more_options_ga.setIcon(QIcon(":/icons/add.png"))
            self.more_options_ga.setText("  Advanced options")
            self.more_options_ga.setMaximumWidth(180)
            self.advanced_options.hide()

