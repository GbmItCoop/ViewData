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
            f"Graphe\n\nAbscisses : {abscisse}\nOrdonnées : {ordonnee}"
        )

    def export_png(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Exporter le graphe en PNG",
            "graphe.png",
            "Image PNG (*.png)"
        )

        if file_path:
            QtWidgets.QMessageBox.information(
                self,
                "Export PNG",
                f"Graphe exporté vers :\n{file_path}"
            )