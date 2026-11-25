# Teslim Kontrol Listesi — S2_G14

Son teslim: **21 Aralık 2026 Pazar, 12.00** — ieüLearn → Dönem Sonu Projesi. Geç teslim kabul edilmez.
Zip'i grup adına **bir üye** yükler.

## Takvim

- [ ] **25 Kasım 2026 Çarşamba, 12.00** — ieüLearn'de grup seçimi; Google Sheet'e grup üyeleri
      (ad-soyad, section), proje adı, bir cümlelik açıklama ve GitHub depo bağlantısı
- [ ] **14 Aralık 2026 Pazar** — grup içi anlaşmazlık bildirimi için son gün
- [ ] **21 Aralık 2026 Pazar, 12.00** — zip teslimi
- [ ] Sunum tarihi duyurulacak

## Zip

- [ ] Ad: `S2_G14_<ProjeAdi>.zip` — Türkçe karakter ve boşluk yok (uyulmazsa −2)
- [ ] Zip son commit'ten oluşturuldu; teslimden sonra push yapılmayacak
- [ ] Zip başka bir bilgisayarda açılıp `kod/main.py` ile çalıştırılarak denendi

| # | Dosya / klasör | İçerik | Hazır |
|---|---|---|---|
| 1 | `kod/` | Tüm `.py` dosyaları, `main.py`, `requirements.txt`, `.db` dosyası — GitHub'daki son sürümle aynı | [ ] |
| 2 | `README.md` | Proje adı, üyeler ve görev dağılımı, amaç, kurulum, GUI modülü ve veri tabanı, GitHub bağlantısı, YZ Kullanım Beyanı | [ ] |
| 3 | `sinif_diyagrami.pdf` / `.png` | UML: tüm sınıflar, özellikler, metotlar, ilişkiler (kalıtım, ilişkilendirme) — kodla birebir | [ ] |
| 4 | `ekran_goruntuleri.pdf` | Her ekranın görüntüsü, altında bir cümle açıklama | [ ] |
| 5 | `veritabani.sql` | `CREATE TABLE`, örnek `INSERT`, uygulamanın kullandığı temel sorgular (isteğe bağlı ER diyagramı) | [ ] |
| 6 | `sunum.pdf` / `.pptx` | Ders sunumu | [ ] |
| 7 | `commit_gecmisi.pdf` | Commits sayfası (tüm sayfalar) + Insights → Contributors, teslim günü alınmış (Ek A.8) | [ ] |

Eksik her dosya: −5 (ilgili rubrik kaleminden ayrıca). `requirements.txt` eksik veya proje belirtilen
adımlarla çalışmıyor: −5.

## Asgari teknik şartlar (grup projesi)

- [ ] En az 5 sınıf (GUI hariç)
- [ ] En az 1 kalıtım ilişkisi
- [ ] Her sınıfta `__init__`; en az bir sınıfta `@property` veya getter/setter
- [ ] Tüm SQL tek bir `VeriTabani` sınıfında
- [ ] En az 3 tablo, en az 1 foreign key
- [ ] Ekle, listele, güncelle, sil — dördü de arayüzden
- [ ] En az 3 pencere/sekme
- [ ] Girişlerde doğrulama ve `try/except`
- [ ] GUI, model ve veri tabanı ayrı `.py` dosyalarında

## GitHub

- [ ] Depo **public**
- [ ] Üç üye de collaborator ve her biri kendi hesabından commit atıyor
- [ ] Commit mesajları açıklayıcı, gelişim haftalara yayılmış
- [ ] Her üyenin en az bir iş mantığı sınıfı kendi commit'lerinde
- [ ] Depo bağlantısı ve her üyenin GitHub kullanıcı adı README'de ve Google Sheet'te
- [ ] Depo en az dönem sonuna kadar silinmeyecek
