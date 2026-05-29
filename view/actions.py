from PySide6 import QtGui, QtWidgets


def create_actions(window):
    style = window.style()

    window.open_action = QtGui.QAction(
        style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogOpenButton),
        "Ouvrir une table",
        window
    )
    window.open_action.setShortcut("Ctrl+O")
    window.open_action.triggered.connect(window.open_table)

    window.save_action = QtGui.QAction(
        style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogSaveButton),
        "Enregistrer les modifications",
        window
    )
    window.save_action.setShortcut("Ctrl+S")
    window.save_action.triggered.connect(window.save_changes)

    window.export_action = QtGui.QAction(
        style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogYesButton),
        "Exporter le graphe en PNG",
        window
    )
    window.export_action.setShortcut("Ctrl+E")
    window.export_action.triggered.connect(window.export_graph_png)

    window.quit_action = QtGui.QAction(
        style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton),
        "Quitter",
        window
    )
    window.quit_action.setShortcut("Ctrl+Q")
    window.quit_action.triggered.connect(window.close)

    # Menu Aide
    window.about_action = QtGui.QAction(
        "À propos",
        window
    )
    window.about_action.triggered.connect(window.show_about)

    window.about_qt_action = QtGui.QAction(
        "À propos de Qt",
        window
    )
    window.about_qt_action.triggered.connect(
        QtWidgets.QApplication.aboutQt
    )