# fungsi tambahan untuk menghitung semua jumlah bahan yang telah
# digunakan untuk membuat candi dari matriks 'candi'
def jumlahbahan(candi):
    sand = int(0)
    stone = int(0)
    water = int(0)
    for i in range (1, candi[1][0]): # gunakan looping untuk menelusuri setiap elemen matriks 'candi'
        sand = int(sand) + int(candi[0][i][2]) 
        stone = int(stone) + int(candi[0][i][3])
        water = int(water) + int(candi[0][i][4])
    return (sand, stone, water)

# fungsi tambahan untuk menghitung harga candi sesuai dengan ketentuan pada spesifikasi
# yang menerima list 'li' yang berisi [id, pembuat, pasir, batu, air]
def hitungharga(li):
    return 10000 * int(li[2]) + 15000 * int(li[3]) + 7500 * int(li[4])
    
# fungsi ini menerima 'usern' sebagai string username dari pemain saat itu
# dan matriks 'candi' yang berisi data seluruh candi yang sudah dibangun
def laporancandi(usern, candi):

    # cek username pemain
    # bila username bukan Bondowoso maka
    if usern != "Bondowoso":
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        
    # tetapi jika username pemain adalah Bondowoso maka
    else:
    
        # hitung ada berapa jumlah bahan yang telah digunakan untuk membangun candi
        (sand, stone, water) = jumlahbahan(candi)
        
        # cari indeks candi yang memiliki harga termurah dan termahal
        idxmahal = int(1)
        idxmurah = int(1)
        for i in range (1, candi[1][0]):
            if hitungharga(candi[0][idxmahal]) < hitungharga(candi[0][i]): # jika ada candi yang lebih mahal
                idxmahal = i # maka indeks mereka ditukar
            if hitungharga(candi[0][idxmurah]) > hitungharga(candi[0][i]): # dan jika ada candi yang lebih murah
                idxmurah = i # maka indeks mereka ditukar
                
        # output laporan candi
        print(f"\n> Total candi: {candi[1][0] - 1}") # total candi dikurangi satu (nama kolom)
        print(f"> Total Pasir yang digunakan: {sand}")
        print(f"> Total Batu yang digunakan: {stone}")
        print(f"> Total Air yang digunakan: {water}")
        if candi[1][0] - 1 == 0: # jika total candi adalah nol
            print(f"> ID Candi termahal: -") # maka tidak ada candi termahal dan termurah
            print(f"> ID Candi termurah: -")
        else: # tetapi jika total candi tidak nol
            print(f"> ID Candi termahal: {idxmahal} (Rp {hitungharga(candi[0][idxmahal])})") # maka buat output yang sesuai
            print(f"> ID Candi termurah: {idxmurah} (Rp {hitungharga(candi[0][idxmurah])})")
