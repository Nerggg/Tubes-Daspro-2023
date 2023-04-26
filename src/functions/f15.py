def help(usern, user): #Fungsi Help untuk membantu user berdasarkan akun yang digunakan
    if usern == "": #Apabila tidak ada akun yang digunakan, akan memunculkan layar help untuk user yang belum masuk ke suatu akun
        print("===================== HELP =====================")
        print("")
        print("1. Login: Masuk menggunakan akun")
        print("2. Exit: Keluar dari program")
    else:
        for i in range (user[1][0]):
            if user[0][i][0] == usern:
                index = i
                break
        if user[0][index][2] == "bandung_bondowoso": #Apabila akun yang digunakan adalah Bondowoso, akan memunculkan layar help untuk akun Bondowoso
            print("===================== HELP =====================")
            print("")
            print("1. logout: Keluar dari akun yang sedang digunakan")
            print("2. summonjin: Memanggil jin")
            print("3. hilangkanjin: Menghapus jin")
            print("4. ubahtipejin: Mengubah tipe jin")
            print("5. batchkumpul: Membuat semua jin pengumpul mengumpulkan bahan")
            print("6. batchbangun: Membuat semua jin pembangun membangun candi")
            print("7. laporanjin: Mengambil laporan jin")
            print("8. laporancandi: Mengambil laporan candi")
        elif user[0][index][2] == "roro_jonggrang": #Apabila akun yang digunakan adalah Jonggrang, akan memunculkan layar help untuk akun Jonggrang
            print("===================== HELP =====================")
            print("")
            print("1. logout: Keluar dari akun yang sedang digunakan")
            print("2. hancurkancandi: Menghancurkan candi")
            print("3. ayamberkokok: Membuat ayam berkokok sehingga memalsukan pagi hari")
        elif user[0][index][2] == "jin_pembangun": #Apabila akun yang digunakan adalah Pembangun, akan memunculkan layar help untuk akun Jin Pembangun
            print("===================== HELP =====================")
            print("")
            print("1. bangun: Membangun candi")
        elif user[0][index][2] == "jin_pengumpul": #Apabila akun yang digunakan adalah Pengumpul, akan memunculkan layar help untuk akun Jin Pengumpul
            print("===================== HELP =====================")
            print("")
            print("1. kumpul: Mengumpulkan bahan")
