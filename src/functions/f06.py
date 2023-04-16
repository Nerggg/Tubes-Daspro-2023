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

def bangun(usern, user, candi, bahan):
    if usern == "null":
        print("Lakukan login terlebih dahulu!")
    else:
        for i in range (1, user[1][0]):
            if usern == user[0][i][0]:
                index = i
                break
        if user[0][index][2] != "jin_pembangun":
            print("Hanya jin pembangun yang dapat membangun candi!")
        else:
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
            else:
                sand = int(rng(1))
                stone = int(rng(1))
                water = int(rng(1))
                bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2])
                bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2])
                bahan[0][idxair][2] = int(bahan[0][idxair][2])
                if bahan[0][idxpasir][2] < sand or bahan[0][idxbatu][2] < stone or bahan[0][idxair][2] < water:
                    print("Bahan bangunan tidak mencukupi")
                    print("Candi tidak bisa dibangun!")
                else:
                    print(f"Candi berhasil dibangun dan menggunakan {sand} pasir, {stone} batu, dan {water} air.")
                    print("Sisa candi yang perlu dibangun: .")
                    bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) - sand
                    bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) - stone
                    bahan[0][idxair][2] = int(bahan[0][idxbatu][2]) - water
                    li = [candi[1][0], usern, sand, stone, water]
                    candi = myappend(candi, li)
    return (candi, bahan)
