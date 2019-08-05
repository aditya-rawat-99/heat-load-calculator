from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QPushButton, QMdiSubWindow
import sys
import testing
import NewWindow
from backend import calculate
from PyQt5 import QtCore


class Summer(QMainWindow):
    def __init__(self, parent=None):
        super(Summer, self).__init__(parent)

        self.backend = calculate()
        self.difference_dbfb = None
        self.difference_Grlb = None

        self.main = testing.Ui_MainWindow()
        self.main.setupUi(self)
        self.main.calculateSummer_PB.clicked.connect(lambda: self.populateTable(self.main.tableWidget_Summer))
        self.main.tableWidget_Summer.cellDoubleClicked.connect(
            lambda: self.doubleClickOnCellItem(self.main.tableWidget_Summer))

        self.main.actionQuit.triggered.connect(self.close)

    def populateTable(self, table):
        col = 0
        for row in range(0, table.rowCount()):
            try:
                Area = float((table.item(row, col)).text())
                SunGain = float((table.item(row, col + 1)).text())
                Factor = float(table.item(row, col + 2).text())
            except Exception as err:
                QMessageBox.about(self, "Invalid Values", "Enter Proper Values")
                return

            table.setItem(row, 3, QTableWidgetItem(str(self.backend.calculateValues(Area, SunGain, Factor))))

    def getDifference(self):
        self.difference_dbfb = float(str(self.main.difference_dbfb.text()))
        self.difference_Grlb = float(str(self.main.difference_grlb.text()))

    def doubleClickOnCellItem(self, table):
        index = table.currentIndex()

        if index.column() == 2 and index.row() == 0:
            try:
                val = float((table.item(index.row(), index.column())).text())
            except:
                QMessageBox.about(self, "Invalid Value", "Value of Factor is Invalid")
                return
            for i in range(0, table.rowCount()):
                table.setItem(i, 2, QTableWidgetItem(str(val)))
        else:
            return

    def getSetValues(self):

        # Get Values
        try:
            self.people = float(self.main.People_LE.text())
            self.freshAir = float(self.main.FreshAir_LE.text())
            self.FloorArea = float(self.main.FloorArea_LE.text())
            self.Height = float(self.main.Height_LE.text())
            self.AirChangeReq = float(self.main.AirChangeReq_LE.text())
        except Exception as err:
            QMessageBox.about(self, "Invalid Value", "Enter Appropriate Values")
            return
        # Calculate Values
        FA = format(float(str(self.backend.calculate_FA(self.people, self.freshAir, self.FloorArea))), ".6f")
        UV = format(float(str(self.backend.calculate_UV(self.Height, self.FloorArea, self.AirChangeReq))), ".6f")
        FA_Input = format(float(str(self.backend.calculate_FAInput())), ".6f")

        # Display values
        self.main.FA_LE.setText(FA)
        self.main.Unknown_LE.setText(UV)
        self.main.FAInput_LE.setText(FA_Input)

    def messageBox(self):
        return QMessageBox.about(self, "Invalid Value", "Enter Appropriate Values")


class Monsoon(Summer):
    def __init__(self, parent=None):
        super(Monsoon, self).__init__(parent)
        self.main.calculateMonsoon_PB.clicked.connect(lambda: self.populateTable(self.main.tableWidget_Monsoon))
        self.main.tableWidget_Monsoon.cellDoubleClicked.connect(
            lambda: self.doubleClickOnCellItem(self.main.tableWidget_Monsoon))
        self.main.Calculate_PB.clicked.connect(self.getSetValues)
        self.main.NewWindow.clicked.connect(self.NewWindow)

    # New Window

    def NewWindow(self):
        self.setDisabled(True)
        self.dialog = newWin(self)
        self.dialog.show()


class newWin(QMainWindow):
    def __init__(self, parent):
        super(newWin, self).__init__(parent)
        self.main = NewWindow.Ui_MainWindow()
        self.main.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)


if __name__ == '__main__':
    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)
    ex = Monsoon()
    ex.show()
    sys.exit(app.exec_())
