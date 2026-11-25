# CLAUDE.md — S2_G14_Restoran (MBP 207 Dönem Sonu Projesi)

Bu dosya, bu depoda çalışan Claude (ve diğer YZ araçları) için kuralları ve proje bağlamını içerir.
Grubun 3 üyesi de bu dosyayı kullanır. **Önce "Yapay zekâ kuralları" bölümünü oku; bu bölüm her şeyden önce gelir.**
Kuralların kaynağı dersin yönergesidir: *MBP 207 Dönem Sonu Projesi — Yönerge ve Rubrik* (19 Kasım 2026).

## Proje

Restoranlar için Python masaüstü uygulaması. Modüller: **masa, rezervasyon, sipariş takibi, menü,
personel ve stok**. Sınıf ve tablo tasarımı öğrencilere aittir.

- Dil: Python 3 · GUI: **CustomTkinter** · Veri tabanı: **SQLite** (`sqlite3`, kurulum gerektirmez)
- PyCharm'da açılıp `kod/main.py` ile çalışmalı. Harici kütüphaneler `kod/requirements.txt` içinde.
- Grup: Section 2, Grup 14 (3 kişi) → **grup projesi** şartları geçerli.
- Son teslim: **21 Aralık 2026 Pazar 12.00**, ieüLearn → Dönem Sonu Projesi, tek zip.
  Zip adı: `S2_G14_<ProjeAdi>.zip` (Türkçe karakter ve boşluk yok). Geç teslim kabul edilmez.
- Depo: https://github.com/efeozd123-droid/2_14_Restraunt (public olmalı)

## Yapay zekâ kuralları (yönerge Bölüm 4 — kesin)

Back end'de YZ kullanımı yasaktır. Tespit edilirse OOP puanı (25) sıfırlanır ve akademik dürüstlük
süreci başlar.

**Öğretim elemanı kararı (25.11.2026):** Bu grupta YZ yalnızca **README ve GUI** için kullanılır.
**Veri tabanı ve diğer tüm kısımlar öğrencilere aittir.** Bu karar yönergedeki "SQL için ihtiyaç
hâlinde destek" iznini de kaldırır. Bu yüzden:

| Katman | Dosyalar | Claude ne yapabilir |
|---|---|---|
| **Back end: OOP iş mantığı** | `kod/modeller/**`, `kod/veritabani.py` | **YASAK.** Kod yazma, tamamlama, refactor, hata ayıklama yok; bu dosyaları açıp düzenleme. |
| **Veri tabanı (SQL, şema)** | `veritabani.sql`, tablo tasarımı, SQL sorgu metinleri | **YASAK.** Tablo, sütun, CREATE/SELECT/INSERT önerme veya yazma yok. |
| **Sınıf diyagramı, sunum** | `sinif_diyagrami.*`, `sunum.*` | **YASAK.** Öğrenciler hazırlar. |
| GUI | `kod/gui/**`, `kod/main.py` | Serbest. Tamamen yazılabilir. |
| README | `README.md` | Serbest. İçerik kodla uyumlu olmalı. |
| Çalışma düzeni dosyaları | `CLAUDE.md`, `TESLIM.md`, `.gitignore`, `kod/requirements.txt` | Yönergeyi aktaran kural/kontrol listesi; proje içeriği yazılmaz. |

- Yönerge back end için **hata ayıklamada da** YZ kullanımını yasaklar. Öğrencinin back end kodunu
  okuyup hatasını gösterme ("öğretmen modu") ancak dersin öğretim elemanı bunu bu grup için açıkça
  onaylarsa yapılır; onay alınırsa tarihiyle buraya yazılır. **Şu an onay yok.**
- Python/OOP kavramları (kalıtım, `@property`, try/except, parametreli sorgu…) yalnızca **projeden
  bağımsız, genel örneklerle** anlatılabilir. Proje sınıflarıyla aynı yapıda "örnek" yazarak dolaylı
  kod verilmez.
- `VeriTabani` sınıfı ve içindeki tüm SQL metinleri öğrencilere aittir.
- GUI bir model/`VeriTabani` metoduna ihtiyaç duyar ve metot yoksa: metodu **yazma**. Hangi isimde,
  hangi parametreyle, ne döndüren bir metot gerektiğini "Arayüz ↔ back end sözleşmesi" tablosuna
  ekle; sınıfın sahibi yazar. Ekranlar, metot henüz yazılmamışsa çökmeden "bağlantısız" çalışır.
- **Beyan:** README'deki "Yapay Zekâ Kullanım Beyanı" zorunludur. GUI veya README ürettiğinde
  bu bölüme hangi dosya / iş için kullanıldığını bir satırla ekle.

## Asgari şartlar (grup projesi, yönerge Bölüm 3)

- [ ] En az **5 sınıf** (kendi yazılan, GUI sınıfları hariç)
- [ ] En az **1 kalıtım** (ebeveyn–çocuk) ilişkisi
- [ ] Her sınıfta `__init__`; en az bir sınıfta `@property` veya getter/setter
- [ ] Tüm SQL işlemlerini toplayan ayrı bir `VeriTabani` sınıfı
- [ ] En az **3 tablo**, en az **1 foreign key**
- [ ] **CRUD**: ekle, listele, güncelle, sil — dördü de arayüzden
- [ ] En az **3 pencere/sekme**
- [ ] Kullanıcı girişlerinde doğrulama ve `try/except`

