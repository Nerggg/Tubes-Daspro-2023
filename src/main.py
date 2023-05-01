# import semua library yang digunakan untuk permainan
import time
import random
import functions.f01 as f01
import functions.f02 as f02
import functions.f03 as f03
import functions.f04 as f04
import functions.f05 as f05
import functions.f06 as f06
import functions.f07 as f07
import functions.f08 as f08
import functions.f09 as f09
import functions.f10 as f10
import functions.f11 as f11
import functions.f12 as f12
import functions.f13 as f13
import functions.f14 as f14
import functions.f15 as f15
import functions.f16 as f16
import utils.mysplit as spl
import utils.myappend as app
import utils.rng as rng

# panggil fungsi 'load' untuk mendefinisikan lokasi dari file game
(proceed, address) = f13.load()

# jika 'proceed' bernilai true berarti permainan dijalankan
if proceed:

    # buka semua file data game
    # dan simpan pada matriksnya masing-masing
    with open (address + '\\user.csv', 'r') as csv:
        user = spl.mysplit(csv.read())

    with open (address + '\\candi.csv', 'r') as csv:
        candi = spl.mysplit(csv.read())

    with open (address + '\\bahan_bangunan.csv', 'r') as csv:
        bahan = spl.mysplit(csv.read())

    # deklarasi username kosong
    usern = str("")

# selama permainan dijalankan
while proceed:

    opsi = input(">>> ")

    match opsi:
        case "login":
            usern = f01.login(usern, user)
        case "logout":
            usern = f02.logout(usern)
        case "summonjin":
            user = f03.summonjin(usern, user)
        case "hapusjin":
            (user, candi) = f04.hapusjin(usern, user, candi)
        case "ubahjin":
            user = f05.ubahjin(usern, user)
        case "bangun":
            (candi, bahan) = f06.bangun(usern, user, candi, bahan)
        case "kumpul":
            bahan = f07.kumpul(usern, user, bahan)
        case "batchkumpul":
            bahan = f08.batchkumpul(usern, user, bahan)
        case "batchbangun":
            (candi, bahan) = f08.batchbangun(usern, user, candi, bahan)
        case "laporanjin":
            f09.laporanjin(usern, user, candi, bahan)
        case "laporancandi":
            f10.laporancandi(usern, candi)
        case "hancurkancandi":
            candi = f11.hancurkancandi(usern, candi)
        case "ayamberkokok":
            proceed = f12.ayamberkokok(usern, candi)
        case "save":
            f14.save(user, candi, bahan, address)
        case "help":
            f15.help(usern, user)
        case "exit":
            proceed = f16.exit(user, candi, bahan, address)
