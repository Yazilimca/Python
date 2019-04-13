import random


liste = ''
parola = ''

cevap_sayi = input('Parolanın içerisinde sayı olsun mu? [E/H]: ')
if cevap_sayi == 'E':
  liste = liste + '0123456789'

cevap_harf = input('Parolanın içerisinde harf olsun mu? [E/H]: ')
if cevap_harf == 'E':
  liste = liste + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

cevap_karakter = input('Parolanın içerisinde özel karakter olsun mu? [E/H]: ')
if cevap_karakter == 'E':
  liste = liste + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

minimum = int(input('Parola minimum karakter olsun?: '))
maksimum = int(input('Parola maksimum kaç karakter olsun?: '))

uzunluk = random.randint(minimum, maksimum)

if cevap_sayi != 'E' and cevap_harf != 'E' and cevap_karakter != 'E':
  print('En az bir cevap E olmalıdır\n')
else:
  for c in range(uzunluk):
    parola += random.choice(liste)


    
print(parola)

