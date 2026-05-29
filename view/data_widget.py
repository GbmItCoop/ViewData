from PySide6 import QtWidgets


class DataWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["A", "B", "C"])

        layout.addWidget(self.table)

        self.load_fake_data()

    def load_fake_data(self):
        for row in range(10):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(row * 2)))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(row * 3)))

        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )