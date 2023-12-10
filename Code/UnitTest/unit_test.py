import unittest

from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu


class TestGestoreMenu(unittest.TestCase):

    def setUp(self):
        # Creazione di una materia prima di esempio
        self.materia_prima_di_esempio = MateriaPrima(
            codice="MP1",
            nome="Ingrediente di Esempio",
            costo_al_kg=4.0,
            qta_disponibile=150,
            qta_limite=300,
            qta_ordine_STD=50,
            data_scadenza="2023-12-31"
        )

        # Creazione di un prodotto di esempio che utilizza la materia prima
        self.prodotto_di_esempio = Prodotto(
            nome="Prodotto di Esempio",
            codice=123,
            prezzo_al_pubblico=10.99,
            tipologia="Tipologia di Esempio",
            ingredienti=[
                (self.materia_prima_di_esempio, 100),
            ]
        )
        self.gestore_menu = GestoreMenu()

    def test_calcola_costo_unitario(self):
        costo_unitario_calcolato = self.prodotto_di_esempio.calcola_costo_unitario()
        self.assertEqual(costo_unitario_calcolato, 400.0)

    def test_aggiungi_prodotto(self):
        self.gestore_menu.aggiungi_prodotto(self.prodotto_di_esempio)
        prodotto_recuperato = self.gestore_menu.estrai_per_nome("Prodotto di Esempio")
        self.assertIsNotNone(prodotto_recuperato)
        self.assertEqual(prodotto_recuperato.nome, "Prodotto di Esempio")

    def test_estrai_per_nome_trovato(self):
        self.gestore_menu.aggiungi_prodotto(self.prodotto_di_esempio)
        prodotto_trovato = self.gestore_menu.estrai_per_nome("Prodotto di Esempio")

        self.assertIsNotNone(prodotto_trovato)
        self.assertEqual(prodotto_trovato.nome, self.prodotto_di_esempio.nome)
        self.assertEqual(prodotto_trovato.codice, self.prodotto_di_esempio.codice)
        self.assertEqual(prodotto_trovato.prezzo_al_pubblico, self.prodotto_di_esempio.prezzo_al_pubblico)

    def test_estrai_per_nome_non_trovato(self):
        # Test quando il prodotto con il nome specificato NON è presente nella lista
        prodotto_non_trovato = self.gestore_menu.estrai_per_nome("ProdottoNonEsistente")
        self.assertIsNone(prodotto_non_trovato)

    def test_modifica_prodotto(self):
        self.gestore_menu.aggiungi_prodotto(self.prodotto_di_esempio)
        self.gestore_menu.modifica_prodotto("Prodotto di Esempio", 15.99, ["Nuovo Ingrediente1", "Nuovo Ingrediente2"])
        prodotto_modificato = self.gestore_menu.estrai_per_nome("Prodotto di Esempio")
        self.assertEqual(prodotto_modificato.prezzo_al_pubblico, 15.99)
        self.assertEqual(prodotto_modificato.ingredienti, ["Nuovo Ingrediente1", "Nuovo Ingrediente2"])


if __name__ == '__main__':
    unittest.main()
