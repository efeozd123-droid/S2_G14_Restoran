"""Tüm ekranların türediği taban sınıf: başlık, açıklama ve bağlantı uyarısı."""

import customtkinter as ctk

from gui.tema import RENKLER, yazi


class Sayfa(ctk.CTkFrame):
    """Ana penceredeki içerik alanına yerleşen ekran.

    Alt sınıflar `icerigi_olustur()` metodunu doldurur ve `self.govde` içine yerleşir.
    `self.vt` VeriTabani nesnesidir; veri tabanı yoksa None'dır ("bağlantısız" mod).
    """

    baslik = "Sayfa"
    aciklama = ""

    def __init__(self, master, uygulama):
        super().__init__(master, fg_color=RENKLER["arka_plan"], corner_radius=0)
        self.uygulama = uygulama
        self.vt = uygulama.vt

        ust = ctk.CTkFrame(self, fg_color="transparent")
        ust.pack(fill="x", padx=28, pady=(24, 4))
        ctk.CTkLabel(ust, text=self.baslik, font=yazi(24, True), text_color=RENKLER["yazi"],
                     anchor="w").pack(fill="x")
        if self.aciklama:
            ctk.CTkLabel(ust, text=self.aciklama, font=yazi(13),
                         text_color=RENKLER["soluk_yazi"], anchor="w",
                         justify="left").pack(fill="x", pady=(2, 0))

        if self.vt is None:
            self._baglanti_uyarisi()

        self.govde = ctk.CTkFrame(self, fg_color="transparent")
        self.govde.pack(fill="both", expand=True, padx=28, pady=(12, 24))
        self.icerigi_olustur()

    def _baglanti_uyarisi(self):
        kutu = ctk.CTkFrame(self, fg_color=RENKLER["uyari_zemin"], corner_radius=8,
                            border_width=1, border_color=RENKLER["uyari"])
        kutu.pack(fill="x", padx=28, pady=(10, 0))
        metin = ("Veri tabanı bağlantısı yok: kod/veritabani.py henüz yazılmadı ya da açılamadı. "
                 "Ekranlar görüntülenir ancak kayıt işlemleri yapılamaz.")
        if self.uygulama.baglanti_hatasi:
            metin += f"\nAyrıntı: {self.uygulama.baglanti_hatasi}"
        ctk.CTkLabel(kutu, text=metin, font=yazi(12), text_color=RENKLER["yazi"],
                     anchor="w", justify="left", wraplength=900).pack(fill="x", padx=12, pady=8)

    def icerigi_olustur(self):
        """Alt sınıflar ekran içeriğini burada kurar."""
