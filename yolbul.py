def StartP(liste, a, i=0):
    if liste[i] == 'S':
        a = i
        return a
    else:
        return StartP(liste, i + 1, a)


def gidilecekYol(liste, length, i):
    count = 0
    if i < (len(liste) - length):
        if liste[i + length] == 'P' or liste[i + length] == 'H':
            count = count + 1
    if i > length:
        if liste[i - length] == 'P' or liste[i - length] == 'H':
            count = count + 1
    if liste[i + 1] == 'P' or liste[i + 1] == 'H':
        count = count + 1
    if liste[i - 1] == 'P' or liste[i - 1] == 'H':
        count = count + 1
    if count > 1:
        return True
    else:
        return False


def YolSecici(liste, length, i, gecici):
    if i < len(gecici) - length and gecici[i - length]== 'F':
        gecici=liste.copy()
        return 1
    if gecici[i - 1] == 'F' or gecici[i + 1] == 'F':
        gecici=liste.copy()
        return 1
    if i < len(gecici) - length:
        if gecici[i + length] == 'F':
            gecici=liste.copy()
            return 1
    if i < len(gecici) - length and (gecici[i + length] == 'P'
                                     or gecici[i + length] == 'H'):
        del gecici[i + length]
        gecici.insert(i + length, 'G')
        return YolSecici(gecici, length, i + length,gecici)

    if gecici[i + 1] == 'P' or gecici[i + 1] == 'H':
        del gecici[i + 1]
        gecici.insert(i + 1, 'G')
        return YolSecici(gecici, length, i + 1,gecici)

    if gecici[i - 1] == 'P' or gecici[i - 1] == 'H':
        gecici.insert(i - 1, 'G')
        return YolSecici(gecici, length, i - 1,gecici)

    if i > length and (gecici[i - length] == 'P'
                       or gecici[i - length] == 'H'):
        del gecici[i - length]
        gecici.insert(i - length, 'G')
        return YolSecici(gecici, length, i - length,gecici)
    else:
        gecici = liste.copy()
        return 0


