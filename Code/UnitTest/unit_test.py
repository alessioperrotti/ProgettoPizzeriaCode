import pickle
import unittest
from datetime import date, timedelta
from PyQt6.QtWidgets import QApplication

from Code.GestioneDipendenti.Controller.cont_inserisci_dipendente import ContInserisciDipendente, UsedUsername, \
    OutOfDate
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente


class TestContInserisciDipendente(unittest.TestCase):
    def setUp(self):
        # Creare una vista e un'applicazione fittizia per i test
        self.app = QApplication([])
        self.view = VistaInserisciDipendente()
        self.controller = ContInserisciDipendente(None, self.view)

    def test_confirm_close_valid_data(self):
        # Simulare dati validi e testare se il metodo funziona correttamente
        self.view.edit_nome.setText("Nome")
        self.view.edit_cognome.setText("Cognome")
        self.view.edit_ruolo.setCurrentText("Cuoco")
        self.view.edit_email.setText("email@example.com")
        self.view.edit_stipendio.setText("1000.00")
        self.view.calendario.setSelectedDate(date.today())
        self.view.edit_username.setText("nuovo_username")
        self.view.edit_password.setText("password123")

        try:
            self.controller.confirm_close()
        except Exception as e:
            self.assertFalse(True, f"Eccezione sollevata: {e}")

        # Aggiungi ulteriori asserzioni se necessario

    def test_confirm_close_invalid_data(self):
        # Simulare dati invalidi e testare se il metodo gestisce correttamente le eccezioni
        self.view.edit_nome.setText("")  # Nome vuoto per causare un'eccezione
        self.view.edit_cognome.setText("Cognome")
        # Aggiungi altri dati secondo necessità

        with self.assertRaises(ValueError):  # Assicurarsi che un'eccezione sia sollevata
            self.controller.confirm_close()

        # Aggiungi ulteriori asserzioni se necessario

    def test_confirm_close_used_username(self):
        # Simulare un caso in cui l'username è già utilizzato e verificare se l'eccezione viene gestita correttamente
        self.view.edit_nome.setText("Nome")
        self.view.edit_cognome.setText("Cognome")
        self.view.edit_ruolo.setCurrentText("Cuoco")
        self.view.edit_email.setText("email@example.com")
        self.view.edit_stipendio.setText("1000.00")
        self.view.calendario.setSelectedDate(date.today())
        self.view.edit_username.setText("filippoS")  # Simula un'username già esistente nel modello
        self.view.edit_password.setText("filippo")

        with self.assertRaises(UsedUsername):  # Assicurarsi che l'eccezione specifica venga sollevata
            self.controller.confirm_close()

        # Aggiungi ulteriori asserzioni se necessario

    def test_confirm_close_out_of_date(self):
        # Simulare un caso in cui la data di nascita è futura e verificare se l'eccezione viene gestita correttamente
        self.view.edit_nome.setText("Nome")
        self.view.edit_cognome.setText("Cognome")
        self.view.edit_ruolo.setCurrentText("Cuoco")
        self.view.edit_email.setText("email@example.com")
        self.view.edit_stipendio.setText("1000.00")
        self.view.calendario.setSelectedDate(date.today() + timedelta(days=1))  # Data futura
        self.view.edit_username.setText("nuovo_username")
        self.view.edit_password.setText("password123")

        with self.assertRaises(OutOfDate):  # Assicurarsi che l'eccezione specifica venga sollevata
            self.controller.confirm_close()

    def tearDown(self):
        # Pulisci le risorse dopo ogni test se necessario
        self.app.quit()


if __name__ == '__main__':
    unittest.main()
