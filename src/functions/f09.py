from utils import mysort as srt
from utils import myappend as app

def laporanjin(usern, user, candi, bahan):
    if usern != "Bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
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
        totalkumpul = int(0)
        totalbangun = int(0)
        malas = str()
        for i in range (1, user[1][0]):
            if user[0][i][2] == "jin_pengumpul":
                totalkumpul += 1
            elif user[0][i][2] == "jin_pembangun":
                totalbangun += 1
        pembangun = [["",0] for i in range (totalbangun)]
        pembangun = [pembangun, [0]]
        for i in range (1, user[1][0]):
            if user[0][i][2] == "jin_pembangun":
                pembangun[0][pembangun[1][0]][0] = user[0][i][0]
                pembangun[1][0] = int(pembangun[1][0]) + 1
        pembangun = srt.stringsort(pembangun)
        for i in range (1, candi[1][0]):
            for j in range (pembangun[1][0]):
                if candi[0][i][1] == pembangun[0][j][0]:
                    pembangun[0][j][1] = int(pembangun[0][j][1]) + 1
        idxrajin = int(0)
        idxmalas = int(0)
        for i in range (pembangun[1][0] - 1, -1, -1):
            if pembangun[0][i][1] >= pembangun[0][idxrajin][1]:
                idxrajin = i
        for i in range (0, pembangun[1][0]):
            if pembangun[0][i][1] <= pembangun[0][idxmalas][1]:
                idxmalas = i
        print(f"\n> Total Jin: {user[1][0] - 3}")
        print(f"> Total Jin Pengumpul: {totalkumpul}")
        print(f"> Total Jin Pembangun: {totalbangun}")
        if totalbangun == 0:
            print("> Jin Terajin: -")
            print("> Jin Termalas: -")
        else:
            print(f"> Jin Terajin: {pembangun[0][idxrajin][0]}")
            print(f"> Jin Termalas: {pembangun[0][idxmalas][0]}")
        print(f"> Jumlah Pasir: {bahan[0][1][2]}")
        print(f"> Jumlah Batu: {bahan[0][2][2]}")
        print(f"> Jumlah Air: {bahan[0][3][2]}")
