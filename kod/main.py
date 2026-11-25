"""Uygulamayı başlatır. PyCharm'da bu dosya çalıştırılır.

VeriTabani sınıfı (kod/veritabani.py) öğrenciler tarafından yazılır. Dosya henüz yoksa veya
bağlantı açılamazsa arayüz "bağlantısız" modda açılır.
"""

from gui.ana_pencere import AnaPencere


def veritabanina_baglan():
    """(vt, hata_metni) döner. Bağlantı yoksa vt None olur."""
    try:
        from veritabani import VeriTabani
    except ImportError:
        return None, None
    try:
        return VeriTabani(), None
    except Exception as hata:
        return None, hata


def main():
    vt, hata = veritabanina_baglan()
    pencere = AnaPencere(vt, hata)
    pencere.mainloop()


if __name__ == "__main__":
    main()
