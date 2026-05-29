from PySide6 import QtWidgets
import pyqtgraph as pg

from view.PlotWidget_ui import Ui_PlotWidget


class PlotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_window = parent

        self.ui = Ui_PlotWidget()
        self.ui.setupUi(self)

        self.ui.button_tracer.clicked.connect(self.tracer)

    def update_columns(self, columns):
        self.ui.combo_abscisses.clear()
        self.ui.combo_ordonnees.clear()

        self.ui.combo_abscisses.addItems(columns)
        self.ui.combo_ordonnees.addItems(columns)

        if len(columns) >= 2:
            self.ui.combo_abscisses.setCurrentIndex(0)
            self.ui.combo_ordonnees.setCurrentIndex(1)

    def tracer(self):
        if self.main_window is None:
            return

        model = self.main_window.database_model.model

        if model is None:
            QtWidgets.QMessageBox.warning(
                self,
                "Aucune donnée",
                "Veuillez d'abord ouvrir une table de données."
            )
            return

        x_col = self.ui.combo_abscisses.currentIndex()
        y_col = self.ui.combo_ordonnees.currentIndex()

        if x_col < 0 or y_col < 0:
            QtWidgets.QMessageBox.warning(
                self,
                "Colonnes manquantes",
                "Veuillez sélectionner une abscisse et une ordonnée."
            )
            return

        x_values = []
        y_values = []

        for row in range(model.rowCount()):
            x_index = model.index(row, x_col)
            y_index = model.index(row, y_col)

            x_data = model.data(x_index)
            y_data = model.data(y_index)

            try:
                x_values.append(float(x_data))
                y_values.append(float(y_data))
            except (TypeError, ValueError):
                continue

        if not x_values or not y_values:
            QtWidgets.QMessageBox.warning(
                self,
                "Données non numériques",
                "Impossible de tracer le graphe : les colonnes sélectionnées ne contiennent pas de données numériques."
            )
            return

        self.ui.graph_area.clear()

        self.ui.graph_area.plot(
            x_values,
            y_values,
            pen=pg.mkPen(width=2),
            symbol="o",
            symbolSize=7
        )

        self.ui.graph_area.setLabel(
            "bottom",
            self.ui.combo_abscisses.currentText()
        )

        self.ui.graph_area.setLabel(
            "left",
            self.ui.combo_ordonnees.currentText()
        )

        self.ui.graph_area.setTitle(
            f"{self.ui.combo_ordonnees.currentText()} en fonction de {self.ui.combo_abscisses.currentText()}"
        )

    def export_png(self):
        QtWidgets.QMessageBox.information(
            self,
            "Export PNG",
            "L’export PNG sera traité dans l’étape suivante."
        )