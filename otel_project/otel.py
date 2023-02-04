from datetime import datetime

class Otel():
    def __init__(self):
        self.odalar = []
        self.personel = []
        self.rezervasyonlar = []

    def oda_ekle(self, oda):
        self.odalar.append(oda)

    def personel_ekle(self, personel):
        self.personel.append(personel)

    def personele_odenen_maas_toplami(self):
        toplam = 0
        for p in self.personel:
            toplam += p.aldigiMaas
        return toplam

    def bos_oda_sayisi(self):
        oda_sayisi = len(self.odalar)
        dolu_oda_sayisi = len(self.rezervasyonlar)
        return oda_sayisi - dolu_oda_sayisi

    def checkin(self, rezervasyon):
        misafir = rezervasyon.misafir
        oda = rezervasyon.oda
        print("{} {} {} numarali odaya yerlesti".format(
            misafir.isim, misafir.soyisim, oda.odaNumarasi
        ))
        self.rezervasyonlar.append(rezervasyon)

    def checkout(self, rezervasyon):
        misafir = rezervasyon.misafir
        print("{} {}'den alinacak ucret: {} TL".format(
            misafir.isim, misafir.soyisim, rezervasyon.ucret_hesapla())
        )
        self.rezervasyonlar.remove(rezervasyon)


class Personel():
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, pozisyon, maas, egitimDurumi, iseGirisTarihi):
        self.isim = isim
        self.soyisim = soyisim
        self.sicilNo = sicilNo
        self.kimlikNo = kimlikNo
        self.pozisyon = pozisyon
        self.aldigiMaas = maas
        self.egitimDurumi = egitimDurumi
        format = "%d/%m/%Y"
        self.iseGirisTarihi = datetime.strptime(iseGirisTarihi, format)
        self.email = isim.lower() + "." + soyisim.lower() + "@butikotel.com.tr"

    def personel_bilgilerini_goster(self):   #personellerin bilgilerini gösterir.
        return "Ad: {}, Soyad: {}, Maas: {}, Email: {}".format(self.isim, self.soyisim, self.aldigiMaas, self.email)

    def personelin_toplam_calistigi_gun_sayisi(self):
        bugun = datetime.now()
        calistigi_gun = (bugun - self.iseGirisTarihi).days
        return calistigi_gun

    def maas_zam_yap(self, tutar):
        pass

    def maas_kesintisi_yap(self, tutar):
        self.aldigiMaas -= tutar

    def ayliktoplam_verilecek_maas_hesapla(self, aldigiMaas):
        maas_listesi = []
        Personel.sum += aldigiMaas - self.aldigiMaas
        self._aldigiMaas = aldigiMaas


class Mudur(Personel):
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, aldigiMaas, egitimDurumi, iseGirisTarihi, sorumluOlduguKisiSayisi):
        Personel.__init__(self, isim, soyisim, sicilNo, kimlikNo, "Mudur" , aldigiMaas,  egitimDurumi, iseGirisTarihi)
        self.sorumluOlduguKisiSayisi = sorumluOlduguKisiSayisi
    
    def maas_zam_yap(self, prim):
        self.aldigiMaas *= prim

class Housekeeping(Personel):
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, aldigiMaas, egitimDurumi, iseGirisTarihi, dil, gunlukTemizledigiOdaSayisi):
        Personel.__init__(self, isim, soyisim, sicilNo, kimlikNo, "Temizlikci", aldigiMaas, egitimDurumi, iseGirisTarihi)
        self.gunlukTemizledigiOdaSayisi = gunlukTemizledigiOdaSayisi
        self.bildigiDil = dil

    def maas_zam_yap(self, yeni_asgari_ucret):
        self.aldigiMaas = yeni_asgari_ucret


class Resepsiyonist(Personel):
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, aldigiMaas, egitimDurumi, iseGirisTarihi, dil):
        Personel.__init__(self, isim, soyisim, sicilNo, kimlikNo, "Resepsiyonist", aldigiMaas, egitimDurumi, iseGirisTarihi)
        self.bildigiDil1 = dil
        
    def maas_zam_yap(self, performans):
        self.aldigiMaas += performans


