import random
from utils import myappend as app
from utils import rng

def batchkumpul(usern, user, bahan):
    for i in range (user[1][0]):
        if user[0][i][0] == usern:
            index = i
            break
    if user[0][index][2] != "jin_pengumpul":
        print("Hanya jin pengumpul yang dapat melakukan batch kumpul!")
    else:
        count = int(0)
        for i in range (user[1][0]):
            if user[0][i][2] == "jin_pengumpul":
                count += 1
        if count == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
            pasirada = False
            batuada = False
            airada = False
            idxtemp = 2
            for i in range (1, bahan[1][0]):
                if "pasir" == bahan[0][i][0]:
                    pasirada = True
                    idxpasir = i
                    idxtemp -= 1
                elif "batu" == bahan[0][i][0]:
                    batuada = True
                    idxbatu = i
                    idxtemp -= 1
                elif "air" == bahan[0][i][0]:
                    airada = True
                    idxair = i
                    idxtemp -= 1
            if not pasirada:
                bahan = app.myappend(bahan, ["pasir", "Pasir digunakan untuk membangun candi", 0])
                idxpasir = 3 - idxtemp
                idxtemp -= 1
            if not batuada:
                bahan = app.myappend(bahan, ["batu", "Batu digunakan untuk membangun candi", 0])
                idxbatu = 3 - idxtemp
                idxtemp -= 1
            if not airada:
                bahan = app.myappend(bahan, ["air", "Air digunakan untuk membangun candi", 0])
                idxair = 3 - idxtemp
                idxtemp -= 1
            sand = int(0)
            stone = int(0)
            water = int(0)
            for i in range (count):
                sand += int(rng.rng(0))
                stone += int(rng.rng(0))
                water += int(rng.rng(0))
            print(f"Jin menemukan total {sand} pasir, {stone} batu, dan {water} air.")
            bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) + sand
            bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) + stone
            bahan[0][idxair][2] = int(bahan[0][idxair][2]) + water
    return bahan

def batchbangun(usern, user, candi, bahan):
    for i in range (user[1][0]):
        if user[0][i][0] == usern:
            index = i
            break
    if user[0][index][2] != "jin_pembangun":
        print("Hanya jin pembangun yang dapat melakukan batch kumpul!")
    else:
        count = int(0)
        pembangun = [[["pembangun"]], [1,1]]
        for i in range (user[1][0]):
            if user[0][i][2] == "jin_pembangun":
                count += 1
                pembangun = app.myappend(pembangun, [user[0][i][0]])
        if count == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            pasirada = False
            batuada = False
            airada = False
            for i in range (1, bahan[1][0]):
                if "pasir" == bahan[0][i][0]:
                    pasirada = True
                    idxpasir = i
                elif "batu" == bahan[0][i][0]:
                    batuada = True
                    idxbatu = i
                elif "air" == bahan[0][i][0]:
                    airada = True
                    idxair = i
            if not pasirada and not batuada and not airada:
                print("Bangun gagal. Anda tidak memiliki bahan apapun. Silahkan kumpul terlebih dahulu")
            elif not pasirada and not batuada and airada:
                print("Bangun gagal. Anda tidak memiliki pasir dan batu. Silahkan kumpul terlebih dahulu")
            elif batuada and not pasirada and not airada:
                print("Bangun gagal. Anda tidak memiliki pasir dan air. Silahkan kumpul terlebih dahulu")
            elif pasirada and not batuada and not airada:
                print("Bangun gagal. Anda tidak memiliki batu dan air. Silahkan kumpul terlebih dahulu")
            elif not pasirada and batuada and airada:
                print("Bangun gagal. Anda tidak memiliki pasir. Silahkan kumpul terlebih dahulu")
            elif pasirada and batuada and not airada:
                print("Bangun gagal. Anda tidak memiliki air. Silahkan kumpul terlebih dahulu")
            elif not batuada and pasirada and airada:
                print("Bangun gagal. Anda tidak memiliki batu. Silahkan kumpul terlebih dahulu")
            else:
                canditemp = candi
                bahantemp = [0, 0, 0]
                jumlah = int(0)
                for i in range (count):
                    sand = int(rng.rng(1))
                    stone = int(rng.rng(1))
                    water = int(rng.rng(1))
                    canditemp = app.myappend(canditemp, [candi[1][0] + i, pembangun[0][i+1][0], sand, stone, water])
                    bahantemp[0] += sand
                    bahantemp[1] += stone
                    bahantemp[2] += water
                    jumlah += 1
                if bahantemp[0] > int(bahan[0][idxpasir][2]) or bahantemp[1] > int(bahan[0][idxbatu][2]) or bahantemp[2] > int(bahan[0][idxair][2]):
                    print(f"\nBangun gagal. Bahan yang kurang:")
                    if int(bahantemp[0]) > int(bahan[0][idxpasir][2]):
                        print(f"-{int(bahantemp[0]) - int(bahan[0][idxpasir][2])} pasir")
                    if int(bahantemp[1]) > int(bahan[0][idxbatu][2]):
                        print(f"-{int(bahantemp[1]) - int(bahan[0][idxbatu][2])} batu")
                    if int(bahantemp[2]) > int(bahan[0][idxair][2]):
                        print(f"-{int(bahantemp[2]) - int(bahan[0][idxair][2])} air")
                else:
                    print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {bahantemp[0]} pasir, {bahantemp[1]} batu, dan {bahantemp[2]} air.")
                    print(f"Jin berhasil membangun total {jumlah} candi.")
                    candi = canditemp
                    bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) - bahantemp[0]
                    bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) - bahantemp[1]
                    bahan[0][idxair][2] = int(bahan[0][idxair][2]) - bahantemp[2]
    return (candi, bahan)
