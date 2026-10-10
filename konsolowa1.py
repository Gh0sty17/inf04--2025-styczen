import unittest


class SzyfrCezara:
    def __init__(self, tekst_jawny: str = "", klucz: int = 0):
        self.tekst_jawny: str = tekst_jawny
        self.klucz: int = klucz

    def szyfruj(self, tekst_jawny: str = None, klucz: int = None) -> str:
        tekst = self.tekst_jawny if tekst_jawny is None else tekst_jawny
        k = self.klucz if klucz is None else klucz

        zaszyfrowane_znaki = []

        for znak in tekst:
            if znak == " ":
                zaszyfrowane_znaki.append(" ")
            elif "a" <= znak <= "z":
                kod_przesuniety = (ord(znak) - ord("a") + k) % 26 + ord("a")
                zaszyfrowane_znaki.append(chr(kod_przesuniety))
            else:
                zaszyfrowane_znaki.append(znak)

        return "".join(zaszyfrowane_znaki)


class TestSzyfrCezara(unittest.TestCase):
    def setUp(self):
        self.szyfrator = SzyfrCezara()

    def test_szyfruj_danePodstawoweKluczDodatni_zwracaZaszyfrowanyTekst(self):
        tekst_jawny = "abc"
        klucz = 3
        oczekiwany_wynik = "def"
        wynik = self.szyfrator.szyfruj(tekst_jawny, klucz)
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_szyfruj_zawijanieAlfabetu_zwracaZaszyfrowanyTekst(self):
        tekst_jawny = "xyz"
        klucz = 3
        oczekiwany_wynik = "abc"
        wynik = self.szyfrator.szyfruj(tekst_jawny, klucz)
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_szyfruj_kluczUjemnyDeszyfrowanie_zwracaZaszyfrowanyTekst(self):
        tekst_jawny = "def"
        klucz = -3
        oczekiwany_wynik = "abc"
        wynik = self.szyfrator.szyfruj(tekst_jawny, klucz)
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_szyfruj_kluczWiekszyNizDlugoscAlfabetu_zwracaZaszyfrowanyTekst(self):
        tekst_jawny = "abc"
        klucz = 29
        oczekiwany_wynik = "def"
        wynik = self.szyfrator.szyfruj(tekst_jawny, klucz)
        self.assertEqual(wynik, oczekiwany_wynik)

    def test_szyfruj_kluczZeroOrazSpacje_zwracaNiezmienionyTekst(self):
        tekst_jawny = "ala ma kota"
        klucz = 0
        oczekiwany_wynik = "ala ma kota"
        wynik = self.szyfrator.szyfruj(tekst_jawny, klucz)
        self.assertEqual(wynik, oczekiwany_wynik)


def main():
    print("=" * 45)
    print("   PROGRAM SZYFRUJĄCY – SZYFR CEZARA")
    print("=" * 45)

    tekst_jawny = input("Podaj tekst jawny do zaszyfrowania: ")

    while True:
        try:
            klucz = int(input("Podaj klucz szyfrowania (liczba całkowita): "))
            break
        except ValueError:
            print("Błąd: Klucz musi być liczbą całkowitą! Spróbuj ponownie.")

    instancja_szyfru = SzyfrCezara(tekst_jawny, klucz)
    tekst_zaszyfrowany = instancja_szyfru.szyfruj()

    print("-" * 45)
    print(f"Tekst jawny:        {tekst_jawny}")
    print(f"Klucz:              {klucz}")
    print(f"Tekst zaszyfrowany: {tekst_zaszyfrowany}")
    print("=" * 45)


if __name__ == "__main__":
    main()
    print("\nUruchamianie testów jednostkowych...")
    unittest.main(argv=[""], exit=False)