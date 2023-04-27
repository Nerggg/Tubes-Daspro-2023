# fungsi ini menerima 'usern' sebagai username pemain saat itu
# dan matriks 'user' yang berisi data seluruh pemain
def ubahjin(usern, user):
    
    # ketika username pemain bukan Bondowoso
    if usern != "Bondowoso":
        print("Hanya Bandung Bondowoso yang dapat mengubah jin!")
        
    # tetapi jika username pemain adalah Bondowoso
    else:
    
        # input username jin yang akan diubah rolenya
        ubah = str(input("Masukkan username jin : "))
        
        # cek apakah username memang ada atau tidak pada 'user'
        userada = False
        for i in range (1, user[1][0]):
            if ubah == user[0][i][0]:
                userada = True
                index = i
                break
                
        # jika username ada pada 'user'
        if userada:
                
            # dan username tersebut adalah jin pengumpul
            if user[0][index][2] == "jin_pengumpul":
            
                # maka tanyakan kepada pemain apakah ingin mengubahnya menjadi jin pembangun
                while True:
                    opt = str(input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? "))
                    # jika pemain sudah setuju
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        user[0][index][2] = "jin_pembangun" # dan ganti role jin pada 'user'
                        break
                    # tetapi jika pemain tidak setuju
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
            
            # tetapi jika username tersebut adalah jin pembangun
            elif user[0][index][2] == "jin_pembangun":
            
                # maka tanyakan kepada pemain apakah ingin mengubahnya menjadi jin pengumpul
                while True:
                    opt = str(input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
                    # jika pemain sudah setuju
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        user[0][index][2] = "jin_pengumpul"
                        break
                    # tetapi jika pemain tidak setuju                        
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
                        
        # tetapi jika username tidak ada pada 'user'
        else:
            print("Tidak ada jin dengan username tersebut.")
    
    # kembalikan 'user'
    return user
