def ubahjin(usern, user):
    if usern == "Bondowoso":
        ubah = str(input("Masukkan username jin : "))
        userada = False
        for i in range (1, user[1][0]):
            if ubah == user[0][i][0]:
                userada = True
                index = i
                break
        if userada:
            if user[0][index][2] == "jin_pengumpul":
                while True:
                    opt = str(input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? "))
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        user[0][index][2] = "jin_pembangun"
                        break
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
            elif user[0][index][2] == "jin_pembangun":
                while True:
                    opt = str(input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        user[0][index][2] = "jin_pengumpul"
                        break
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
        else:
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bandung Bondowoso yang dapat mengubah jin!")
    return user
