# Application de Visualisation de Données

## Présentation

Cette application a été développée en Python avec PySide6 dans le cadre de la formation **Concevoir une Interface Graphique en Python**.

Elle permet :

* d'ouvrir une base de données SQLite ;
* de sélectionner une table ;
* d'afficher les données dans une vue tabulaire ;
* de modifier les données ;
* d'enregistrer les modifications ;
* de visualiser les données sous forme graphique ;
* d'exporter un graphique au format PNG.

L'application utilise l'architecture **Modèle / Vue** proposée par Qt.

---

## Technologies utilisées

* Python 3
* PySide6
* SQLite
* Qt Model/View
* QSqlDatabase
* QSqlTableModel
* QTableView
* PyQtGraph

---

## Structure du projet

```text
ViewData/
│
├── app.py
├── README.md
├── requirements.txt
│
├── model/
│   ├── __init__.py
│   └── sql_model.py
│
└── view/
    ├── __init__.py
    ├── actions.py
    ├── menus.py
    ├── toolbar.py
    ├── mainwindow.py
    ├── data_widget.py
    ├── open_table_dialog.py
    ├── about_table_dialog.py
    ├── PlotWidget.py
    ├── PlotWidget_ui.py
    └── PlotWidget.ui
```

---

## Installation

Créer un environnement virtuel :

```bash
python3 -m venv .venv
```

Activer l'environnement :

Linux :

```bash
source .venv/bin/activate
```

Windows :

```cmd
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Lancement

Depuis le dossier du projet :

```bash
python app.py
```

---

## Utilisation

### Ouvrir une table

Menu :

```text
Fichier → Ouvrir une table
```

Sélectionner :

* un fichier SQLite (.db)
* une table

Les données sont alors affichées dans l'onglet **Données**.

---

### Modifier les données

Les données affichées dans le tableau peuvent être modifiées directement.

Pour enregistrer :

```text
Fichier → Enregistrer les modifications
```

ou :

```text
Ctrl + S
```

---

### Afficher un graphique

1. Ouvrir une table.
2. Aller dans l'onglet **Graphes**.
3. Choisir une colonne pour les abscisses.
4. Choisir une colonne pour les ordonnées.
5. Cliquer sur **Tracer**.

Le graphique est généré à partir du modèle Qt.

---

### Exporter un graphique

Menu :

```text
Fichier → Exporter le graphe en PNG
```

ou :

```text
Ctrl + E
```

---

## Architecture Modèle / Vue

L'application repose sur les composants Qt suivants :

```text
QSqlDatabase
        │
        ▼
QSqlTableModel
        │
 ┌──────┴─────────┐
 ▼                ▼
QTableView     PlotWidget
```

Cette architecture garantit une séparation claire entre :

* les données ;
* leur représentation ;
* les interactions utilisateur.

---

## Auteur

Projet réalisé par Gloria MADZOU dans le cadre de la formation Python Interface Graphique :

**Concevoir une Interface Graphique en Python**

Développé avec Python, PySide6 et SQLite.
