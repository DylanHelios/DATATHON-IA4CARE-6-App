import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QFileDialog, QHeaderView, QSizePolicy, QSpacerItem, QDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class CelluleAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analyseur de Cellules")
        self.resize(900, 600)

        self.first_file_loaded = False  # Pour empêcher de changer le label de gauche
        self.categories = [
            "Bénin", "Bénin < 104", "AUS", "Microvésicule",
            "Microvésicule Atypies", "onco", "Malin CPT", "Médullaire"
        ]

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        # Bouton fichier
        file_button = QPushButton("File")
        file_button.clicked.connect(self.load_file)
        file_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        main_layout.addWidget(file_button, alignment=Qt.AlignLeft)

        # Labels de nom de fichier
        filenames_layout = QHBoxLayout()

        # Label centré à gauche
        self.label_file1 = QLabel("Nom de fichier")
        self.label_file1.setAlignment(Qt.AlignCenter)
        self.label_file1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        filenames_layout.addWidget(self.label_file1)

        # Espacement au centre (facultatif)
        # filenames_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Label centré à droite
        self.label_file2 = QLabel("")
        self.label_file2.setAlignment(Qt.AlignCenter)
        self.label_file2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        filenames_layout.addWidget(self.label_file2)

        main_layout.addLayout(filenames_layout)

        # Tableau
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Catégorie de cellules", "Nombres", "% de cellule", "Gallerie Image"
        ])
        
        # Ajuster la taille des colonnes
        self.table.setColumnWidth(0, 200)  # Largeur pour "Catégorie de cellules"
        self.table.setColumnWidth(1, 100)  # Largeur pour "Nombres"
        self.table.setColumnWidth(2, 100)  # Largeur pour "% de cellule"
        
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)  # Étendre la dernière colonne
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.table)

        self.populate_table()

    def populate_table(self):
        self.table.setRowCount(len(self.categories))

        for i, category in enumerate(self.categories):
            item = QTableWidgetItem(category)
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(i, 0, item)
            self.table.setItem(i, 1, QTableWidgetItem(""))
            self.table.setItem(i, 2, QTableWidgetItem(""))
            self.table.setItem(i, 3, QTableWidgetItem(""))

    def show_image_in_fullscreen(self, image_path):
        dialog = QDialog(self)
        dialog.setWindowTitle("Image en gros plan")
        layout = QVBoxLayout()
        label = QLabel()
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap.scaled(800, 600, Qt.KeepAspectRatio))
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec_()

    def update_table_from_json(self, data):
        self.table.setRowCount(len(data))

        for i, entry in enumerate(data):
            category_item = QTableWidgetItem(entry['Nom'])
            category_item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(i, 0, category_item)

            number_item = QTableWidgetItem(str(entry['Nombre']))
            self.table.setItem(i, 1, number_item)

            # Gérer les images
            images_layout = QVBoxLayout()
            for image_path in entry['Images']:
                image_label = QLabel()
                pixmap = QPixmap(image_path)
                image_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))
                image_label.mousePressEvent = lambda event, path=image_path: self.show_image_in_fullscreen(path)
                images_layout.addWidget(image_label)
            images_widget = QWidget()
            images_widget.setLayout(images_layout)
            self.table.setCellWidget(i, 3, images_widget)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Fichiers png (*.png);;Tous les fichiers (*)")
        if file_path:
            file_name = file_path.split("/")[-1]

            # Label de droite : toujours mis à jour
            self.label_file2.setText(file_name)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    import json
                    data = json.load(f)
                    self.update_table_from_json(data['Categorie'])
            except Exception as e:
                print("Erreur :", e)

    def load_fake_data(self):
        # Données fictives
        fake_data = [
            {"Nom": "Bénin", "Nombre": 13, "Images": ["~/Bureau/thumbnail_224x224/.svs_ann_1923.png", "~/Bureau/thumbnail_224x224/32076A.svs_ann_1924.png"]},
            {"Nom": "AUS", "Nombre": 7, "Images": ["~/Bureau/thumbnail_224x224/33577.svs_ann_3684.png", "~/Bureau/thumbnail_224x224/33577.svs_ann_3685.png"]},
            {"Nom": "Microvésicule", "Nombre": 5, "Images": ["~/Bureau/thumbnail_224x224/3689.svs_ann_1163.png", "~/Bureau/thumbnail_224x224/3689.svs_ann_1164.png"]},
            {"Nom": "Malin CPT", "Nombre": 10, "Images": ["~/Bureau/thumbnail_224x224/4415.svs_ann_4316.png", "~/Bureau/thumbnail_224x224/4415.svs_ann_4317.png"]}
        ]
        # Calculer le total
        total = sum(entry['Nombre'] for entry in fake_data)

        # Mettre à jour le tableau avec les données fictives
        self.table.setRowCount(len(fake_data))

        for i, entry in enumerate(fake_data):
            category_item = QTableWidgetItem(entry['Nom'])
            category_item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(i, 0, category_item)

            number_item = QTableWidgetItem(str(entry['Nombre']))
            self.table.setItem(i, 1, number_item)

            # Calculer et afficher le pourcentage
            percentage = (entry['Nombre'] / total) * 100
            percentage_item = QTableWidgetItem(f"{percentage:.2f}%")
            self.table.setItem(i, 2, percentage_item)

            # Gérer les images
            images_layout = QVBoxLayout()
            for image_path in entry['Images']:
                image_label = QLabel()
                pixmap = QPixmap(image_path)
                image_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))
                image_label.mousePressEvent = lambda event, path=image_path: self.show_image_in_fullscreen(path)
                images_layout.addWidget(image_label)
            images_widget = QWidget()
            images_widget.setLayout(images_layout)
            self.table.setCellWidget(i, 3, images_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CelluleAnalyzer()
    window.load_fake_data()
    window.show()
    sys.exit(app.exec())
