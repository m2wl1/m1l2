karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifrenin uzunluğunu girin:"))

sifre = ""
if sifre_uzunlugu >=8:
    for i in range(sifre_uzunlugu):
        sifre = sifre + random.choice(karakterler)
else:
    print("daha uzun olmalı")
print(sifre)
