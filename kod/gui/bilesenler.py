"""Ekranlarda tekrar kullanılan arayüz parçaları: tablo, form, bilgi kartı ve mesaj kutuları.

Bu dosyada iş mantığı ve SQL yoktur; yalnızca görünüm ve kullanıcı etkileşimi vardır.
"""

from tkinter import messagebox, ttk

import customtkinter as ctk

from gui.tema import RENKLER, yazi


# ---------------------------------------------------------------- mesajlar

def hata_goster(mesaj, baslik="Hata"):
    messagebox.showerror(baslik, str(mesaj))


def bilgi_goster(mesaj, baslik="Bilgi"):
    messagebox.showinfo(baslik, str(mesaj))


def onay_al(mesaj, baslik="Onay"):
    """Kullanıcı 'Evet' derse True döner (silme gibi geri alınamayan işlemlerden önce)."""
    return messagebox.askyesno(baslik, mesaj)


# ---------------------------------------------------------------- tablo

class Tablo(ctk.CTkFrame):
    """Kaydırılabilir liste tablosu (ttk.Treeview).

    sutunlar: [("anahtar", "Başlık", genişlik), ...]
    Satırlar demet veya liste olarak verilir; sıra sütunlarla aynıdır.
    """

    _stil_hazir = False

    def __init__(self, master, sutunlar, yukseklik=12, **kwargs):
        super().__init__(master, fg_color=RENKLER["kart"], corner_radius=10,
                         border_width=1, border_color=RENKLER["kenar"], **kwargs)
        Tablo._stili_hazirla()

        self.sutunlar = sutunlar
        anahtarlar = [s[0] for s in sutunlar]
        self.agac = ttk.Treeview(self, columns=anahtarlar, show="headings",
                                 height=yukseklik, style="Restoran.Treeview",
                                 selectmode="browse")
        for anahtar, baslik, genislik in sutunlar:
            self.agac.heading(anahtar, text=baslik, anchor="w")
            self.agac.column(anahtar, width=genislik, minwidth=60, anchor="w")
        self.agac.tag_configure("cift", background=RENKLER["tablo_cizgi"])

        kaydirma = ctk.CTkScrollbar(self, command=self.agac.yview)
        self.agac.configure(yscrollcommand=kaydirma.set)

        self.agac.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)
        kaydirma.grid(row=0, column=1, sticky="ns", padx=(0, 4), pady=8)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    @classmethod
    def _stili_hazirla(cls):
        if cls._stil_hazir:
            return
        stil = ttk.Style()
        stil.theme_use("clam")
        stil.configure("Restoran.Treeview", background=RENKLER["kart"],
                       fieldbackground=RENKLER["kart"], foreground=RENKLER["yazi"],
                       rowheight=30, borderwidth=0, font=("TkDefaultFont", 11))
        stil.configure("Restoran.Treeview.Heading", background=RENKLER["tablo_baslik"],
                       foreground=RENKLER["yazi"], relief="flat", padding=(6, 6),
                       font=("TkDefaultFont", 11, "bold"))
        stil.map("Restoran.Treeview",
                 background=[("selected", RENKLER["tablo_secili"])],
                 foreground=[("selected", RENKLER["yazi"])])
        stil.map("Restoran.Treeview.Heading",
                 background=[("active", RENKLER["kenar"])])
        cls._stil_hazir = True

    def doldur(self, satirlar, etiketler=None):
        """Tabloyu temizleyip verilen satırlarla doldurur. None değerler boş gösterilir.

        etiketler: her satır için ek Treeview etiketleri (örn. durum rengi), isteğe bağlı.
        """
        self.temizle()
        for sira, satir in enumerate(satirlar):
            degerler = ["" if d is None else d for d in satir]
            etiket = ("cift",) if sira % 2 else ()
            if etiketler:
                etiket = etiket + tuple(etiketler[sira])
            self.agac.insert("", "end", values=degerler, tags=etiket)

    def renk_etiketi(self, etiket, yazi_rengi):
        """Bir etikete sahip satırların yazı rengini ayarlar."""
        self.agac.tag_configure(etiket, foreground=yazi_rengi)

    def temizle(self):
        self.agac.delete(*self.agac.get_children())

    def secili(self):
        """Seçili satırın değerlerini metin demeti olarak döner; seçim yoksa None."""
        secim = self.agac.selection()
        if not secim:
            return None
        return tuple(str(d) for d in self.agac.item(secim[0], "values"))

    def secim_degisince(self, fonksiyon):
        self.agac.bind("<<TreeviewSelect>>", lambda _olay: fonksiyon())


