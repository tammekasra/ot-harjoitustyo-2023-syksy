import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
    def saldo_euroina(self):
        return self.saldo / 100

    def test_konstruktori_asettaa_saldon_oikein(self):
        # alustetaan maksukortti, jossa on 10 euroa (1000 senttiä)
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 9.00 euroa")
    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
    	kortti = Maksukortti(1000)
    	kortti.syo_edullisesti()

    	self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")
    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
    	kortti = Maksukortti(1000)
    	kortti.syo_edullisesti()

    	self.assertEqual(kortti.saldo_euroina(), 7.5)
