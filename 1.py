while True:
    secenek1 = "(1) toplama"
    secenek2 = "(2) cikarma"
    secenek3 = "(3) carpma"
    secenek4 = "(4) bolme"

    print "Yapmak istediginiz islemin numarasini giriniz"

    print secenek1
    print secenek2
    print secenek3
    print secenek4

    soru = raw_input(":")

    if soru == "1":
        sayi1 = input("Ilk sayiyi girin")
        sayi2 = input("Ikinci sayiyi girin")
        print sayi1, "+", sayi2, "=", sayi1 + sayi2

    if soru == "2":
        sayi3 = input("Ilk sayiyi girin")
        sayi4 = input("Ikinci sayiyi girin")
        print sayi3, "-", sayi4, "=", sayi3 - sayi4

    if soru == "3":
        sayi5 = input("Ilk sayiyi girin")
        sayi6 = input("Ikinci sayiyi girin")
        print sayi5, "X", sayi6, "=", sayi5 * sayi6

    if soru == "4":
        sayi7 = input("Ilk sayiyi girin")
        sayi8 = input("Ikinci sayiyi girin")
        print sayi7, "/", sayi8, "=", sayi7 / sayi8