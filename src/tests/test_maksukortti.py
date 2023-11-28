import unittest
from src.maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def test_kortin_saldo_alustetaan_oikein(self):
        kortti = Maksukortti(1000)
        self.assertEqual(kortti.saldo, 1000)

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_edullisesti()
        self.assertEqual(kortti.saldo, 760)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(1000)
        kortti.syo_maukkaasti()
        self.assertEqual(kortti.saldo, 600)


if __name__ == '__main__':
    unittest.main()
