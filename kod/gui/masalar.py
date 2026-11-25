"""Masalar ekranı: salondaki masaların listesi ve ekle / güncelle / sil işlemleri.

Görünüm ve davranış KayitEkrani şablonundan gelir. Bu dosyaya yalnızca şunlar yazılır:
  - SUTUNLAR ve ALANLAR: Masa sınıfının bilgilerine göre
  - kayitlari_getir, kayit_ekle, kayit_guncelle, kayit_sil: Masa sınıfını ve VeriTabani
    metotlarını çağıran dört bağlantı metodu
Bunlar, Masa sınıfının sahibi metot adlarını CLAUDE.md'deki sözleşme tablosuna yazınca doldurulur.
O zamana kadar ekran "back end bekleniyor" uyarısı gösterir.
"""

from gui.kayit_ekrani import KayitEkrani


class MasalarEkrani(KayitEkrani):
    baslik = "Masalar"
    aciklama = "Salondaki masalar ve anlık durumları."
    form_basligi = "Masa Bilgisi"
    bekleme_mesaji = "Masa sınıfı ve VeriTabani'ndaki masa metotları henüz yazılmadı."

    # Masa sınıfına göre doldurulacak:
    SUTUNLAR = []
    ALANLAR = []
    # Durumu renkli göstermek için (sınıfta böyle bir bilgi varsa):
    # durum_sutunu = "..."
    # DURUM_RENKLERI = {"...": RENKLER["basari"], ...}
