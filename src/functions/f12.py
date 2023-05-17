# fungsi ini menerima matriks 'candi' yang berisi data candi
# dan 'usern' sebagai username pemain saat itu
def ayamberkokok(usern, candi):

    # jika username pemain bukan Roro
    if usern != "Roro":
        print("Hanya Roro yang dapat memanggil ayam!")

        # mengembalikan 'True' agar permainan tidak berakhir
        return True

    # jika username pemain adalah Roro
    else:
        print("\nKukuruyuk.. Kukuruyuk..\n")

        # mengeluarkan jumlah candi yang sudah terbangun
        print(f"Jumlah Candi: {candi[1][0] - 1}\n")

        # memeriksa apakah candi yang sudah terbangun berjumlah kurang dari 100
        if candi[1][0] - 1 < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi")

        else:   # jika candi yang terbangun berjumlah lebih besar sama dengan 100
            print("Yah, Bandung Bondowoso memenangkan permainan!")

    # mengembalikan 'False' untuk menghentikan permainan
    return False
