"""Uygulamanın ana penceresi: soldaki menü ve sağdaki içerik alanı.

Yeni bir ekran bağlamak için MODULLER listesinde ilgili modülün "sinif" değerini
YapimAsamasinda yerine yeni ekran sınıfı yapmak yeterlidir.
"""

import customtkinter as ctk

from gui.ana_panel import AnaPanel
from gui.tema import RENKLER, temayi_uygula, yazi
from gui.yapim_asamasinda import YapimAsamasinda

MODULLER = [
    {"anahtar": "ana_panel", "baslik": "Ana Panel", "sinif": AnaPanel},
    {
        "anahtar": "masalar", "baslik": "Masalar", "sinif": None,
        "aciklama": "Salondaki masalar ve anlık durumları.",
        "ozellikler": ["Masa listesi ve durumu (boş, dolu, rezerve)",
                       "Masa ekleme, düzenleme ve silme",
                       "Masaya sipariş açma"],
    },
    {
        "anahtar": "rezervasyonlar", "baslik": "Rezervasyonlar", "sinif": None,
        "aciklama": "Müşteri rezervasyonlarının kaydı ve takibi.",
        "ozellikler": ["Tarihe göre rezervasyon listesi",
                       "Rezervasyon ekleme, güncelleme ve iptal",
                       "Rezervasyona masa atama"],
    },
    {
        "anahtar": "siparisler", "baslik": "Siparişler", "sinif": None,
        "aciklama": "Masalardan alınan siparişler ve hazırlık durumu.",
        "ozellikler": ["Açık ve kapanmış siparişlerin listesi",
                       "Siparişe menüden ürün ekleme ve çıkarma",
                       "Sipariş durumunu güncelleme ve hesabı kapatma"],
    },
    {
        "anahtar": "menu", "baslik": "Menü", "sinif": None,
        "aciklama": "Menüdeki yemek ve içecekler.",
        "ozellikler": ["Kategoriye göre ürün listesi",
                       "Ürün ekleme, fiyat güncelleme ve silme"],
    },
    {
        "anahtar": "stok", "baslik": "Stok", "sinif": None,
        "aciklama": "Mutfak malzemeleri ve stok seviyeleri.",
        "ozellikler": ["Malzeme listesi ve mevcut miktar",
                       "Malzeme ekleme, miktar güncelleme ve silme",
                       "Asgari seviyenin altındaki malzemeleri vurgulama"],
    },
    {
        "anahtar": "personel", "baslik": "Personel", "sinif": None,
        "aciklama": "Restoran çalışanları ve görevleri.",
        "ozellikler": ["Personel listesi ve görevleri",
                       "Personel ekleme, bilgi güncelleme ve silme"],
    },
]


class AnaPencere(ctk.CTk):

    def __init__(self, vt=None, baglanti_hatasi=None):
        temayi_uygula()
        super().__init__(fg_color=RENKLER["arka_plan"])
        self.vt = vt
        self.baglanti_hatasi = baglanti_hatasi
        self.moduller = MODULLER
        self.aktif_sayfa = None
        self.menu_dugmeleri = {}

        self.title("S2_G14 Restoran")
        self.geometry("1200x740")
        self.minsize(1000, 640)

        self._yan_menu_olustur()
        self.icerik = ctk.CTkFrame(self, fg_color=RENKLER["arka_plan"], corner_radius=0)
        self.icerik.pack(side="left", fill="both", expand=True)

        self.sayfa_ac("ana_panel")

    def _yan_menu_olustur(self):
        menu = ctk.CTkFrame(self, width=220, fg_color=RENKLER["yan_menu"], corner_radius=0)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        ctk.CTkLabel(menu, text="Restoran", font=yazi(22, True),
                     text_color=RENKLER["yan_menu_yazi"], anchor="w").pack(fill="x", padx=22,
                                                                           pady=(26, 0))
        ctk.CTkLabel(menu, text="Yönetim Sistemi", font=yazi(12),
                     text_color=RENKLER["yan_menu_soluk"], anchor="w").pack(fill="x", padx=22,
                                                                            pady=(0, 22))

        for modul in self.moduller:
            dugme = ctk.CTkButton(menu, text=modul["baslik"], anchor="w", height=40,
                                  corner_radius=8, font=yazi(14),
                                  fg_color="transparent", text_color=RENKLER["yan_menu_yazi"],
                                  hover_color=RENKLER["yan_menu_secili"],
                                  command=lambda a=modul["anahtar"]: self.sayfa_ac(a))
            dugme.pack(fill="x", padx=12, pady=2)
            self.menu_dugmeleri[modul["anahtar"]] = dugme

        durum = "Veri tabanı bağlı" if self.vt is not None else "Veri tabanı bağlı değil"
        renk = RENKLER["basari"] if self.vt is not None else RENKLER["uyari"]
        alt = ctk.CTkFrame(menu, fg_color="transparent")
        alt.pack(side="bottom", fill="x", padx=22, pady=18)
        ctk.CTkFrame(alt, width=8, height=8, corner_radius=4,
                     fg_color=renk).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(alt, text=durum, font=yazi(11), text_color=RENKLER["yan_menu_soluk"],
                     anchor="w").pack(side="left")

    def sayfa_ac(self, anahtar):
        """Menüden seçilen ekranı açar. Ekran her açılışta yeniden kurulur, veriler tazelenir."""
        modul = next(m for m in self.moduller if m["anahtar"] == anahtar)

        if self.aktif_sayfa is not None:
            self.aktif_sayfa.destroy()

        if modul["sinif"] is None:
            self.aktif_sayfa = YapimAsamasinda(self.icerik, self, modul)
        else:
            self.aktif_sayfa = modul["sinif"](self.icerik, self)
        self.aktif_sayfa.pack(fill="both", expand=True)

        for a, dugme in self.menu_dugmeleri.items():
            secili = a == anahtar
            dugme.configure(
                fg_color=RENKLER["vurgu"] if secili else "transparent",
                hover_color=RENKLER["vurgu_koyu"] if secili else RENKLER["yan_menu_secili"],
                font=yazi(14, secili),
            )
