from PySide6 import QtWidgets
from view.about_table_dialog import AboutTableDialog
from view.open_table_dialog import OpenTableDialog
from view.data_widget import DataWidget
from view.PlotWidget import PlotWidget
from view.actions import create_actions
from view.menus import create_menus
from view.toolbar import create_toolbar
from model.sql_model import DatabaseModel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application de visualisation de données")
        self.resize(900, 550)

        self.database_model = DatabaseModel()

        create_actions(self)
        create_menus(self)
        create_toolbar(self)

        self.create_central_widget()
        self.statusBar().showMessage("Prêt")

    def create_central_widget(self):
        self.tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabs)

        self.data_widget = DataWidget()
        self.plot_widget = PlotWidget(self)

        self.tabs.addTab(self.data_widget, "Données")
        self.tabs.addTab(self.plot_widget, "Graphes")

        self.data_widget.columns_changed.connect(
            self.plot_widget.update_columns
        )

    def open_table(self):
        dialog = OpenTableDialog(self)

        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            success = self.database_model.open_database(
                dialog.database_path,
                dialog.table_name
            )

            if not success:
                QtWidgets.QMessageBox.critical(
                    self,
                    "Erreur",
                    "Impossible d'ouvrir la base de données."
                )
                return

            self.data_widget.set_model(self.database_model.model)
            
            about_dialog = AboutTableDialog(
                dialog.database_path,
                dialog.table_name,
                self.database_model.model,
                self
            )

            about_dialog.exec()

            self.plot_widget.update_columns(
                self.data_widget.get_columns()
            )

            self.tabs.setCurrentWidget(self.data_widget)

            self.statusBar().showMessage(
                f"Table ouverte : {dialog.table_name} depuis {dialog.database_path}"
            )

    def save_changes(self):
        if self.database_model.model is None:
            QtWidgets.QMessageBox.warning(
                self,
                "Aucune table",
                "Aucune table n'est ouverte."
            )
            return

        if self.database_model.submit():
            QtWidgets.QMessageBox.information(
                self,
                "Enregistrement",
                "Les modifications ont été enregistrées."
            )
            self.statusBar().showMessage("Modifications enregistrées")
        else:
            QtWidgets.QMessageBox.critical(
                self,
                "Erreur",
                "Impossible d'enregistrer les modifications."
            )

    def export_graph_png(self):
        self.tabs.setCurrentWidget(self.plot_widget)
        self.plot_widget.export_png()
        self.statusBar().showMessage("Export du graphe demandé")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Quitter",
            "Voulez-vous vraiment quitter l'application ?",
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No,
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def show_about(self):
        QtWidgets.QMessageBox.about(
            self,
            "À propos",
            """
            <h3>Application de visualisation de données</h3>
            <p>Version 1.0</p>
            <p>Formation Python Interfaces Graphiques</p>
            <p>PySide6 / SQLite / Modèle-Vue / Graphiques</p>
            """,
        )