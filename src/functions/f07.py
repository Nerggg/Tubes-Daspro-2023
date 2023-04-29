import random
from utils import myappend as app
from utils import rng

# fungsi ini menerima 'usern' sebagai username pemain saat itu,
# matriks 'user' yang berisi data seluruh pemain
# dan matriks 'bahan' yang berisi data bahan yang dimiliki oleh pemain
def kumpul(usern, user, bahan):

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
                
        # jika bukan jin pengumpul maka
        if user[0][index][2] != "jin_pengumpul":
            print("Hanya jin pengumpul yang dapat mengumpulkan bahan bangunan!")
            
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
                
            # kemudian kita gunakan rng untuk menghasilkan jumlah bahan yang dikumpulkan
            sand = int(rng.rng(0))
            stone = int(rng.rng(0))
            water = int(rng.rng(0))
            
            # setelah itu kita simpan semua bahan pada matriks 'bahan'
            print(f"Jin menemukan {sand} pasir, {stone} batu, dan {water} air.")
            bahan[0][idxpasir][2] = int(bahan[0][idxpasir][2]) + sand
            bahan[0][idxbatu][2] = int(bahan[0][idxbatu][2]) + stone
            bahan[0][idxair][2] = int(bahan[0][idxair][2]) + water

    # kemudain kita kembalikan matriks 'bahan'
    return bahan
