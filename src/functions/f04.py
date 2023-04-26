from utils import myremove as myr

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain,
# dan matriks 'candi' yang berisi data candi 
def hapusjin(usern, user, candi):

    # ketika username pemain bukan Bondowoso 
    if usern != "Bondowoso":
        print("Hanya Bandung Bondowoso yang dapat menghapus jin!")
        
    # tetapi jika username pemain adalah Bondowoso
    else:
        
        # input username yang akan dihapus
        hapus = str(input("Masukkan username jin : "))
        
        # lakukan pengecekan username pada matriks 'user'
        userada = False
        for i in range (1, user[1][0]):
            if hapus == user[0][i][0]:
                userada = True
                break
                
        # jika username tersebut ada pada matriks
        if userada:
        
            # input komitmen pemain untuk menghapus jin
            print(f"Apakah anda yakin ingin menghapus jin dengan username {hapus} (Y/N)?", end = " ")
            opt = str(input())
            
            # jika pemain benar-benar ingin menghapus jin
            if opt == "y" or opt == "Y":
                print("\nJin telah berhasil dihapus dari alam gaib.")
                user = myr.myremove_user(hapus, user) # hapus username jin dari 'user' menggunakan 'myremove.py'
                candi = myr.myremove_candi(hapus, candi) # dan hapus juga candi yang dibuat olehnya menggunakan 'myremove.py'
                
            # tetapi jika pemain tidak jadi menghapus jin
            elif opt == "n" or opt == "N":
                print("\nPenghapusan jin dibatalkan.")
        
        # tetapi jika username tersebut tidak ada pada matriks
        else:
            print("Tidak ada jin dengan username tersebut.")
        
    # mengembalikan 'user' dan 'candi'
    return (user, candi)
