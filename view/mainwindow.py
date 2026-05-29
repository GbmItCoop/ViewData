from PySide6 import QtWidgets
from view.data_widget import DataWidget
from view.PlotWidget import PlotWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application de visualisation de données")
        self.resize(900, 550)

        self.create_central_widget()

    def create_central_widget(self):
        self.tabs = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabs)

        self.data_widget = DataWidget()
        self.plot_widget = PlotWidget()

        self.tabs.addTab(self.data_widget, "Données")
        self.tabs.addTab(self.plot_widget, "Graphes")