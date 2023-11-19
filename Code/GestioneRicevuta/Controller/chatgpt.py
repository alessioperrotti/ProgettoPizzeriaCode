import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit

class Finestra(QWidget):
    def __init__(self):
        super().__init__()

        # Crea una tabella con dati di esempio
        self.tabella = QTableWidget(self)
        self.tabella.setColumnCount(3)
        self.tabella.setHorizontalHeaderLabels(["Nome", "Cognome", "Età"])

        dati = [
            ["Alice", "Rossi", 25],
            ["Bob", "Verdi", 30],
            ["Charlie", "Blu", 22],
            ["David", "Gialli", 28]
        ]

        self.aggiungi_dati_tabella(dati)

        # Crea un campo di ricerca
        self.campo_ricerca = QLineEdit(self)
        self.campo_ricerca.setPlaceholderText("Inserisci il nome")

        # Connetti il segnale di modifica del campo di ricerca al metodo di aggiornamento della tabella
        self.campo_ricerca.textChanged.connect(self.filtra_tabella)

        # Layout principale
        layout_principale = QVBoxLayout(self)
        layout_principale.addWidget(self.campo_ricerca)
        layout_principale.addWidget(self.tabella)

    def aggiungi_dati_tabella(self, dati):
        self.tabella.setRowCount(len(dati))
        for riga, dati_riga in enumerate(dati):
            for colonna, dato in enumerate(dati_riga):
                item = QTableWidgetItem(str(dato))
                self.tabella.setItem(riga, colonna, item)

    def filtra_tabella(self):
        testo_ricerca = self.campo_ricerca.text().lower()

        for riga in range(self.tabella.rowCount()):
            nome = self.tabella.item(riga, 0).text().lower()
            self.tabella.setRowHidden(riga, testo_ricerca not in nome)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    finestra = Finestra()
    finestra.show()
    sys.exit(app.exec())
