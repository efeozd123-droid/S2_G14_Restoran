"""Back end metotları henüz hazır olmayan modüller için geçici ekran.

Modülün sınıfları ve VeriTabani metotları yazılınca bu sayfanın yerine gerçek ekran gelir
(bkz. ana_pencere.py içindeki MODULLER listesi).
"""

import customtkinter as ctk

from gui.sayfa import Sayfa
from gui.tema import RENKLER, yazi


class YapimAsamasinda(Sayfa):

    def __init__(self, master, uygulama, modul):
        self.modul = modul
        self.baslik = modul["baslik"]
        self.aciklama = modul["aciklama"]
        super().__init__(master, uygulama)

    def icerigi_olustur(self):
        kart = ctk.CTkFrame(self.govde, fg_color=RENKLER["kart"], corner_radius=12,
                            border_width=1, border_color=RENKLER["kenar"])
        kart.pack(fill="x", anchor="n")

        ctk.CTkLabel(kart, text="Bu ekranda olacaklar", font=yazi(15, True),
                     text_color=RENKLER["yazi"], anchor="w").pack(fill="x", padx=20, pady=(18, 6))
        for madde in self.modul["ozellikler"]:
            satir = ctk.CTkFrame(kart, fg_color="transparent")
            satir.pack(fill="x", padx=20, pady=2)
            ctk.CTkFrame(satir, width=8, height=8, corner_radius=4,
                         fg_color=RENKLER["vurgu"]).pack(side="left", padx=(2, 10))
            ctk.CTkLabel(satir, text=madde, font=yazi(13), text_color=RENKLER["yazi"],
                         anchor="w").pack(side="left", fill="x")

        durum = ctk.CTkFrame(kart, fg_color=RENKLER["tablo_cizgi"], corner_radius=8)
        durum.pack(fill="x", padx=20, pady=(16, 20))
        ctk.CTkLabel(durum, text="Durum: back end bekleniyor", font=yazi(13, True),
                     text_color=RENKLER["vurgu_koyu"], anchor="w").pack(fill="x", padx=14,
                                                                       pady=(10, 0))
        ctk.CTkLabel(durum,
                     text=("Bu modülün sınıfları ve VeriTabani metotları yazılıp CLAUDE.md'deki "
                           "\"Arayüz ↔ back end sözleşmesi\" tablosuna eklendiğinde ekran bağlanacak."),
                     font=yazi(12), text_color=RENKLER["soluk_yazi"], anchor="w",
                     justify="left", wraplength=820).pack(fill="x", padx=14, pady=(2, 10))
