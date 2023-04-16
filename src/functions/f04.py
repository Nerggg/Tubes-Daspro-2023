def myremove_user(target, li):
    count = int(0)
    for i in range (1, li[1][0]):
        if li[0][i][0] == target:
            count += 1
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-count)]
    temp = [temp, [li[1][0]-count,li[1][1]]]
    for i in range (temp[1][0]):
        if li[0][i][0] == target:
            continue
        else:
            for j in range (temp[1][1]):
                temp[0][i][j] = li[0][i][j]
    return temp

def myremove_candi(target, li):
    count = int(0)
    for i in range (1, li[1][0]):
        if li[0][i][1] == target:
            count += 1
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-count)]
    print(count)
    temp = [temp, [li[1][0]-count,li[1][1]]]
    for i in range (temp[1][0]):
        if li[0][i][1] != target:
            for j in range (temp[1][1]):
                temp[0][i][j] = li[0][i][j]
        else:
            for j in range (temp[1][1]):
                temp[0][i][j] = li[0][i+count][j]
        if i > 0:
            temp[0][i][0] = i
    return temp

def hapusjin(usern, user, candi):
    if usern == "Bondowoso":
        hapus = str(input("Masukkan username jin : "))
        userada = False
        for i in range (1, user[1][0]):
            if hapus == user[0][i][0]:
                userada = True
                break
        if userada:
            print(f"Apakah anda yakin ingin menghapus jin dengan username {hapus} (Y/N)?", end = " ")
            opt = str(input())
            if opt == "y" or opt == "Y":
                print("\nJin telah berhasil dihapus dari alam gaib.")
                user = myremove_user(hapus, user)
                candi = myremove_candi(hapus, candi)
            elif opt == "n" or opt == "N":
                print("\nPenghapusan jin dibatalkan.")
        else:
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bandung Bondowoso yang dapat menghapus jin!")
    return (user, candi)