# ---------------------------------------------------------------- form

class FormPaneli(ctk.CTkFrame):
    """Etiketli giriş alanlarından oluşan form.

    alanlar: [("anahtar", "Etiket"), ...] veya seçim kutusu için
             [("anahtar", "Etiket", ["Seçenek 1", "Seçenek 2"]), ...]
    degerler() boş alanları None olarak döner; doğrulama model sınıfındadır.
    """

    def __init__(self, master, alanlar, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.girdiler = {}
        for sira, alan in enumerate(alanlar):
            anahtar, etiket = alan[0], alan[1]
            ctk.CTkLabel(self, text=etiket, font=yazi(12), text_color=RENKLER["soluk_yazi"],
                         anchor="w").grid(row=sira * 2, column=0, sticky="w", pady=(6, 0))
            if len(alan) > 2:
                girdi = ctk.CTkComboBox(self, values=list(alan[2]), state="readonly",
                                        border_color=RENKLER["kenar"],
                                        button_color=RENKLER["vurgu"],
                                        button_hover_color=RENKLER["vurgu_koyu"])
                girdi.set("")
            else:
                girdi = ctk.CTkEntry(self, border_color=RENKLER["kenar"])
            girdi.grid(row=sira * 2 + 1, column=0, sticky="ew")
            self.girdiler[anahtar] = girdi
        self.grid_columnconfigure(0, weight=1)

    def degerler(self):
        sonuc = {}
        for anahtar, girdi in self.girdiler.items():
            metin = girdi.get().strip()
            sonuc[anahtar] = metin if metin else None
        return sonuc

    def doldur(self, degerler):
        for anahtar, deger in degerler.items():
            if anahtar not in self.girdiler:
                continue
            girdi = self.girdiler[anahtar]
            metin = "" if deger is None else str(deger)
            if isinstance(girdi, ctk.CTkComboBox):
                girdi.set(metin)
            else:
                girdi.delete(0, "end")
                girdi.insert(0, metin)

    def temizle(self):
        self.doldur({anahtar: None for anahtar in self.girdiler})


# ---------------------------------------------------------------- kartlar ve düğmeler

class BilgiKarti(ctk.CTkFrame):
    """Ana paneldeki sayı kartı (örn. 'Dolu masa: 5')."""

    def __init__(self, master, baslik, deger="—", aciklama="", renk=None, **kwargs):
        super().__init__(master, fg_color=RENKLER["kart"], corner_radius=12,
                         border_width=1, border_color=RENKLER["kenar"], **kwargs)
        ctk.CTkFrame(self, width=4, height=1, fg_color=renk or RENKLER["vurgu"],
                     corner_radius=2).pack(side="left", fill="y", padx=(10, 0), pady=14)
        icerik = ctk.CTkFrame(self, fg_color="transparent")
        icerik.pack(side="left", fill="both", expand=True, padx=14, pady=12)
        ctk.CTkLabel(icerik, text=baslik, font=yazi(12), text_color=RENKLER["soluk_yazi"],
                     anchor="w").pack(fill="x")
        self.deger_etiketi = ctk.CTkLabel(icerik, text=str(deger), font=yazi(28, True),
                                          text_color=RENKLER["yazi"], anchor="w")
        self.deger_etiketi.pack(fill="x")
        if aciklama:
            ctk.CTkLabel(icerik, text=aciklama, font=yazi(11), text_color=RENKLER["soluk_yazi"],
                         anchor="w").pack(fill="x")

    def guncelle(self, deger):
        self.deger_etiketi.configure(text=str(deger))


def ana_dugme(master, metin, komut, **kwargs):
    return ctk.CTkButton(master, text=metin, command=komut, fg_color=RENKLER["vurgu"],
                         hover_color=RENKLER["vurgu_koyu"], font=yazi(13, True),
                         height=36, corner_radius=8, **kwargs)


def ikincil_dugme(master, metin, komut, **kwargs):
    return ctk.CTkButton(master, text=metin, command=komut, fg_color="transparent",
                         border_width=1, border_color=RENKLER["kenar"],
                         text_color=RENKLER["yazi"], hover_color=RENKLER["tablo_baslik"],
                         font=yazi(13), height=36, corner_radius=8, **kwargs)


def tehlike_dugme(master, metin, komut, **kwargs):
    return ctk.CTkButton(master, text=metin, command=komut, fg_color=RENKLER["tehlike"],
                         hover_color=RENKLER["tehlike_koyu"], font=yazi(13, True),
                         height=36, corner_radius=8, **kwargs)
