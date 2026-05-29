from PySide6 import QtWidgets
from view.PlotWidget_ui import Ui_PlotWidget


class PlotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_PlotWidget()
        self.ui.setupUi(self)

        self.ui.button_tracer.clicked.connect(self.tracer)

    def tracer(self):
        abscisse = self.ui.combo_abscisses.currentText()
        ordonnee = self.ui.combo_ordonnees.currentText()

        self.ui.graph_area.setText(
            f"Graphique demandé :\nAbscisses = {abscisse}\nOrdonnées = {ordonnee}"
        )