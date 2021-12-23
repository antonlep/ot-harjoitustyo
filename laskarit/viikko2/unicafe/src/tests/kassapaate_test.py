import unittest
from kassapaate import Kassapaate
from kassapaate import EDULLINEN
from kassapaate import MAUKAS
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti_pieni = Maksukortti(100)

    def test_luodun_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myydyt_oikein(self):
        myydyt = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(myydyt, 0)

    def test_edullinen_osto_kateisella_oikea_rahamaara_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + EDULLINEN)

    def test_edullinen_osto_kateisella_vaihtoraha_oikea(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 1000 - EDULLINEN)

    def test_edullinen_osto_kateisella_myytyjen_maara_kasvaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_osto_kateisella_ei_riittavasti_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_osto_kateisella_ei_riittavasti_rahaa_vaihtoraha_oikea(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    def test_edullinen_osto_kateisella_ei_riittavasti_rahaa_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_osto_kateisella_oikea_rahamaara_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + MAUKAS)

    def test_maukas_osto_kateisella_vaihtoraha_oikea(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 1000 - MAUKAS)

    def test_maukas_osto_kateisella_myytyjen_maara_kasvaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_osto_kateisella_ei_riittavasti_rahaa_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_osto_kateisella_ei_riittavasti_rahaa_vaihtoraha_oikea(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    def test_maukas_osto_kateisella_ei_riittavasti_rahaa_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_osto_kortilla_saldo_vahenee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000 - EDULLINEN)

    def test_edullinen_osto_kortilla_palauttaa_true(self):
        status = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(status, True)
        
    def test_edullinen_osto_kortilla_lounasmaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_osto_kortilla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_osto_kortilla_ei_riittavasti_rahaa_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_pieni)
        self.assertEqual(self.maksukortti_pieni.saldo, 100)

    def test_edullinen_osto_kortilla_ei_riittavasti_rahaa_palauttaa_false(self):
        status = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_pieni)
        self.assertEqual(status, False)
        
    def test_edullinen_osto_kortilla_ei_riitavasti_rahaa_lounasmaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_pieni)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_osto_kortilla_saldo_vahenee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000 - MAUKAS)

    def test_maukas_osto_kortilla_palauttaa_true(self):
        status = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(status, True)
        
    def test_maukas_osto_kortilla_lounasmaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_osto_kortilla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_osto_kortilla_ei_riittavasti_rahaa_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_pieni)
        self.assertEqual(self.maksukortti_pieni.saldo, 100)

    def test_maukas_osto_kortilla_ei_riittavasti_rahaa_palauttaa_false(self):
        status = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_pieni)
        self.assertEqual(status, False)
        
    def test_maukas_osto_kortilla_ei_riitavasti_rahaa_lounasmaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_pieni)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahan_lataus_kortille_muuttaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_rahan_lataus_kortille_muuttaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_negatiivisen_rahan_lataus_kortille_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_negatiivisen_rahan_lataus_kortille_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    

    
