from utils import myremove as myr

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
                user = myr.myremove_user(hapus, user)
                candi = myr.myremove_candi(hapus, candi)
            elif opt == "n" or opt == "N":
                print("\nPenghapusan jin dibatalkan.")
        else:
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bandung Bondowoso yang dapat menghapus jin!")
    return (user, candi)
