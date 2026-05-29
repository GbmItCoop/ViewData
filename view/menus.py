def create_menus(window):

    # Menu Fichier
    file_menu = window.menuBar().addMenu("Fichier")

    file_menu.addAction(window.open_action)
    file_menu.addAction(window.save_action)
    file_menu.addAction(window.export_action)

    file_menu.addSeparator()

    file_menu.addAction(window.quit_action)

    # Menu Aide
    help_menu = window.menuBar().addMenu("Aide")

    help_menu.addAction(window.about_action)
    help_menu.addSeparator()
    help_menu.addAction(window.about_qt_action)