"""Liste + form düzeninde, dört CRUD işlemini yapan ortak ekran şablonu.

Her modül ekranı (Masalar, Personel, Menü...) bu sınıftan türetilir ve yalnızca şunları verir:
  - SUTUNLAR: tabloda görünen sütunlar [("anahtar", "Başlık", genişlik), ...]; ilk sütun kaydın kimliği
  - ALANLAR:  formdaki alanlar (FormPaneli biçimi); anahtarları SUTUNLAR'dakilerle eşleşir
  - dört bağlantı metodu: kayitlari_getir, kayit_ekle, kayit_guncelle, kayit_sil
Bağlantı metotları öğrencilerin yazdığı model sınıflarını ve VeriTabani metotlarını çağırır.
Bu dosyada iş mantığı ve SQL yoktur.
"""

import sqlite3

import customtkinter as ctk

from gui.bilesenler import (FormPaneli, Tablo, ana_dugme, bilgi_goster, hata_goster,
                            ikincil_dugme, onay_al, tehlike_dugme)
from gui.sayfa import Sayfa
from gui.tema import RENKLER, yazi


class KayitEkrani(Sayfa):
    form_basligi = "Kayıt Bilgisi"
    SUTUNLAR = []
    ALANLAR = []
    durum_sutunu = None          # renkli gösterilecek sütunun anahtarı (isteğe bağlı)
    DURUM_RENKLERI = {}          # {"Boş": "#3F7D58", ...}
    bekleme_mesaji = "Bu modülün sınıfları ve VeriTabani metotları henüz yazılmadı."

    # ------------------------------------------------ alt sınıfın dolduracağı bağlantı metotları

    def kayitlari_getir(self):
        """Tablo satırlarını döner: [(kimlik, ...SUTUNLAR sırasıyla), ...]"""
        raise NotImplementedError

    def kayit_ekle(self, degerler):
        """degerler: form alanları {anahtar: metin veya None}"""
        raise NotImplementedError

    def kayit_guncelle(self, kimlik, degerler):
        """kimlik tablodan gelir ve METİN'dir (ör. "3"); gerekirse int(kimlik) ile çevrilir."""
        raise NotImplementedError

    def kayit_sil(self, kimlik):
        """kimlik METİN'dir (ör. "3")."""
        raise NotImplementedError

    # ------------------------------------------------ ekran kurulumu

    def icerigi_olustur(self):
        self.secili_kimlik = None
        self._tum_satirlar = []
        self.bekliyor = not self.SUTUNLAR

        if not self.bekliyor and self.vt is not None:
            try:
                self._tum_satirlar = list(self.kayitlari_getir())
            except NotImplementedError:
                self.bekliyor = True
            except Exception as hata:
                hata_goster(f"Kayıtlar yüklenemedi:\n{hata}")

        if self.bekliyor:
            self._bekleme_karti()
            return

        self.govde.grid_columnconfigure(0, weight=1)
        self.govde.grid_rowconfigure(0, weight=1)
        self._liste_bolumu().grid(row=0, column=0, sticky="nsew", padx=(0, 16))
        self._form_bolumu().grid(row=0, column=1, sticky="ns")
        self.aramayi_uygula()

    def _liste_bolumu(self):
        bolum = ctk.CTkFrame(self.govde, fg_color="transparent")
        ust = ctk.CTkFrame(bolum, fg_color="transparent")
        ust.pack(fill="x", pady=(0, 10))
        self.arama = ctk.CTkEntry(ust, placeholder_text="Ara...", width=280, height=36,
                                  border_color=RENKLER["kenar"])
        self.arama.pack(side="left")
        self.arama.bind("<KeyRelease>", lambda _olay: self.aramayi_uygula())
        self.sayac = ctk.CTkLabel(ust, text="", font=yazi(12), text_color=RENKLER["soluk_yazi"])
        self.sayac.pack(side="right")

        self.tablo = Tablo(bolum, self.SUTUNLAR, yukseklik=14)
        self.tablo.pack(fill="both", expand=True)
        for durum, renk in self.DURUM_RENKLERI.items():
            self.tablo.renk_etiketi(f"durum_{durum}", renk)
        self.tablo.secim_degisince(self._secim_degisti)
        return bolum

    def _form_bolumu(self):
        kart = ctk.CTkFrame(self.govde, width=320, fg_color=RENKLER["kart"], corner_radius=12,
                            border_width=1, border_color=RENKLER["kenar"])
        ctk.CTkLabel(kart, text=self.form_basligi, font=yazi(16, True),
                     text_color=RENKLER["yazi"], anchor="w").pack(fill="x", padx=20, pady=(18, 0))
        self.mod_etiketi = ctk.CTkLabel(kart, text="", font=yazi(12),
                                        text_color=RENKLER["soluk_yazi"], anchor="w")
        self.mod_etiketi.pack(fill="x", padx=20)

        self.form = FormPaneli(kart, self.ALANLAR, width=280)
        self.form.pack(fill="x", padx=20, pady=(6, 16))

        ana_dugme(kart, "Kaydet", self.kaydet).pack(fill="x", padx=20, pady=(0, 8))
        ikincil_dugme(kart, "Yeni kayıt", self.yeni).pack(fill="x", padx=20, pady=(0, 8))
        tehlike_dugme(kart, "Sil", self.sil).pack(fill="x", padx=20, pady=(0, 18))
        self._modu_goster()
        return kart

    def _bekleme_karti(self):
        kart = ctk.CTkFrame(self.govde, fg_color=RENKLER["kart"], corner_radius=12,
                            border_width=1, border_color=RENKLER["kenar"])
        kart.pack(fill="x", anchor="n")
        ctk.CTkLabel(kart, text="Durum: back end bekleniyor", font=yazi(15, True),
                     text_color=RENKLER["vurgu_koyu"], anchor="w").pack(fill="x", padx=20,
                                                                       pady=(18, 4))
        ctk.CTkLabel(kart, text=self.bekleme_mesaji, font=yazi(13), text_color=RENKLER["yazi"],
                     anchor="w", justify="left", wraplength=820).pack(fill="x", padx=20)
        ctk.CTkLabel(kart,
                     text=("Sınıf sahibi metot adlarını CLAUDE.md'deki \"Arayüz ↔ back end "
                           "sözleşmesi\" tablosuna yazınca bu ekran liste ve formla açılacak."),
                     font=yazi(12), text_color=RENKLER["soluk_yazi"], anchor="w",
                     justify="left", wraplength=820).pack(fill="x", padx=20, pady=(6, 18))

    # ------------------------------------------------ liste

    def listeyi_yenile(self):
        try:
            self._tum_satirlar = list(self.kayitlari_getir())
        except Exception as hata:
            hata_goster(f"Kayıtlar yüklenemedi:\n{hata}")
            self._tum_satirlar = []
        self.aramayi_uygula()

    def aramayi_uygula(self):
        metin = self.arama.get().strip().lower()
        if metin:
            satirlar = [s for s in self._tum_satirlar
                        if any(metin in str(d).lower() for d in s if d is not None)]
        else:
            satirlar = list(self._tum_satirlar)

        etiketler = None
        if self.durum_sutunu:
            sira = self._sutun_sirasi(self.durum_sutunu)
            etiketler = [(f"durum_{s[sira]}",) for s in satirlar]
        self.tablo.doldur(satirlar, etiketler)

        toplam = len(self._tum_satirlar)
        self.sayac.configure(text=f"{len(satirlar)} / {toplam} kayıt" if metin else f"{toplam} kayıt")

        # Düzenlenmekte olan kayıt hâlâ listedeyse seçili kalır (form korunur);
        # süzgeç dışında kaldıysa seçim ve form temizlenir. Aksi hâlde Kaydet kopya kayıt ekler.
        if self.secili_kimlik is not None:
            agac = self.tablo.agac
            eslesen = [i for i in agac.get_children()
                       if str(agac.item(i, "values")[0]) == self.secili_kimlik]
            if eslesen:
                agac.selection_set(eslesen[0])
            else:
                self.secili_kimlik = None
                self.form.temizle()
        self._modu_goster()

    def _sutun_sirasi(self, anahtar):
        return [s[0] for s in self.SUTUNLAR].index(anahtar)

    def _secim_degisti(self):
        satir = self.tablo.secili()
        if satir is None:
            self.secili_kimlik = None
        elif satir[0] != self.secili_kimlik:
            # Yalnızca başka bir kayda geçilince form doldurulur; aynı kayıt yeniden
            # seçildiğinde (ör. arama sonrası) kullanıcının düzenlemeleri silinmez.
            self.secili_kimlik = satir[0]
            self.form.temizle()
            degerler = {}
            for alan in self.ALANLAR:
                anahtar = alan[0]
                if anahtar in [s[0] for s in self.SUTUNLAR]:
                    degerler[anahtar] = satir[self._sutun_sirasi(anahtar)]
            self.form.doldur(degerler)
        self._modu_goster()

    def _modu_goster(self):
        if self.secili_kimlik is None:
            self.mod_etiketi.configure(text="Yeni kayıt ekleniyor")
        else:
            baslik = self.SUTUNLAR[0][1]
            self.mod_etiketi.configure(text=f"Seçili kayıt düzenleniyor ({baslik}: {self.secili_kimlik})")

    # ------------------------------------------------ işlemler

    def yeni(self):
        self.tablo.agac.selection_remove(self.tablo.agac.selection())
        self.secili_kimlik = None
        self.form.temizle()
        self._modu_goster()

    def _baglanti_var_mi(self):
        if self.vt is None:
            hata_goster("Veri tabanı bağlı değil; kayıt işlemi yapılamaz.")
            return False
        return True

    def _islem_yap(self, islem):
        """Back end çağrısını yapar; hatayı mesaj kutusunda gösterir. Başarılıysa True döner."""
        try:
            islem()
        except NotImplementedError:
            hata_goster("Bu işlem için back end metodu henüz yazılmadı.")
        except ValueError as hata:
            hata_goster(hata, "Geçersiz giriş")
        except sqlite3.Error as hata:
            hata_goster(f"Veri tabanı hatası:\n{hata}")
        except Exception as hata:
            hata_goster(f"Beklenmeyen hata:\n{hata}")
        else:
            return True
        return False

    def kaydet(self):
        if not self._baglanti_var_mi():
            return
        degerler = self.form.degerler()
        kimlik = self.secili_kimlik
        if kimlik is None:
            basarili = self._islem_yap(lambda: self.kayit_ekle(degerler))
        else:
            basarili = self._islem_yap(lambda: self.kayit_guncelle(kimlik, degerler))
        if basarili:
            self.listeyi_yenile()
            self.yeni()

    def sil(self):
        if not self._baglanti_var_mi():
            return
        kimlik = self.secili_kimlik
        if kimlik is None:
            bilgi_goster("Silmek için önce listeden bir kayıt seçin.")
            return
        if not onay_al(f"Seçili kayıt ({self.SUTUNLAR[0][1]}: {kimlik}) silinsin mi?\n"
                       "Bu işlem geri alınamaz."):
            return
        if self._islem_yap(lambda: self.kayit_sil(kimlik)):
            self.listeyi_yenile()
            self.yeni()