def yol(liste, a, yollar, length):
    gecici=liste.copy()
    if liste[a] == 'S':
        del yollar[a]
        yollar.insert(a, 'S')
    if a < len(liste) - length and liste[a + length] == 'F':
        del yollar[a + length]
        del liste[a + length]
        liste.insert(a + length, 'F')
        yollar.insert(a + length, 'F')
    if liste[a - 1] == 'F':
        del yollar[a - 1]
        del liste[a - 1]
        liste.insert(a - 1, 'F')
        yollar.insert(a - 1, 'F')
    if liste[a + 1] == 'F':
        del yollar[a + 1]
        del liste[a + 1]
        liste.insert(a + 1, 'F')
        yollar.insert(a + 1, 'F')
    if a > length and liste[a-length] == 'F':
        del yollar[a - length]
        del liste[a - length]
        liste.insert(a - length, 'F')
        yollar.insert(a - length, 'F')

    elif liste[a] is not 'S' and gidilecekYol(harfler, length, a):
        if liste[a + length] == 'P' or liste[a + length] == 'H':
            if YolSecici(harfler, length, a + length,gecici) == 1:
                del yollar[a + length]
                if liste[a + length] == 'P':
                    yollar.insert(a + length, 1)
                else:
                    yollar.insert(a + length, 'H')
                del liste[a + length]
                liste.insert(a + length, 'G')
                return yol(liste, a + length, yollar, length)
            else:
                del liste[a + length]
                liste.insert(a + length, 'G')
        if liste[a + 1] == 'P' or liste[a + 1] == 'H':
            if YolSecici(harfler, length, a + 1,gecici) == 1:
                del yollar[a + 1]
                if liste[a + 1] == 'P':
                    yollar.insert(a + 1, 1)
                else:
                    yollar.insert(a + 1, 'H')
                del liste[a + 1]
                liste.insert(a + 1, 'G')
                return yol(liste, a + 1, yollar, length)
            else:
                del liste[a + 1]
                liste.insert(a + 1, 'G')

        if liste[a - 1] == 'P' or liste[a - 1] == 'H':
            if YolSecici(harfler, length, a - 1,gecici) == 1:
                del yollar[a - 1]
                if liste[a - 1] == 'P':
                    yollar.insert(a - 1, 1)
                else:
                    yollar.insert(a - 1, 'H')
                del liste[a - 1]
                liste.insert(a - 1, 'G')
                return yol(liste, a - 1, yollar, length)
            else:
                del liste[a - 1]
                liste.insert(a - 1, 'G')

        if a > length and (liste[a - length] == 'P' or liste[a - 1] == 'H'):
            if YolSecici(harfler, length, a - length,gecici) == 1:
                del yollar[a - length]
                if liste[a - length] == 'P':
                    yollar.insert(a - length, 1)
                else:
                    yollar.insert(a - length, 'H')
                del liste[a - length]
                liste.insert(a - length, 'G')
                return yol(liste, a - length, yollar, length)
            else:
                del liste[a - length]
                liste.insert(a - length, 'G')

    if a < len(liste)-length and (liste[a + length] == 'P' or liste[a + length] == 'H') \
            and yollar[a + length] == 0:
        del yollar[a + length]
        if liste[a + length] == 'P':
            yollar.insert(a + length, 1)
        else:
            yollar.insert(a + length, 'H')
        del liste[a + length]
        liste.insert(a + length, 'G')
        return yol(liste, a + length, yollar, length)

    elif (liste[a - 1] == 'P' or liste[a - 1] == 'H') \
            and yollar[a - 1] == 0:
        del yollar[a - 1]
        if liste[a - 1] == 'P':
            yollar.insert(a - 1, 1)
        else:
            yollar.insert(a - 1, 'H')
        del liste[a - 1]
        liste.insert(a - 1, 'G')
        return yol(liste, a - 1, yollar, length)

    elif (liste[a + 1] == 'P' or liste[a + 1] == 'H') \
            and yollar[a + 1] == 0:
        del yollar[a + 1]
        if liste[a + 1] == 'P':
            yollar.insert(a + 1, 1)
        else:
            yollar.insert(a + 1, 'H')
        del liste[a + 1]
        liste.insert(a + 1, 'G')
        return yol(liste, a + 1, yollar, length)
    elif a > length and (liste[a - length] == 'P' or liste[a - length] == 'H') \
            and yollar[a - length] == 0:
        del yollar[a - length]
        if liste[a - length] == 'P':
            yollar.insert(a - length, 1)
        else:
            yollar.insert(a - length, 'H')
        del liste[a - length]
        liste.insert(a - length, 'G')
        return yol(liste, a - length, yollar, length)
    else:
        return 0


def Yazdir(liste, length, dosya, i=0):
    if i < len(liste):
        if (i + 1) % length is 1 and i is not 0:
            dosya.write("\n")
        if liste[i] == 'F':
            dosya.write("F, ")
            dosya.flush()
            return Yazdir(liste, length, dosya, i + 1)
        if liste[i] == 'S':
            dosya.write("S, ")
            dosya.flush()
            return Yazdir(liste, length, dosya, i + 1)
        if liste[i] == 1:
            dosya.write("1, ")
            dosya.flush()
            return Yazdir(liste, length, dosya, i + 1)
        if liste[i] == 'H':
            dosya.write("H, ")
            dosya.flush()
            return Yazdir(liste, length, dosya, i + 1)
        else:
            dosya.write("0, ")
            return Yazdir(liste, length, dosya, i + 1)
    else:
        return -1


with open('girdi.txt') as dosya:
    DosyaVerisi = dosya.read()

uzunluk = len(DosyaVerisi[0:DosyaVerisi.find("\n")])

harfler = []

for i in DosyaVerisi:
    if i is not '\n':
        harfler.append(i)

s = 0
s = StartP(harfler, s)

yollar = [0] * len(harfler)
gecici = harfler.copy()
yol(harfler, s, yollar, uzunluk)


with open('cikti.txt', 'w') as cikti:
    Yazdir(yollar, uzunluk, cikti)
cikti = open('cikti.txt', 'r')

print(cikti.read())

k=input("press close to exit")