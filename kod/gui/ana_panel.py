"""Uygulama açıldığında görünen özet ekranı."""

import customtkinter as ctk

from gui.bilesenler import BilgiKarti, ikincil_dugme
from gui.sayfa import Sayfa
from gui.tema import RENKLER, yazi


class AnaPanel(Sayfa):
    baslik = "Ana Panel"
    aciklama = "Restoranın bugünkü durumu ve modüllere hızlı erişim."

    def icerigi_olustur(self):
        kartlar = ctk.CTkFrame(self.govde, fg_color="transparent")
        kartlar.pack(fill="x")
        # Sayılar ilgili VeriTabani metotları yazılınca doldurulacak; şimdilik "—".
        bilgiler = [
            ("Dolu masa", "Şu an servis verilen masalar", RENKLER["vurgu"]),
            ("Bugünkü rezervasyon", "Bugün için kayıtlı", RENKLER["basari"]),
            ("Açık sipariş", "Hazırlanan veya servis bekleyen", RENKLER["uyari"]),
            ("Kritik stok", "Asgari seviyenin altındaki ürünler", RENKLER["tehlike"]),
        ]
        self.kartlar = {}
        for sutun, (baslik, aciklama, renk) in enumerate(bilgiler):
            kart = BilgiKarti(kartlar, baslik, "—", aciklama, renk)
            kart.grid(row=0, column=sutun, sticky="nsew", padx=(0 if sutun == 0 else 12, 0))
            kartlar.grid_columnconfigure(sutun, weight=1, uniform="kart")
            self.kartlar[baslik] = kart

        ctk.CTkLabel(self.govde, text="Hızlı erişim", font=yazi(15, True),
                     text_color=RENKLER["yazi"], anchor="w").pack(fill="x", pady=(28, 8))
        dugmeler = ctk.CTkFrame(self.govde, fg_color="transparent")
        dugmeler.pack(fill="x")
        for sira, modul in enumerate(self.uygulama.moduller):
            if modul["anahtar"] == "ana_panel":
                continue
            dugme = ikincil_dugme(dugmeler, modul["baslik"],
                                  lambda a=modul["anahtar"]: self.uygulama.sayfa_ac(a))
            dugme.grid(row=0, column=sira, sticky="ew", padx=(0, 10))
            dugmeler.grid_columnconfigure(sira, weight=1, uniform="dugme")
