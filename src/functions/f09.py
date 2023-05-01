from utils import mysort as srt
from utils import myappend as app

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# dan matriks 'bahan' yang berisi data bahan yang dimiliki oleh pemain
def laporanjin(usern, user, candi, bahan):

    # jika username user bukan Bondowoso
    if usern != "Bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

    # tetapi jika username user adalah Bondowoso
    else:
        # kita cek apakah bahan-bahannya sudah ada pada matriks 'bahan' atau belum
        pasirada = False
        batuada = False
        airada = False
        idxtemp = 2

        # jika sudah ada, kita ambil index dari masing-masing bahan
        for i in range (1, bahan[1][0]):
            if "pasir" == bahan[0][i][0]:
                pasirada = True
                idxpasir = i
                idxtemp -= 1
            elif "batu" == bahan[0][i][0]:
                batuada = True
                idxbatu = i
                idxtemp -= 1
            elif "air" == bahan[0][i][0]:
                airada = True
                idxair = i
                idxtemp -= 1

        # jika pasir belum ada, kita declare 0 pasir ke matriks 'bahan'
        if not pasirada:
            bahan = app.myappend(bahan, ["pasir", "Pasir digunakan untuk membangun candi", 0])
            idxpasir = 3 - idxtemp
            idxtemp -= 1

        # jika batu belum ada, kita declare 0 batu ke matriks 'bahan'
        if not batuada:
            bahan = app.myappend(bahan, ["batu", "Batu digunakan untuk membangun candi", 0])
            idxbatu = 3 - idxtemp
            idxtemp -= 1

        # jika air belum ada, kita declare 0 air ke matriks 'bahan'
        if not airada:
            bahan = app.myappend(bahan, ["air", "Air digunakan untuk membangun candi", 0])
            idxair = 3 - idxtemp
            idxtemp -= 1


        # kita hitung ada berapa total jin pengumpul dan jin pembangun
        # dengan menggunakan loop
        totalkumpul = int(0)
        totalbangun = int(0)
        for i in range (1, user[1][0]):
            if user[0][i][2] == "jin_pengumpul":
                totalkumpul += 1
            elif user[0][i][2] == "jin_pembangun":
                totalbangun += 1

        # kemudian kita cari jin terrajin dan jin termalasnya
        # dengan membuat matriks yang berisi nama jin dan jumlah candi yang dibangun olehnya
        pembangun = [["",0] for i in range (totalbangun)]
        pembangun = [pembangun, [0]]

        # pertama kita tambahkan terlebih dahulu jin pembangun ke dalam matriks
        for i in range (1, user[1][0]):
            if user[0][i][2] == "jin_pembangun":
                pembangun[0][pembangun[1][0]][0] = user[0][i][0]
                pembangun[1][0] = int(pembangun[1][0]) + 1

        # setelah itu lakukan sorting agar namanya berurut secara abjad
        pembangun = srt.stringsort(pembangun)

        # lalu hitung ada berapa candi yang dibangun oleh jin itu
        for i in range (1, candi[1][0]):
            for j in range (pembangun[1][0]):
                if candi[0][i][1] == pembangun[0][j][0]:
                    pembangun[0][j][1] = int(pembangun[0][j][1]) + 1 # dengan menambahkan 1 pada jumlah candi yang dibangun oleh jin tersebut

        # sekarang kita menentukan index dari jin terrajin dan jin termalas
        idxrajin = int(0)
        idxmalas = int(0)
        # dengan membandingkan banyak candi yang mereka bangun dengan loop
        for i in range (pembangun[1][0] - 1, -1, -1):
        # jika ada pembangun yang membangun lebih banyak candi dibandingkan jin dengan index terrajin
            if pembangun[0][i][1] >= pembangun[0][idxrajin][1]:
                idxrajin = i # maka index mereka ditukar
        # dan jika ada pembangun yang membangun lebih sedikit candi dibandingkan jin dengan index termalas
        for i in range (0, pembangun[1][0]):
            if pembangun[0][i][1] <= pembangun[0][idxmalas][1]:
                idxmalas = i # maka indeks mereka ditukar

        # output laporan jin
        print(f"\n> Total Jin: {user[1][0] - 3}") # nilai efektif dikurangi 3 (Bondowoso, Roro, dan nama kolom)
        print(f"> Total Jin Pengumpul: {totalkumpul}")
        print(f"> Total Jin Pembangun: {totalbangun}")
        if totalbangun == 0: # jika jin pembangun tidak ada
            print("> Jin Terajin: -") # berarti jin terrajin dan termalas juga tidak ada
            print("> Jin Termalas: -")
        else: # tetapi jika jin pembangun ada
            print(f"> Jin Terajin: {pembangun[0][idxrajin][0]}") # kita buat output yang sesuai
            print(f"> Jin Termalas: {pembangun[0][idxmalas][0]}")

        # terakhir kita output jumlah bahan yang dimiliki
        print(f"> Jumlah Pasir: {bahan[0][1][2]} unit")
        print(f"> Jumlah Batu: {bahan[0][2][2]} unit")
        print(f"> Jumlah Air: {bahan[0][3][2]} unit")
