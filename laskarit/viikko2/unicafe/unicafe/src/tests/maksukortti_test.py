import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def test_kortin_saldo_alussa_oikein(self):
        kortti = Maksukortti(1000)
        self.assertEqual(kortti.saldo, 1000)

    def testa_rahan_lataaminen(self):
        kortti = Maksukortti(0)
        kortti.lataa_rahaa(500)
        self.assertEqual(kortti.saldo, 500) #we check if we got 500

    def testa_rahan_ottaminen(self):
        kortti = Maksukortti(1000)
        result = kortti.ota_rahaa(500)
        self.assertTrue(result)
        self.assertEqual(kortti.saldo, 500)  #we add 1000, take 500 and check if 500

    def testa_rahan_ottaminen_ei_muuta(self):
        kortti = Maksukortti(200)
        result = kortti.ota_rahaa(500)
        self.assertFalse(result)
        self.assertEqual(kortti.saldo, 200) #we check if can take money 500 from 200 (minus values should not be made or impossible to do)

    def testa_ota_rahaa_palauttaa(self):
        kortti = Maksukortti(1000)
        result = kortti.ota_rahaa(500)
        self.assertTrue(result) # if we add 100 and take 500, we are left with 500 

    def testa_ota_rahaa_palauttaa_false(self):
        kortti = Maksukortti(200)
        result = kortti.ota_rahaa(500)
        self.assertFalse(result) #if we only have 200 and take 500 is impossible

