from PySide6.QtSql import QSqlDatabase, QSqlTableModel


class DatabaseModel:
    def __init__(self):
        self.database = None
        self.model = None
        self.last_error = ""

    def open_database(self, db_file, table_name):
        self.last_error = ""

        connection_name = "main_connection"

        if QSqlDatabase.contains(connection_name):
            self.database = QSqlDatabase.database(connection_name)
        else:
            self.database = QSqlDatabase.addDatabase("QSQLITE", connection_name)

        self.database.setDatabaseName(db_file)

        if not self.database.open():
            self.last_error = self.database.lastError().text()
            return False

        self.model = QSqlTableModel(db=self.database)
        self.model.setTable(table_name)

        if not self.model.select():
            self.last_error = self.model.lastError().text()
            return False

        if self.model.columnCount() == 0:
            self.last_error = "La table ne contient aucune colonne."
            return False

        return True

    def submit(self):
        if self.model is None:
            self.last_error = "Aucune table ouverte."
            return False

        if not self.model.submitAll():
            self.last_error = self.model.lastError().text()
            return False

        return True