import sys
from PyQt5.QtWidgets import *

widgets = [
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLCDNumber,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit
    ]
app = QApplication(sys.argv)
root = QWidget()
grid = QHBoxLayout()

toolbar = QToolBar("My main toolbar")
for w in widgets:
    grid.addWidget(w())
root.setLayout(grid)
#root.resize(250, 250)
root.setWindowTitle("Hello world!")
root.show()
if __name__ == '__main__':
    sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
# root = QWidget()
# root.resize(250, 250)
# root.setWindowTitle("Hello world!")
# root.show()
#
# grid = QGridLayout()
#
# root.setLayout(grid)
#
# grid.addWidget(composant1, 0, 0) # composant, ligne, colonne
# grid.addWidget(composant2, 1, 0) # composant, ligne, colonne
# grid.addWidget(composant3, 0, 1) # composant, ligne, colonne
# grid.addWidget(composant4, 1, 1)
# if __name__ == '__main__':
#     sys.exit(app.exec_())