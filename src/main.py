import time
import random
import functions.f01 as f01
import functions.f02 as f02
import functions.f03 as f03
import functions.f04 as f04
import functions.f05 as f05
import functions.f06 as f06
import functions.f07 as f07
import functions.f14 as f14
import utils.mysplit as spl
import utils.myappend as app
import utils.rng as rng

with open ('user.csv', 'r') as csv:
    user = spl.mysplit(csv.read())

with open ('candi.csv', 'r') as csv:
    candi = spl.mysplit(csv.read())

with open ('bahan_bangunan.csv', 'r') as csv:
    bahan = spl.mysplit(csv.read())

# Deklarasi username kosong
usern = str("null")

while True:

    opsi = input(">>> ")

    if opsi == "login":
        usern = f01.login(usern, user)
    elif opsi == "logout":
        usern = f02.logout(usern)
    elif opsi == "summonjin":
        user = f03.summonjin(usern, user)
    elif opsi == "hapusjin":
        (user, candi) = f04.hapusjin(usern, user, candi)
    elif opsi == "ubahjin":
        user = f05.ubahjin(usern, user)
    elif opsi == "bangun":
        (candi, bahan) = f06.bangun(usern, user, candi, bahan)
    elif opsi == "kumpul":
        bahan = f07.kumpul(usern, user, bahan)
    elif opsi == "save":
        f14.save(user, candi, bahan)
    elif opsi == "print":
        print(candi)
