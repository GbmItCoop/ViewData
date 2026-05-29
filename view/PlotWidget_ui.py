from PySide6 import QtCore, QtWidgets


class Ui_PlotWidget(object):
    def setupUi(self, PlotWidget):
        PlotWidget.setObjectName("PlotWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(PlotWidget)

        self.leftPanel = QtWidgets.QWidget(PlotWidget)
        self.leftPanel.setMaximumWidth(180)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftPanel)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.label_abscisses = QtWidgets.QLabel("Abscisses")
        self.combo_abscisses = QtWidgets.QComboBox()
        self.combo_abscisses.addItems(["A", "B", "C"])

        self.label_ordonnees = QtWidgets.QLabel("Ordonnées")
        self.combo_ordonnees = QtWidgets.QComboBox()
        self.combo_ordonnees.addItems(["A", "B", "C"])

        self.button_tracer = QtWidgets.QPushButton("Tracer")

        self.verticalLayout.addWidget(self.label_abscisses)
        self.verticalLayout.addWidget(self.combo_abscisses)
        self.verticalLayout.addSpacing(15)

        self.verticalLayout.addWidget(self.label_ordonnees)
        self.verticalLayout.addWidget(self.combo_ordonnees)
        self.verticalLayout.addSpacing(15)

        self.verticalLayout.addWidget(self.button_tracer)
        self.verticalLayout.addStretch()

        self.graph_area = QtWidgets.QLabel("Graphique")
        self.graph_area.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.graph_area.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid black;
                font-size: 20px;
            }
        """)

        self.horizontalLayout.addWidget(self.leftPanel)
        self.horizontalLayout.addWidget(self.graph_area)

        QtCore.QMetaObject.connectSlotsByName(PlotWidget)