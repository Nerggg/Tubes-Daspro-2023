def jumlahbahan(candi):
    sand = int(0)
    stone = int(0)
    water = int(0)
    for i in range (1, candi[1][0]):
        sand = int(sand) + int(candi[0][i][2])
        stone = int(stone) + int(candi[0][i][3])
        water = int(water) + int(candi[0][i][4])
    return (sand, stone, water)

def hitungharga(li):
    return 10000 * int(li[2]) + 15000 * int(li[3]) + 7500 * int(li[4])
def laporancandi(usern, candi):
    if usern != "Bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        (sand, stone, water) = jumlahbahan(candi)
        idxmahal = int(1)
        idxmurah = int(1)
        for i in range (1, candi[1][0]):
            if hitungharga(candi[0][idxmahal]) < hitungharga(candi[0][i]):
                idxmahal = i
            if hitungharga(candi[0][idxmurah]) > hitungharga(candi[0][i]):
                idxmurah = i
        print(f"\n> Total candi: {candi[1][0] - 1}")
        print(f"> Total Pasir yang digunakan: {sand}")
        print(f"> Total Batu yang digunakan: {stone}")
        print(f"> Total Air yang digunakan: {water}")
        if candi[1][0] - 1 == 0:
            print(f"> ID Candi termahal: -")
            print(f"> ID Candi termurah: -")
        else:
            print(f"> ID Candi termahal: {idxmahal} (Rp {hitungharga(candi[0][idxmahal])})")
            print(f"> ID Candi termurah: {idxmurah} (Rp {hitungharga(candi[0][idxmurah])})")
