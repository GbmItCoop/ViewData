import sqlite3
from PySide6 import QtWidgets


class OpenTableDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ouvrir une table")
        self.resize(500, 150)

        self.database_path = None
        self.table_name = None

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.file_edit = QtWidgets.QLineEdit()
        self.file_edit.setReadOnly(True)

        self.browse_button = QtWidgets.QPushButton("Parcourir...")

        self.table_combo = QtWidgets.QComboBox()

        self.ok_button = QtWidgets.QPushButton("Ouvrir")
        self.cancel_button = QtWidgets.QPushButton("Annuler")

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        file_layout = QtWidgets.QHBoxLayout()
        file_layout.addWidget(QtWidgets.QLabel("Base de données :"))
        file_layout.addWidget(self.file_edit)
        file_layout.addWidget(self.browse_button)

        table_layout = QtWidgets.QHBoxLayout()
        table_layout.addWidget(QtWidgets.QLabel("Table :"))
        table_layout.addWidget(self.table_combo)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        main_layout.addLayout(file_layout)
        main_layout.addLayout(table_layout)
        main_layout.addLayout(buttons_layout)

    def create_connections(self):
        self.browse_button.clicked.connect(self.choose_database)
        self.ok_button.clicked.connect(self.validate)
        self.cancel_button.clicked.connect(self.reject)

    def choose_database(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Choisir une base SQLite",
            "",
            "Bases SQLite (*.db *.sqlite *.sqlite3);;Tous les fichiers (*)"
        )

        if not file_path:
            return

        self.database_path = file_path
        self.file_edit.setText(file_path)
        self.load_tables(file_path)

    def load_tables(self, file_path):
        self.table_combo.clear()

        try:
            connection = sqlite3.connect(file_path)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type = 'table'
                ORDER BY name
            """)

            tables = [row[0] for row in cursor.fetchall()]
            connection.close()

            self.table_combo.addItems(tables)

        except sqlite3.Error as error:
            QtWidgets.QMessageBox.critical(
                self,
                "Erreur SQLite",
                f"Impossible de lire la base de données :\n{error}"
            )

    def validate(self):
        if not self.database_path:
            QtWidgets.QMessageBox.warning(
                self,
                "Base manquante",
                "Veuillez sélectionner une base de données."
            )
            return

        if self.table_combo.currentText() == "":
            QtWidgets.QMessageBox.warning(
                self,
                "Table manquante",
                "Aucune table n'a été sélectionnée."
            )
            return

        self.table_name = self.table_combo.currentText()
        self.accept()