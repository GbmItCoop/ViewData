from PySide6.QtSql import (
    QSqlDatabase,
    QSqlTableModel
)


class DatabaseModel:

    def __init__(self):
        self.database = None
        self.model = None

    def open_database(self, db_file, table_name):

        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(db_file)

        if not self.database.open():
            return False

        self.model = QSqlTableModel()
        self.model.setTable(table_name)
        self.model.select()

        return True

    def submit(self):
        return self.model.submitAll()