## Mimari

Katmanlar ayrı dosyalarda tutulur. **GUI içinde iş mantığı ve SQL olmaz.** GUI yalnızca model
sınıflarının ve `VeriTabani` sınıfının metotlarını çağırır.

```
kod/
  main.py               # uygulamayı başlatır, VeriTabani nesnesini pencereye verir   (GUI)
  requirements.txt      # customtkinter
  veritabani.py         # VeriTabani sınıfı: tüm SQL burada        (BACK END — YZ yasak)
  modeller/             # iş mantığı sınıfları                     (BACK END — YZ yasak)
  gui/                  # arayüz ekranları                         (YZ serbest)
    ana_pencere.py      # yan menü + içerik alanı; MODULLER listesi ekranları tanımlar
    sayfa.py            # Sayfa taban sınıfı: başlık, açıklama, "bağlantısız" uyarısı
    ana_panel.py        # açılış ekranı: özet kartları, hızlı erişim
    yapim_asamasinda.py # back end'i hazır olmayan modüller için geçici ekran
    bilesenler.py       # Tablo, FormPaneli, BilgiKarti, düğmeler, mesaj kutuları
    tema.py             # renkler ve yazı tipleri
veritabani.sql          # CREATE TABLE + örnek veri + temel sorgular (ÖĞRENCİ — YZ yasak)
sinif_diyagrami.pdf     # UML sınıf diyagramı                     (ÖĞRENCİ — YZ yasak)
README.md               #                                          (YZ serbest)
TESLIM.md               # teslim kontrol listesi
```

- Doğrulama kuralları model sınıfındadır (setter `ValueError` fırlatır); GUI hatayı yakalayıp
  `messagebox` ile anlamlı mesaj gösterir.
- SQL'de yalnızca parametreli sorgu (`?`); string birleştirme yok. `PRAGMA foreign_keys = ON`.
- PK / FK / NOT NULL kısıtları eksiksiz.

### Arayüz ↔ back end sözleşmesi

GUI'nin `VeriTabani` ve model sınıflarından beklediği metotlar. Metot adlarını, parametrelerini ve
dönüş değerlerini **sınıfın sahibi belirleyip buraya yazar**; ekran bu tabloya göre bağlanır.
Bir ekran yeni metot gerektirirse Claude ihtiyacı buraya "öneri" olarak ekler, sahibi onaylar ve yazar.

- `kod/main.py` `VeriTabani()` nesnesini **parametresiz** oluşturur. `kod/veritabani.py` yoksa veya
  bağlantı hata verirse arayüz "bağlantısız" modda açılır. Kurucu farklı olacaksa `main.py` güncellenir.
- Ekle/güncelle/sil hataları (`ValueError`, `sqlite3.IntegrityError` vb.) back end'de yutulmaz;
  GUI yakalayıp `messagebox` ile anlamlı mesaj gösterir.
- Bir modülün metotları hazır olunca `gui/ana_pencere.py` içindeki `MODULLER` listesinde o modülün
  `"sinif"` değeri gerçek ekran sınıfıyla değiştirilir.

| Modül | Sınıf.metot | Parametreler | Döndürür | Sahibi |
|---|---|---|---|---|
| _(sınıf sahipleri dolduracak)_ | | | | |

## Görev dağılımı

Her üye en az bir iş mantığı (OOP) sınıfından sorumludur (yönerge Bölüm 7). Yalnızca arayüz veya
dokümantasyon yapan üye bireysel katkı puanını tam alamaz.

| Üye | GitHub | İş mantığı sınıfları | GUI ekranı |
|---|---|---|---|
| _Ad Soyad_ | efeozd123-droid | | |
| _Ad Soyad_ | dnzctnn | | |
| _Ad Soyad_ | _kullanıcı adı_ | | |

## Git ve kod kuralları

- Bireysel puan commit geçmişine göre verilir: **her üye kendi hesabıyla ve kendi dosyalarını**
  commit eder. Başka bir üyenin dosyasını onun yerine yazıp commit etme.
- Tüm çalışma `main` dalında yapılır; ayrı dal açılmaz.
- Commit mesajları Türkçe ve açıklayıcı ("Siparis ekrani arayuzu eklendi"). "guncelleme",
  "son hali", yalnızca dosya adı gibi mesajlar puan düşürür. Commit'ler haftalara yayılmalı.
- YZ'nin ürettiği dosyalar (GUI, README, kural dosyaları) **Claude adıyla** commit edilir ve mesajın
  sonunda `Co-Authored-By: Claude` satırı bulunur; böylece YZ'nin yazdığı kısımlar commit geçmişinde
  açıkça ayrılır. Üyelerin kendi yazdığı dosyalar kendi hesaplarından commit edilir.
- Önce Pull, sonra çalış, sonra Commit and Push. Herkes kendi dosyasında çalışır (çakışma önlemi).
- `.db`, `venv/`, `.idea/` depoya girmez (`.gitignore`). `.db` yalnızca teslim zip'ine konur.
- İsimlendirme: Türkçe, Türkçe karakter yok; sınıflar `PascalCase`, metot/değişkenler `snake_case`.
- Derste görülmeyen ileri düzey yapılardan kaçın. Sunumda her satır savunulabilmeli.
- Teslimden sonra depoya push yapılmaz; zip son commit'ten oluşturulur.
