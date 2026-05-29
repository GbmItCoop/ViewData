import os
from PySide6 import QtWidgets, QtCore


class AboutTableDialog(QtWidgets.QDialog):
    def __init__(self, database_path, table_name, model, parent=None):
        super().__init__(parent)

        self.database_path = database_path
        self.table_name = table_name
        self.model = model

        self.setWindowTitle("Informations sur la table")
        self.resize(450, 250)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        file_name = os.path.basename(self.database_path)

        self.database_label = QtWidgets.QLabel(f"Base de données : {file_name}")
        self.path_label = QtWidgets.QLabel(f"Chemin : {self.database_path}")
        self.table_label = QtWidgets.QLabel(f"Table ouverte : {self.table_name}")

        row_count = self.model.rowCount() if self.model else 0
        column_count = self.model.columnCount() if self.model else 0

        self.rows_label = QtWidgets.QLabel(f"Nombre de lignes : {row_count}")
        self.columns_label = QtWidgets.QLabel(f"Nombre de colonnes : {column_count}")

        self.columns_list = QtWidgets.QListWidget()

        if self.model:
            for column in range(column_count):
                column_name = self.model.headerData(
                    column,
                    QtCore.Qt.Orientation.Horizontal
                )
                self.columns_list.addItem(str(column_name))

        self.close_button = QtWidgets.QPushButton("Fermer")

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.database_label)
        layout.addWidget(self.path_label)
        layout.addWidget(self.table_label)
        layout.addWidget(self.rows_label)
        layout.addWidget(self.columns_label)

        layout.addWidget(QtWidgets.QLabel("Colonnes :"))
        layout.addWidget(self.columns_list)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.close_button)

        layout.addLayout(buttons_layout)

        self.close_button.clicked.connect(self.accept)