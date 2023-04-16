import random

def myappend(target, li):
    temp = [["" for i in range (target[1][1])] for j in range (target[1][0]+1)]
    temp = [temp, [target[1][0]+1,target[1][1]]]
    for i in range (target[1][0]):
        for j in range (target[1][1]):
            temp[0][i][j] = target[0][i][j]
    for i in range (target[1][1]):
        temp[0][target[1][0]][i] = li[i]
    return temp

def rng(n):
    return random.randint(n,5)

def kumpul(usern, user, bahan):
    if usern == "null":
        print("Lakukan login terlebih dahulu!")
    else:
        for i in range (1, user[1][0]):
            if usern == user[0][i][0]:
                index = i
                break
        if user[0][index][2] != "jin_pengumpul":
            print("Hanya jin pengumpul yang dapat mengumpulkan bahan bangunan!")
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
                bahan = myappend(bahan, ["pasir", "Pasir digunakan untuk membangun candi", 0])
                idxpasir = 3 - idxtemp
                idxtemp -= 1
            if not batuada:
                bahan = myappend(bahan, ["batu", "Batu digunakan untuk membangun candi", 0])
                idxbatu = 3 - idxtemp
                idxtemp -= 1
            if not airada:
                bahan = myappend(bahan, ["air", "Air digunakan untuk membangun candi", 0])
                idxair = 3 - idxtemp
                idxtemp -= 1
            sand = int(rng(0))
            stone = int(rng(0))
            water = int(rng(0))
            print(f"Jin menemukan {sand} pasir, {stone} batu, dan {water} air.")
            bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) + sand
            bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) + stone
            bahan[0][idxair][2] = int(bahan[0][idxair][2]) + water
    return bahan
