# fungsi ini menerima 'usern' sebagai username pemain saat itu
def logout(usern):

    # jika username kosong
    if usern == "":
        print("Anda belum login!")
        
    else: # jika username tidak kosong
        print("Logout berhasil!")
    return "" # dan kembalikan username kosong karena pemain sudah logout
