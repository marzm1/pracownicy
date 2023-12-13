import sys
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.imieEdit.editingFinished.connect(self.imie_editing_finished)
        self.ui.nazwiskoEdit.editingFinished.connect(self.nazwisko_editing_finished)
        self.ui.telEdit.editingFinished.connect(self.tel_editing_finished)
        self.ui.peselEdit.editingFinished.connect(self.pesel_editing_finished)
        self.ui.umowaCheckbox.clicked.connect(self.checkbox)
        self.ui.zapiszButton.clicked.connect(self.zapisz_button_clicked)

        self.show()

    def imie_editing_finished(self):
        pass

    def nazwisko_editing_finished(self):
        pass

    def tel_editing_finished(self):
        pass

    def pesel_editing_finished(self):
        pass

    def checkbox(self):
         pass

    def zapisz_button_clicked(self):
        imie = self.ui.imieEdit.text()
        nazwisko = self.ui.nazwiskoEdit.text()
        tel = self.ui.telEdit.text()
        if self.ui.telEdit.isDigit() == True:
            pass
        else:


        pesel = self.ui.peselEdit.text()
        umowa_o_prace = self.ui.umowaCheckbox.isChecked()
        if umowa_o_prace == True:
            umowa_o_prace = 'umowa o prace'

        else:
            umowa_o_prace = 'bez umowy o prace'

        pracownik = f"{imie} {nazwisko} {tel} {pesel} {umowa_o_prace}"
        self.ui.poleZapisu.addItem(pracownik)

        self.ui.imieEdit.clear()
        self.ui.nazwiskoEdit.clear()
        self.ui.telEdit.clear()
        self.ui.peselEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MyForm()
    sys.exit(app.exec())