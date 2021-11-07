import unittest
from maksukortti import Maksukortti
from maksukortti import EDULLINEN
from maksukortti import MAUKAS

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        vastaus = str(self.kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_negatiivisen_summan_lataaminen_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-10)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_voi_syoda_edullisesti_kun_saldoa_jaljella_lounaan_verran(self):
        kortti = Maksukortti(EDULLINEN)
        kortti.syo_edullisesti()
        self.assertAlmostEqual(kortti.arvo, 0)

    def test_voi_syoda_maukkaasti_kun_saldoa_jaljella_lounaan_verran(self):
        kortti = Maksukortti(MAUKAS)
        kortti.syo_maukkaasti()
        self.assertAlmostEqual(kortti.arvo, 0)