import random
from utils import myappend as app
from utils import rng

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# dan matriks 'bahan' yang berisi data bahan yang dimiliki oleh pemain
def bangun(usern, user, candi, bahan):

    # cek username pemain terlebih dahulu
    # jika username kosong berarti pemain belum login
    if usern == "":
        print("Lakukan login terlebih dahulu!")

    # tetapi jika username pemain tidak kosong
    else:

        # kita cek role dari karakter yang digunakan oleh pemain saat itu
        for i in range (1, user[1][0]):
            if usern == user[0][i][0]:
                index = i
                break

        # jika bukan jin pembangun maka
        if user[0][index][2] != "jin_pembangun":
            print("Hanya jin pembangun yang dapat membangun candi!")

        # tetapi jika karakter adalah jin pembangun
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

            # kemudian kita gunakan rng untuk menghasilkan jumlah bahan yang dibutuhkan
            stone = int(rng.rng(1))
            sand = int(rng.rng(1))
            water = int(rng.rng(1))
            bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2])
            bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2])
            bahan[0][idxair][2] = int(bahan[0][idxair][2])

            # lalu kita cek apakah bahan-bahannya mencukupi atau tidak
            # jika tidak mencukupi maka
            if bahan[0][idxpasir][2] < sand or bahan[0][idxbatu][2] < stone or bahan[0][idxair][2] < water:
                print("Bahan bangunan tidak mencukupi")
                print("Candi tidak bisa dibangun!")

            # tetapi jika ternyata bahannya mencukupi
            else:

                # jika candi yang dibangun belum mencapai 100
                if candi[1][0] - 1 < 100:
                    print(f"Candi berhasil dibangun dan menggunakan {sand} pasir, {stone} batu, dan {water} air.")
                    print(f"Sisa candi yang perlu dibangun: {100 - candi[1][0]}.")

                    # kita ganti jumlah bahan-bahan pada matriks 'bahan'
                    bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) - sand
                    bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) - stone
                    bahan[0][idxair][2] = int(bahan[0][idxair][2]) - water

                    # dan kita tambahkan candi yang telah dibangun pada matriks 'candi'
                    li = [candi[1][0], usern, sand, stone, water]
                    candi = app.myappend(candi, li)

                # tetapi jika candi yang dibangun sudah mencapai 100
                else:
                    print(f"Candi berhasil dibangun dan menggunakan {sand} pasir, {stone} batu, dan {water} air.")
                    print("Tetapi candi tidak disimpan karena jumlah candi yang dibangun sudah 100.")

                    # kita ganti jumlah bahan-bahan pada matriks 'bahan'
                    bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) - sand
                    bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) - stone
                    bahan[0][idxair][2] = int(bahan[0][idxair][2]) - water

    # mengembalikan matriks 'candi' dan 'bahan'
    return (candi, bahan)
