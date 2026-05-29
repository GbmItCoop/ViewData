from PySide6 import QtWidgets

from view.data_widget import DataWidget
from view.PlotWidget import PlotWidget
from view.actions import create_actions
from view.menus import create_menus
from view.toolbar import create_toolbar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application de visualisation de données")
        self.resize(900, 550)

        create_actions(self)
        create_menus(self)
        create_toolbar(self)

        self.create_central_widget()
        self.statusBar().showMessage("Prêt")

    def create_central_widget(self):
        self.tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabs)

        self.data_widget = DataWidget()
        self.plot_widget = PlotWidget()

        self.tabs.addTab(self.data_widget, "Données")
        self.tabs.addTab(self.plot_widget, "Graphes")

    def open_table(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Ouvrir une base SQLite",
            "",
            "Bases SQLite (*.sqlite *.db);;Tous les fichiers (*)",
        )

        if file_path:
            self.data_widget.load_fake_data()
            self.statusBar().showMessage(f"Table ouverte : {file_path}")
            self.tabs.setCurrentWidget(self.data_widget)

    def save_changes(self):
        QtWidgets.QMessageBox.information(
            self, "Enregistrement", "Les modifications ont été enregistrées."
        )
        self.statusBar().showMessage("Modifications enregistrées")

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

        Version 1.0

        Formation Python Interfaces Graphiques

        PySide6 / SQLite / Graphiques
        """,
        )
