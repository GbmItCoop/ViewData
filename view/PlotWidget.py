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
        x_col = self.ui.combo_abscisses.currentIndex()
        y_col = self.ui.combo_ordonnees.currentIndex()

        table = self.main_window.data_widget.table

        x_values = []
        y_values = []

        for row in range(table.rowCount()):
            item_x = table.item(row, x_col)
            item_y = table.item(row, y_col)

            if item_x is None or item_y is None:
                continue

            try:
                x_values.append(float(item_x.text()))
                y_values.append(float(item_y.text()))
            except ValueError:
                continue

        if not x_values or not y_values:
            QtWidgets.QMessageBox.warning(
                self,
                "Erreur",
                "Impossible de tracer le graphe : les colonnes sélectionnées ne contiennent pas de données numériques."
            )
            return

        self.ui.graph_area.clear()

        self.ui.graph_area.plot(
            x_values,
            y_values,
            pen=pg.mkPen(width=2),
            symbol="o",
            symbolSize=8
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