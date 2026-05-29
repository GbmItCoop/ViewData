from PySide6 import QtWidgets, QtCore


class DataWidget(QtWidgets.QWidget):

    columns_changed = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        # Étape 4 : modèle/vue
        # On utilise QTableView au lieu de QTableWidget
        self.table = QtWidgets.QTableView()
        layout.addWidget(self.table)

        self.model = None

    def set_model(self, model):
        self.model = model
        self.table.setModel(self.model)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

        self.columns_changed.emit(self.get_columns())

    def get_columns(self):
        if self.model is None:
            return []

        columns = []

        for column in range(self.model.columnCount()):
            column_name = self.model.headerData(
                column,
                QtCore.Qt.Orientation.Horizontal
            )
            columns.append(str(column_name))

        return columns