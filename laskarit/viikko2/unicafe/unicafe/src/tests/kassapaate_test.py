import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()

    def initializing(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0) #we initialize the amount of money we have and kassapate edulliset and maukkaat to 0

    def kateisella_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1) #We add 300 and get edulisessti for kateisella - we should have 100240 

    def kateisella_ei_miinukseen(self):
        
        
        
        
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0) #we test if we wont be on the minus side

    def syo_mukaaisti_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1) #we get syo_maukaasti one time and pay by cash

    def syo_maukaasti_ei_kateisella(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0) #

    def kortilla_edullinen(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
        
        
        result = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
    
        self.assertTrue(result)

    def syo_maukkaasti_kortilla(self):
     
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)

      
        self.maksukortti.ota_rahaa(500)  
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1) 

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)