class Barmen(Personel):
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, aldigiMaas, egitimDurumi, iseGirisTarihi, dil):
        Personel.__init__(self, isim, soyisim, sicilNo, kimlikNo, "Barmen", aldigiMaas, egitimDurumi, iseGirisTarihi)
        self.bildigiDil1 = dil
    
    def maas_zam_yap(self, performans):
        self.aldigiMaas += performans

class Garson(Personel):
    def __init__(self, isim, soyisim, sicilNo, kimlikNo, aldigiMaas, egitimDurumi, iseGirisTarihi, dil):
        Personel.__init__(self, isim, soyisim, sicilNo, kimlikNo, "Garson", aldigiMaas, egitimDurumi, iseGirisTarihi)
        self.bildigiDil1 = dil

    def maas_zam_yap(self, performans):
        self.aldigiMaas += performans


class Oda():
    def __init__(self, odaTipi, odaNumarasi, musaitmi, yatakSayisi):
        self.odaTipi = odaTipi
        self.odaNumarasi = odaNumarasi
        self.musaitmi = musaitmi   #True-False
        self.yatakSayisi = yatakSayisi

    def bos_oda_sayisi_bul(self):
        return self.odaSayisi - self.dolu_oda_sayisi

    def oda_sayisi_goster(self):
      return "Toplam {} oda vardir".format(self.odaSayisi)

    def check_in_tarihini_goster(self):
        return "{} {}, {} tarihinde giris yapmistir.".format(self.isim, self.soyisim, self.girisTarihi)

    def kalinan_gun_sayisi_hesapla(self):
        gun = (self.cikisTarihi - self.girisTarihi).days
        return "Toplam kalinan gun sayisi {} gundur.".format(gun)


class deluxOda(Oda):
    def __init__(self, odaTipi, odaNumarasi, musaitmi, yatakSayisi, klima, televizyon, internet, odaServisi, 
    erkenCheck_in, kasa, minibar):
        Oda.__init__(self, odaTipi, odaNumarasi, musaitmi, yatakSayisi)
        self.klima = klima
        self.televizyon = televizyon
        self.internet = internet
        self.odaServisi = odaServisi
        self.erkenCheck_in = erkenCheck_in
        self.kasa = kasa
        self.minibar = minibar
        self.fiyat = 1200

class suitOda(Oda):
    def __init__(self, odaTipi, odaNumarasi, musaitmi, yatakSayisi, klima, televizyon, internet, odaServisi, minibar):
        Oda.__init__(self, odaTipi, odaNumarasi, musaitmi, yatakSayisi)
        self.klima = klima
        self.televizyon = televizyon
        self.internet = internet
        self.odaServisi = odaServisi
        self.minibar = minibar
        self.fiyat = 1000

class standartOda(Oda):
    def __init__(self, odaNumarasi, musaitmi, yatakSayisi, televizyon, internet, minibar):
        Oda.__init__(self, "standart", odaNumarasi, musaitmi, yatakSayisi)
        self.televizyon = televizyon
        self.internet = internet
        self.minibar = minibar
        self.fiyat = 800


class Misafir():
    def __init__(self, isim, soyisim, kimlikNo, telefonNo, adres):
        self.isim = isim
        self.soyisim = soyisim
        self.kimlikNo = kimlikNo
        self.telefonNo = telefonNo
        self.adres = adres

class Hizmet():
    def __init__(self, hizmet_adi, fiyat):
        self.hizmet_adi = hizmet_adi
        self.fiyat = fiyat

class Rezervasyon():
    def __init__(self, misafir, oda, giris_tarihi, cikis_tarihi):
        self.misafir = misafir
        self.oda = oda

        format = "%d/%m/%Y"
        self.giris_tarihi = datetime.strptime(giris_tarihi, format)
        self.cikis_tarihi = datetime.strptime(cikis_tarihi, format)
        self.alinan_hizmetler = []

    def alinan_hizmet_ekle(self, hizmet):
        self.alinan_hizmetler.append(hizmet)
    
    def ucret_hesapla(self):
        kalinan_gun = (self.cikis_tarihi - self.giris_tarihi).days
        ucret = kalinan_gun * self.oda.fiyat
        for h in self.alinan_hizmetler:
            ucret += h.fiyat
        return ucret