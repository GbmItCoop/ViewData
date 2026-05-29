from PySide6 import QtWidgets
import pyqtgraph as pg
import pyqtgraph.exporters

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

    def get_model_values(self, model, x_col, y_col):
        x_values = []
        y_values = []

        while model.canFetchMore():
            model.fetchMore()

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

        return x_values, y_values

    def tracer(self):
        if self.main_window is None:
            return

        model = self.main_window.database_model.model

        if model is None:
            QtWidgets.QMessageBox.warning(
                self,
                "Aucune table ouverte",
                "Veuillez d'abord ouvrir une table de données."
            )
            return

        x_col = self.ui.combo_abscisses.currentIndex()
        y_col = self.ui.combo_ordonnees.currentIndex()

        if x_col < 0 or y_col < 0:
            QtWidgets.QMessageBox.warning(
                self,
                "Colonnes manquantes",
                "Veuillez sélectionner une colonne pour les abscisses et une colonne pour les ordonnées."
            )
            return

        x_values, y_values = self.get_model_values(model, x_col, y_col)

        if len(x_values) == 0 or len(y_values) == 0:
            QtWidgets.QMessageBox.warning(
                self,
                "Données non numériques",
                "Impossible de tracer le graphe : les colonnes sélectionnées ne contiennent pas de valeurs numériques exploitables."
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

        x_name = self.ui.combo_abscisses.currentText()
        y_name = self.ui.combo_ordonnees.currentText()

        self.ui.graph_area.setLabel("bottom", x_name)
        self.ui.graph_area.setLabel("left", y_name)
        self.ui.graph_area.setTitle(f"{y_name} en fonction de {x_name}")

    def export_png(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Exporter le graphe en PNG",
            "graphe.png",
            "Images PNG (*.png)"
        )

        if not file_path:
            return

        if not file_path.endswith(".png"):
            file_path += ".png"

        exporter = pg.exporters.ImageExporter(
            self.ui.graph_area.plotItem
        )
        exporter.export(file_path)

        QtWidgets.QMessageBox.information(
            self,
            "Export terminé",
            f"Le graphe a été exporté ici :\n{file_path}"
        )