from PySide6 import QtWidgets


def create_toolbar(window):
    toolbar = QtWidgets.QToolBar("Fichier")
    toolbar.setMovable(False)

    toolbar.addAction(window.open_action)
    toolbar.addAction(window.save_action)
    toolbar.addAction(window.export_action)
    toolbar.addSeparator()
    toolbar.addAction(window.quit_action)

    window.addToolBar(toolbar)