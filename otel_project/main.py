import otel

butikOtel = otel.Otel()

butikOtel.personel_ekle(
    otel.Mudur("Ahmet", "Basaran", 10111, 52812131415,
    30000, "Universite", "10/01/2000", 9)
)

butikOtel.personel_ekle(
    otel.Resepsiyonist("Burak", "Yilmaz", 20001, 12345678901,
    6000, "Universite", "03/02/2019", "Inglizce")
)

butikOtel.personel_ekle(
    otel.Resepsiyonist("Mehmet", "Karatoprak", 20002, 12345678902,
    6500, "Universite", "04/02/2019", "Inglizce")
)

butikOtel.personel_ekle(
    otel.Housekeeping("Emre", "Yildirim", 20311, 52315191410,
    5000, "Turizm MYO", "01/06/2019", "Turkce", 4)
)

butikOtel.personel_ekle(
    otel.Housekeeping("Ecem", "Demirli", 20647, 47392745915,
    6000, "Turizm MYO", "01/06/2019", "Turkce", 5)
)

butikOtel.personel_ekle(
    otel.Barmen("Cem", "Duman", 30045, 27493648932,
    6000, "Universite", "22/03/2017", "Ingilizce")
)

butikOtel.personel_ekle(
    otel.Garson("Bulent", "Sezgin", 20647, 38649021012,
    6000, "Universite", "03/06/2018", "Almanca")
)

butikOtel.oda_ekle(otel.standartOda(101, True, 2, True, False, True))
butikOtel.oda_ekle(otel.standartOda(102, True, 2, True, False, True))
butikOtel.oda_ekle(otel.standartOda(103, True, 1, True, False, True))
butikOtel.oda_ekle(otel.suitOda(104, True, 3, True, True, False, True, True, True))
butikOtel.oda_ekle(otel.suitOda(105, True, 2, True, True, False, True, True, True))
butikOtel.oda_ekle(otel.suitOda(106, True, 3, True, True, False, True, True, True))
butikOtel.oda_ekle(otel.deluxOda(107, True, 3, True, True, True, False, True, False, True, False))
butikOtel.oda_ekle(otel.deluxOda(108, True, 4, True, True, True, True, True, True, True, True))
butikOtel.oda_ekle(otel.deluxOda(109, True, 3, True, True, False, True, True, True, True, True))

print("Personele odenecek toplam maas: {} TL".format(butikOtel.personele_odenen_maas_toplami()))
print("Oda sayisi: ", len(butikOtel.odalar))
print("Bos oda sayisi: ", butikOtel.bos_oda_sayisi())


misafir1 = otel.Misafir("Buse", "Demir", 55613578923, 533221043, "Marmaris-Mugla")
r1 = otel.Rezervasyon(misafir1, butikOtel.odalar[0], "10/12/2022", "12/12/2022")
r1.alinan_hizmet_ekle(otel.Hizmet("Kablolu TV", 500))
r1.alinan_hizmet_ekle(otel.Hizmet("WiFi", 400))
butikOtel.checkin(r1)
print("Bos oda sayisi: ", butikOtel.bos_oda_sayisi())

misafir2 = otel.Misafir("Deniz", "Saygin", 45673580093, 5321230044, "izmir")
r2 = otel.Rezervasyon(misafir2, butikOtel.odalar[1], "23/06/2022", "25/06/2022")
r2.alinan_hizmet_ekle(otel.Hizmet("Ozel Araç", 3000))
butikOtel.checkin(r2)

print("Bos oda sayisi: ", butikOtel.bos_oda_sayisi())
butikOtel.checkout(r2)
print("Bos oda sayisi: ", butikOtel.bos_oda_sayisi())

misafir3 = otel.Misafir("Betul", "Girgin", 45673580093, 5321230044, "izmir")
r3 = otel.Rezervasyon(misafir3, butikOtel.odalar[1], "23/06/2022", "25/06/2022")
r3.alinan_hizmet_ekle(otel.Hizmet("Ozel Araba", 3000))
butikOtel.checkin(r3)
butikOtel.checkout(r1)
butikOtel.checkout(r3)

print("Bos oda sayisi: ", butikOtel.bos_oda_sayisi())

for p in butikOtel.personel:
    print("Personel {} {}, {} gündür çalismaktadir.".format(
        p.isim,
        p.soyisim,
        p.personelin_toplam_calistigi_gun_sayisi())
    )

for i in butikOtel.personel:
    print(i.personel_bilgilerini_goster())