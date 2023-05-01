# fungsi ini menerima 'usern' sebagai username pemain saat itu
def logout(usern):

    # jika username kosong
    if usern == "":
        print("\nLogout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    else: # jika username tidak kosong
        print("\nLogout berhasil!")
    return "" # dan kembalikan username kosong karena pemain sudah logout
