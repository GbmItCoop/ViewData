from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
import pyqtgraph.exporters

from view.PlotWidget_ui import Ui_PlotWidget


class PlotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_window = parent
        self.has_graph = False

        self.ui = Ui_PlotWidget()
        self.ui.setupUi(self)

        self.ui.button_tracer.clicked.connect(self.tracer)

    def update_columns(self, columns):
        self.ui.combo_abscisses.clear()
        self.ui.combo_ordonnees.clear()

        self.ui.combo_abscisses.addItems(columns)
        self.ui.combo_ordonnees.addItems(columns)

        self.has_graph = False
        self.ui.graph_area.clear()

        if len(columns) >= 2:
            self.ui.combo_abscisses.setCurrentIndex(0)
            self.ui.combo_ordonnees.setCurrentIndex(1)

    def get_numeric_columns(self, model):
        numeric_columns = []

        while model.canFetchMore():
            model.fetchMore()

        for col in range(model.columnCount()):
            numeric_count = 0
            checked_count = 0

            for row in range(model.rowCount()):
                value = model.data(model.index(row, col))

                if value in (None, ""):
                    continue

                checked_count += 1

                try:
                    float(value)
                    numeric_count += 1
                except (TypeError, ValueError):
                    pass

            if checked_count > 0 and numeric_count == checked_count:
                column_name = model.headerData(col, QtCore.Qt.Orientation.Horizontal)
                numeric_columns.append(str(column_name))

        return numeric_columns

    def get_model_values(self, model, x_col, y_col):
        x_values = []
        y_values = []
        ignored_rows = 0

        while model.canFetchMore():
            model.fetchMore()

        for row in range(model.rowCount()):
            x_data = model.data(model.index(row, x_col))
            y_data = model.data(model.index(row, y_col))

            try:
                x_values.append(float(x_data))
                y_values.append(float(y_data))
            except (TypeError, ValueError):
                ignored_rows += 1

        return x_values, y_values, ignored_rows

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

        x_values, y_values, ignored_rows = self.get_model_values(model, x_col, y_col)

        if len(x_values) == 0 or len(y_values) == 0:
            QtWidgets.QMessageBox.warning(
                self,
                "Aucune donnée numérique",
                "Impossible de tracer le graphe : les colonnes sélectionnées ne contiennent aucune valeur numérique exploitable."
            )
            self.has_graph = False
            return

        if len(x_values) < 2:
            QtWidgets.QMessageBox.warning(
                self,
                "Données insuffisantes",
                "Il faut au moins deux points numériques pour tracer un graphe."
            )
            self.has_graph = False
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

        self.has_graph = True

        if ignored_rows > 0:
            QtWidgets.QMessageBox.information(
                self,
                "Lignes ignorées",
                f"{ignored_rows} ligne(s) ont été ignorées car elles contiennent des valeurs non numériques."
            )

    def export_png(self):
        if not self.has_graph:
            QtWidgets.QMessageBox.warning(
                self,
                "Aucun graphe",
                "Veuillez d'abord tracer un graphe avant de l'exporter."
            )
            return

        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Exporter le graphe en PNG",
            "graphe.png",
            "Images PNG (*.png)"
        )

        if not file_path:
            return

        if not file_path.lower().endswith(".png"):
            file_path += ".png"

        try:
            exporter = pg.exporters.ImageExporter(self.ui.graph_area.plotItem)
            exporter.export(file_path)

            QtWidgets.QMessageBox.information(
                self,
                "Export terminé",
                f"Le graphe a été exporté ici :\n{file_path}"
            )

        except Exception as error:
            QtWidgets.QMessageBox.critical(
                self,
                "Erreur d'export",
                f"Impossible d'exporter le graphe.\n\nDétail : {error}"
            )