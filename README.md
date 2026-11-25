# S2_G14_Restoran

MBP 207 Görsel Programlama — Dönem Sonu Projesi (S2 · G14)

Bir restoranın günlük işleyişini tek bir masaüstü uygulamasında yöneten Python projesi:
masalar, rezervasyonlar, sipariş takibi, menü, personel ve stok.

## Grup Üyeleri ve Görev Dağılımı

| Üye | GitHub | Sorumlu olduğu sınıflar | GUI ekranı |
|---|---|---|---|
| Efe Özdemir | [efeozd123-droid](https://github.com/efeozd123-droid) | | |
| Deniz Çetin | [dnzctnn](https://github.com/dnzctnn) | | |
| Ada Mısırlı | [adamisirli](https://github.com/adamisirli) | | |

## Projenin Amacı

Küçük ve orta ölçekli restoranlarda masa, rezervasyon, sipariş, menü, personel ve stok bilgileri
çoğunlukla kâğıt üzerinde ya da birbirinden kopuk tablolarda tutulur. Bu uygulama bu bilgileri tek
bir veri tabanında toplar ve her biri için ekle, listele, güncelle ve sil işlemlerini sunar.

| Modül | Ne yapar |
|---|---|
| Masalar | Salondaki masalar ve anlık durumları (boş, dolu, rezerve) |
| Rezervasyonlar | Müşteri rezervasyonlarının kaydı, masa ataması ve iptali |
| Siparişler | Masalardan alınan siparişler, hazırlık durumu ve hesap kapatma |
| Menü | Kategorilere göre yemek ve içecekler, fiyatlar |
| Stok | Mutfak malzemeleri, miktarlar ve kritik seviye uyarısı |
| Personel | Çalışanlar ve görevleri |

## Ekranlar

Uygulama sol tarafta bir menü ve sağda içerik alanından oluşur. Açılışta **Ana Panel** görünür
(dolu masa, bugünkü rezervasyon, açık sipariş ve kritik stok özetleri); menüden diğer modüllere geçilir.

## Kullanılan Teknolojiler

- **GUI modülü:** CustomTkinter
- **Veri tabanı:** SQLite (Python ile birlikte gelen `sqlite3` modülü; ek kurulum gerekmez)

## Kurulum ve Çalıştırma

1. Projeyi PyCharm'da açın.
2. `kod/requirements.txt` için PyCharm'ın önerdiği **Install requirements** uyarısını kabul edin.
3. `kod/main.py` dosyasını çalıştırın.

## GitHub Deposu

https://github.com/efeozd123-droid/2_14_Restraunt

## Yapay Zekâ Kullanım Beyanı

| Araç | Kullanıldığı dosya / iş |
|---|---|
| Claude | `README.md` şablonu ve proje açıklaması |
| Claude | `kod/main.py` ve `kod/gui/` klasörü: ana pencere, yan menü, ana panel, geçici modül ekranları, tema, ortak arayüz bileşenleri (tablo, form, bilgi kartı) |
| Claude | `TESLIM.md` (yönergeden çıkarılan teslim kontrol listesi), `CLAUDE.md` (YZ kullanım kuralları), `.gitignore` |
| — | Back end (`kod/modeller/`, `kod/veritabani.py`), veri tabanı (`veritabani.sql`), sınıf diyagramı: **YZ kullanılmadı** |

Öğretim elemanının 25.11.2026 tarihli kararı gereği YZ yalnızca README ve arayüz (GUI) için kullanılmıştır.

_(Proje ilerledikçe güncellenecek.)_
