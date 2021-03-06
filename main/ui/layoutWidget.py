from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLayout)

from ui.createPersonaWidget import CreatePersonaWidget
from ui.dnaWidget import DnaWidget
from ui.enrollPersonaWidget import EnrollPersonaWidget
from schoolWidget import SchoolWidget


class LayoutWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        school = SchoolWidget()
        school.resize(school.sizeHint())

        dna = DnaWidget()
        dna.resize(dna.sizeHint())

        createPersona = CreatePersonaWidget(dna.get_dna(), school.get_school())
        createPersona.resize(createPersona.sizeHint())

        enrollPersona = EnrollPersonaWidget()
        enrollPersona.resize(enrollPersona.sizeHint())

        vbox = QVBoxLayout(self)
        vbox.addWidget(school)
        vbox.addWidget(dna)
        vbox.addWidget(createPersona)
        vbox.addWidget(enrollPersona)
        vbox.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(vbox)

