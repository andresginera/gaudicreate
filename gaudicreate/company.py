import os
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
    QToolButton,
    QSizePolicy,
    QSpinBox,
    QDoubleSpinBox,
    QFileDialog,
    QApplication,
    QCheckBox,
    QRadioButton,
)

from PyQt5.QtCore import (
    Qt,
    QPoint,
    pyqtSignal,
    QObject,
    QPointF,
    QParallelAnimationGroup,
    pyqtSlot,
    QPropertyAnimation,
    QAbstractAnimation,
)
from PyQt5.QtGui import QIcon, QPainter, QColor


class CompanyTab(QScrollArea):
    def __init__(self, *args, **kwargs):
        super(CompanyTab, self).__init__(*args, **kwargs)

        self.setWidgetResizable(True)
        scroll_content = QWidget(self)
        main_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(main_layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        ga = QGroupBox()
        ga.setTitle("Genetical Algorithm")
        main_layout.addWidget(ga)

        self.layout_ga = QVBoxLayout()
        ga_fl = QHBoxLayout()
        population_label = QLabel("Population: ")
        population_edit = QSpinBox()
        population_edit.setMaximum(999)
        population_edit.setMinimum(2)
        population_edit.setValue(100)
        ga_fl.addStretch(1)

        ga_fl.addWidget(population_label)
        ga_fl.addWidget(population_edit)

        ga_fl.addStretch(1)

        generations_label = QLabel("Generations: ")
        generations_edit = QSpinBox()
        generations_edit.setMaximum(999)
        generations_edit.setMinimum(10)
        generations_edit.setValue(100)
        ga_fl.addWidget(generations_label)
        ga_fl.addWidget(generations_edit)

        ga_fl.addStretch(1)

        self.layout_ga.addLayout(ga_fl)

        t = CollapsibleBox(title="Advanced Options")

        genetical_layout = QVBoxLayout()
        one = QHBoxLayout()

        parameters = QGroupBox()
        parameters_layout = QHBoxLayout()
        parameters.setTitle("Parameters")

        mu_label = QLabel("μ: ")
        mu_edit = QDoubleSpinBox()
        mu_edit.setMaximum(1)
        mu_edit.setValue(1)
        mu_edit.setSingleStep(0.05)
        parameters_layout.addStretch(1)
        parameters_layout.addWidget(mu_label)
        parameters_layout.addWidget(mu_edit)
        parameters_layout.addStretch(1)

        lambda_label = QLabel("λ: ")
        lambda_edit = QDoubleSpinBox()
        lambda_edit.setValue(3)
        parameters_layout.addWidget(lambda_label)
        parameters_layout.addWidget(lambda_edit)
        parameters_layout.addStretch(1)
        parameters.setLayout(parameters_layout)
        one.addWidget(parameters)

        crossover = QGroupBox()
        crossover_layout = QHBoxLayout()
        crossover.setTitle("Crossover")

        cx_eta_label = QLabel("Eta: ")
        cx_eta_label.setToolTip(
            "High eta will produce children resembling to their parents, while a small eta will produce solutions much more different."
        )
        cx_eta_edit = QSpinBox()
        cx_eta_edit.setToolTip(
            "High eta will produce children resembling to their parents, while a small eta will produce solutions much more different."
        )
        cx_eta_edit.setValue(5)
        crossover_layout.addStretch(1)
        crossover_layout.addWidget(cx_eta_label)
        crossover_layout.addWidget(cx_eta_edit)
        crossover_layout.addStretch(1)

        cx_pb_label = QLabel("Probability: ")
        cx_pb_edit = QDoubleSpinBox()
        cx_pb_edit.setValue(0.5)
        cx_pb_edit.setMaximum(1)
        cx_pb_edit.setSingleStep(0.05)
        crossover_layout.addWidget(cx_pb_label)
        crossover_layout.addWidget(cx_pb_edit)
        crossover_layout.addStretch(1)
        crossover.setLayout(crossover_layout)
        one.addWidget(crossover)

        genetical_layout.addLayout(one)
        two = QHBoxLayout()

        mutations = QGroupBox()
        mutations_layout = QHBoxLayout()
        mutations.setTitle("Mutations")

        mut_eta_label = QLabel("Eta: ")
        mut_eta_label.setToolTip(
            "High eta will produce children resembling to their parents, while a small eta will produce solutions much more different."
        )
        mut_eta_edit = QSpinBox()
        mut_eta_edit.setToolTip(
            "High eta will produce children resembling to their parents, while a small eta will produce solutions much more different."
        )
        mut_eta_edit.setValue(5)
        mutations_layout.addStretch(1)
        mutations_layout.addWidget(mut_eta_label)
        mutations_layout.addWidget(mut_eta_edit)
        mutations_layout.addStretch(1)

        mut_pb_label = QLabel("Probability: ")
        mut_pb_edit = QDoubleSpinBox()
        mut_pb_edit.setMaximum(1)
        mut_pb_edit.setSingleStep(0.05)
        mut_pb_edit.setValue(0.5)
        mutations_layout.addWidget(mut_pb_label)
        mutations_layout.addWidget(mut_pb_edit)
        mutations_layout.addStretch(1)

        mut_indpb_label = QLabel("Indp probability: ")
        mut_indpb_edit = QDoubleSpinBox()
        mut_indpb_edit.setValue(1.0)
        mut_indpb_edit.setMaximum(1)
        mut_indpb_edit.setSingleStep(0.05)
        mutations_layout.addWidget(mut_indpb_label)
        mutations_layout.addWidget(mut_indpb_edit)
        mutations_layout.addStretch(1)
        mutations.setLayout(mutations_layout)
        two.addWidget(mutations)

        genetical_layout.addLayout(two)

        t.setContentLayout(genetical_layout)
        self.layout_ga.addWidget(t)

        ga.setLayout(self.layout_ga)

        #

        similarity = QGroupBox()
        similarity.setTitle("Similarity")
        similarity_layout = QHBoxLayout()
        molecules = QVBoxLayout()
        label = QLabel("Molecule(s) for the comparison")
        ligand = QRadioButton("Ligand")
        ligand.setAutoExclusive(False)
        protein = QRadioButton("Protein")
        protein.setAutoExclusive(False)
        metal = QRadioButton("Metal")
        metal.setAutoExclusive(False)
        molecules.addWidget(label)
        molecules.addWidget(ligand)
        molecules.addWidget(protein)
        molecules.addWidget(metal)
        similarity_layout.addLayout(molecules)

        threshold_layout = QHBoxLayout()
        threshold_label = QLabel("Threshold: ")
        threshold = QDoubleSpinBox()
        threshold.setSingleStep(0.05)
        threshold_layout.addStretch(1)
        threshold_layout.addWidget(threshold_label)
        threshold_layout.addWidget(threshold)
        threshold_layout.addStretch(1)
        similarity_layout.addLayout(threshold_layout)

        similarity.setLayout(similarity_layout)

        main_layout.addWidget(similarity)

        #

        output = QGroupBox()
        output.setTitle("Output")
        output_layout = QVBoxLayout()

        name = QHBoxLayout()
        name_label = QPushButton("Save as...")
        self.name_edit = QLineEdit()
        self.name_edit.setText(os.getcwd())
        name_label.clicked.connect(self.save_path)
        name.addWidget(name_label)
        name.addWidget(self.name_edit)
        # output_layout.addLayout(name)

        precision_label = QLabel("Precision: ")
        precision_edit = QSpinBox()
        precision_edit.setMinimum(-3)
        precision_edit.setMaximum(6)
        precision_edit.setValue(3)

        name.addWidget(precision_label)
        name.addWidget(precision_edit)
        output_layout.addLayout(name)

        one = QHBoxLayout()
        compress = QCheckBox("Compress")
        compress.setChecked(True)
        verbose = QCheckBox("Verbose")
        verbose.setChecked(True)
        history = QCheckBox("History")
        check = QCheckBox("Check every")
        self.check_edit = QSpinBox()
        self.check_edit.setValue(10)
        self.check_edit.setEnabled(False)
        check.clicked.connect(self.check_edit_connect)
        pareto = QCheckBox("Pareto")
        prompt = QCheckBox("Prompt of exception")

        one.addWidget(compress)
        one.addStretch(1)
        one.addWidget(verbose)
        one.addStretch(1)
        one.addWidget(history)
        one.addStretch(1)
        one.addWidget(check)
        one.addWidget(self.check_edit)
        one.addStretch(1)
        one.addWidget(pareto)
        one.addStretch(1)
        one.addWidget(prompt)
        output_layout.addLayout(one)

        output.setLayout(output_layout)

        main_layout.addWidget(output)

        #

        main_layout.addWidget(QFrame())
        main_layout.addWidget(QFrame())
        main_layout.addWidget(QFrame())
        main_layout.addWidget(QFrame())

        self.setWidget(scroll_content)

    def save_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            QWidget(), "Save As", "", options=options
        )
        if filename:
            self.name_edit.setText(filename)

    def check_edit_connect(self):
        if self.check_edit.isEnabled():
            self.check_edit.setEnabled(False)
        else:
            self.check_edit.setEnabled(True)


class CollapsibleBox(QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.content_area.setFrameShape(QFrame.NoFrame)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self.content_area, b"maximumHeight")
        )

    @pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(Qt.DownArrow if not checked else Qt.RightArrow)
        self.toggle_animation.setDirection(
            QAbstractAnimation.Forward if not checked else QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

