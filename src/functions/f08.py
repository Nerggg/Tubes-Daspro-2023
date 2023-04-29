import random
from utils import myappend as app
from utils import rng

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain,
# dan matriks 'bahan' yang berisi data bahan yang dimiliki pemain
def batchkumpul(usern, user, bahan):

    # jika username pemain bukan Bondowoso
    if usern != "Bondowoso":
        print("Hanya Bondowoso yang dapat melakukan batch kumpul!")

    # tetapi jika username pemain adalah Bondowoso
    else:

        # kita hitung jumlah jin pengumpul yang kita miliki
        count = int(0)
        for i in range (user[1][0]):
            if user[0][i][2] == "jin_pengumpul":
                count += 1

        # jika kita tidak memiliki jin pengumpul
        if count == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

        # tetapi jika kita memiliki jin pengumpul
        else:
            print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")

            # kita periksa apakah bahannya sudah ada pada matriks 'bahan'
            pasirada = False
            batuada = False
            airada = False
            idxtemp = 2

            # jika sudah ada, kita simpan indeks dari masing-masing bahannya
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

            # jika pasir tidak ada, kita declare pasir sebanyak 0 pada matriks 'bahan'
            if not pasirada:
                bahan = app.myappend(bahan, ["pasir", "Pasir digunakan untuk membangun candi", 0])
                idxpasir = 3 - idxtemp
                idxtemp -= 1

            # jika batu tidak ada, kita declare batu sebanyak 0 pada matriks 'bahan'
            if not batuada:
                bahan = app.myappend(bahan, ["batu", "Batu digunakan untuk membangun candi", 0])
                idxbatu = 3 - idxtemp
                idxtemp -= 1

            # jika air tidak ada, kita declare air sebanyak 0 pada matriks 'bahan'
            if not airada:
                bahan = app.myappend(bahan, ["air", "Air digunakan untuk membangun candi", 0])
                idxair = 3 - idxtemp
                idxtemp -= 1

            # kemudian kita hitung berapa bahan yang dikumpulkan oleh para jin pengumpul
            sand = int(0)
            stone = int(0)
            water = int(0)

            # dengan menggunakan loop sebanyak jumlah jin pengumpul
            for i in range (count):
                sand += int(rng.rng(0))
                stone += int(rng.rng(0))
                water += int(rng.rng(0))

            # setelah itu kita simpan bahan-bahan yang telah dikumpulkan pada matriks 'bahan'
            print(f"Jin menemukan total {sand} pasir, {stone} batu, dan {water} air.")
            bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) + sand
            bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) + stone
            bahan[0][idxair][2] = int(bahan[0][idxair][2]) + water

    # dan kembalikan matriks 'bahan'
    return bahan

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# dan matriks 'bahan' yang berisi data bahan yang dimiliki oleh pemain
def batchbangun(usern, user, candi, bahan):

    # cek username pemain terlebih dahulu
    # jika username pemain bukan Bondowoso
    if usern != "Bondowoso":
        print("Hanya Bondowoso yang dapat melakukan batch bangun!")

    # tetapi jika username pemain adalah Bondowoso
    else:

        # kita hitung ada berapa jin pembangun yang dimiliki
        # dan juga kita declare matriks yang akan menyimpan semua username jin pembangun
        # dengan pembangun[1][0] sebagai nilai efektif dan pembangun[1][1] sebagai jumlah kolom matriks
        count = int(0)
        pembangun = [[["pembangun"]], [1,1]]
        for i in range (user[1][0]):
            if user[0][i][2] == "jin_pembangun":
                count += 1
                pembangun = app.myappend(pembangun, [user[0][i][0]])

        # jika ternyata kita tidak memiliki jin pembangun
        if count == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

        # tetapi jika kita memiliki jin pembangun
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

            # kita hitung ada berapa bahan yang akan dibutuhkan untuk membangun candi
            # dan simpan bahan tersebut pada list 'bahantemp'
            # kemudian kita duplikat 'candi' ke 'canditemp'
            canditemp = candi
            bahantemp = [0, 0, 0]
            jumlah = int(0)

            # kita simpan data bahan-bahan yang dibutuhkan pada 'bahantemp'
            # dan kita simpan juga nama pembuat candi pada 'canditemp'
            for i in range (count):
                sand = int(rng.rng(1))
                stone = int(rng.rng(1))
                water = int(rng.rng(1))
                bahantemp[0] += sand
                bahantemp[1] += stone
                bahantemp[2] += water
                jumlah += 1 # variabel ini untuk tracking berapa candi yang telah dibangun

                # jika jumlah candi masih belum 100 maka kita simpan candi yang dibangun
                if canditemp[1][0] - 1 < 100:
                    canditemp = app.myappend(canditemp, [candi[1][0] + i, pembangun[0][i+1][0], sand, stone, water])

            # kalau ternyata bahan yang dimiliki tidak cukup
            if bahantemp[0] > int(bahan[0][idxpasir][2]) or bahantemp[1] > int(bahan[0][idxbatu][2]) or bahantemp[2] > int(bahan[0][idxair][2]):
                print(f"\nBatchbangun gagal. Bahan yang kurang:")

                # kita output bahan apa saja yang kurang
                if int(bahantemp[0]) > int(bahan[0][idxpasir][2]):
                    print(f"-{int(bahantemp[0]) - int(bahan[0][idxpasir][2])} pasir")
                if int(bahantemp[1]) > int(bahan[0][idxbatu][2]):
                    print(f"-{int(bahantemp[1]) - int(bahan[0][idxbatu][2])} batu")
                if int(bahantemp[2]) > int(bahan[0][idxair][2]):
                    print(f"-{int(bahantemp[2]) - int(bahan[0][idxair][2])} air")

            # tetapi jika bahan yang dimiliki cukup
            else:

                # lakukan output sesuai dengan spesifikasi
                print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {bahantemp[0]} pasir, {bahantemp[1]} batu, dan {bahantemp[2]} air.")
                print(f"Jin berhasil membangun total {jumlah} candi.")

                # jika jumlah candi sudah 100
                if canditemp[1][0] == candi[1][0]:
                    print("Tetapi tidak ada candi yang disimpan karena jumlah candi sudah mencapai batas maksimum.")
                elif jumlah > canditemp[1][0] - candi[1][0]:
                    print(f"Tetapi yang disimpan hanya {canditemp[1][0] - candi[1][0]} candi karena jumlah candi sudah mencapai batas maksimum.")

                # dan kita pindahkan 'canditemp' ke 'candi'
                candi = canditemp

                # kemudian kita simpan modifikasi bahan pada matriks 'bahan'
                bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) - bahantemp[0]
                bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) - bahantemp[1]
                bahan[0][idxair][2] = int(bahan[0][idxair][2]) - bahantemp[2]

    # terakhir, kita kembalikan 'candi' dan 'bahan'
    return (candi, bahan)
