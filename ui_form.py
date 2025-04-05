# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionImportFile = QAction(main)
        self.actionImportFile.setObjectName(u"actionImportFile")
        self.actionSaveRapport = QAction(main)
        self.actionSaveRapport.setObjectName(u"actionSaveRapport")
        self.menuBar = QMenuBar(main)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(9, 9, 109, 23))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.layoutWidget = QWidget(main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_valeur_image = QLabel(main)
        self.label_valeur_image.setObjectName(u"label_valeur_image")
        self.label_valeur_image.setGeometry(QRect(320, 80, 158, 36))
        self.label_valeur_image.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_nom_image = QLabel(main)
        self.label_nom_image.setObjectName(u"label_nom_image")
        self.label_nom_image.setGeometry(QRect(150, 50, 158, 78))
        self.label_nom_image.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
#if QT_CONFIG(shortcut)
        self.label_valeur_image.setBuddy(self.label_valeur_image)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionImportFile)
        self.menuFile.addAction(self.actionSaveRapport)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionImportFile.setText(QCoreApplication.translate("main", u"Import File", None))
        self.actionSaveRapport.setText(QCoreApplication.translate("main", u"Save rapport", None))
        self.menuFile.setTitle(QCoreApplication.translate("main", u"File", None))
        self.label_valeur_image.setText("")
        self.label_nom_image.setText(QCoreApplication.translate("main", u"Nom de l'image:", None))
    # retranslateUi

