import sqlite3
from PySide6 import QtWidgets, QtCore


class DataWidget(QtWidgets.QWidget):

    columns_changed = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget()
        layout.addWidget(self.table)

        self.load_fake_data()

    def load_fake_data(self):
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["A", "B", "C"])

        for row in range(10):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(row * 2)))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(row * 3)))

        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )

        self.columns_changed.emit(self.get_columns())

    def load_sqlite_table(self, database_path, table_name):
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM "{table_name}"')
        rows = cursor.fetchall()

        columns = [description[0] for description in cursor.description]

        connection.close()

        self.table.clear()
        self.table.setColumnCount(len(columns))
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(columns)

        for row_index, row_data in enumerate(rows):
            for col_index, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row_index, col_index, item)

        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )

        self.columns_changed.emit(columns)

    def get_columns(self):
        return [
            self.table.horizontalHeaderItem(i).text()
            for i in range(self.table.columnCount())
        ]