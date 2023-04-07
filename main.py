import time
import random
def rng(n):
    return random.randint(n,5)

def login():
    global usernames, passwords, usern
    if usern != "null":
        print("Anda harus logout terlebih dahulu sebelum login ke akun lain!")
    else:
        usern = str(input("Username: "))
        passw = str(input("Password: "))
        if usern not in usernames:
            print("Username tidak terdaftar!")
            usern = "null"
        elif usern in usernames and passw not in passwords:
            print("Password salah!")
            usern = "null"
        else:
            print(f"Selamat datang, {usern}!")

def logout():
    global usern
    if usern == "null":
        print("Anda belum login!")
    else:
        print("Logout berhasil!")
        usern = "null"

def summonjin():
    global usernames, passwords, usern, roles
    if usern == "Bondowoso":
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - bertugas membangun candi")
        while True:
            opt = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            if opt == 1:
                print("\nMemilih jin \"Pengumpul\"")
                roles.append("jin_pengumpul")
                break
            elif opt == 2:
                print("\nMemilih jin \"Pembangun\"")
                roles.append("jin_pembangun")
                break
            else:
                print(f"\nTidak ada jenis jin bernomor: \"{opt}\"!")

        namajin = input("\nMasukkan username jin: ")
        while namajin in usernames:
            print(f"\nUsername \"{namajin}\" sudah diambil!")
            namajin = input("\nMasukkan username jin: ")
        passjin = input("Masukkan password jin: ")
        passlen = 0
        for i in passjin:
            passlen += 1
        while passlen < 5 or passlen > 25:
            print("\nPassword panjangnya harus 5-25 karakter!")
            passjin = input("Masukkan password jin: ")
            passlen = 0
            for i in passjin:
                passlen += 1
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"\nJin {namajin} berhasil dipanggil!")
        usernames.append(namajin)
        passwords.append(passjin)
    else:
        print("Hanya Bandung Bondowoso yang dapat melakukan summon jin!")

def hapusjin():
    global usernames, passwords, usern, roles
    if usern == "Bondowoso":
        hapus = str(input("Masukkan username jin : "))
        if hapus in usernames:
            while True:
                print(f"Apakah anda yakin ingin menghapus jin dengan username {hapus} (Y/N)?", end = " ")
                opt = str(input())
                if opt == "y" or opt == "Y":
                    print("\nJin telah berhasil dihapus dari alam gaib.")
                    passwords.pop(usernames.index(hapus))
                    roles.pop(usernames.index(hapus))
                    usernames.remove(hapus)
                    break
                elif opt == "n" or opt == "N":
                    print("\nPenghapusan jin dibatalkan.")
                    break
        else:
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bandung Bondowoso yang dapat menghapus jin!")

def ubahjin():
    global usernames, passwords, usern, roles
    if usern == "Bondowoso":
        ubah = str(input("Masukkan username jin : "))
        if ubah in usernames:
            if roles[usernames.index(ubah)] == "jin_pengumpul":
                while True:
                    opt = str(input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? "))
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        roles[usernames.index(ubah)] = "jin_pembangun"
                        break
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
            elif roles[usernames.index(ubah)] == "jin_pembangun":
                while True:
                    opt = str(input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? "))
                    if opt == "y" or opt == "Y":
                        print("\nJin telah berhasil diubah.")
                        roles[usernames.index(ubah)] = "jin_pengumpul"
                        break
                    elif opt == "n" or opt == "N":
                        print("\nPengubahan jin dibatalkan.")
                        break
        else:
            print("Tidak ada jin dengan username tersebut.")
    else:
        print("Hanya Bandung Bondowoso yang dapat mengubah jin!")

def bangun():
    global usernames, usern, roles, ids, pembuat, pasir, batu, air, jumlah, bahanamount
    if usern == "null":
        print("Lakukan login terlebih dahulu!")
    else:
        if roles[usernames.index(usern)] != "jin_pembangun":
            print("Hanya jin pembangun yang dapat membangun candi!")
        else:
            if bahanamount == 1:
                print("Bahan bangunan tidak mencukupi")
                print("Candi tidak bisa dibangun!")
            else:
                sand = int(rng(1))
                stone = int(rng(1))
                water = int(rng(1))
                jumlah[1] = int(jumlah[1])
                jumlah[2] = int(jumlah[2])
                jumlah[3] = int(jumlah[3])
                if jumlah[1] < sand or jumlah[2] < stone or jumlah[3] < water:
                    print("Bahan bangunan tidak mencukupi")
                    print("Candi tidak bisa dibangun!")
                else:
                    print(f"Candi berhasil dibangun dan menggunakan {sand} pasir, {stone} batu, dan {water} air.")
                    print("Sisa candi yang perlu dibangun: .")
                    jumlah[1] -= sand
                    jumlah[2] -= stone
                    jumlah[3] -= water


def kumpul():
    global usernames, usern, roles, nama, jumlah
    if usern == "null":
        print("Lakukan login terlebih dahulu!")
    else:
        if roles[usernames.index(usern)] != "jin_pengumpul":
            print("Hanya jin pengumpul yang dapat mengumpulkan bahan bangunan!")
        else:
            if "pasir" not in nama:
                nama.append("pasir")
                jumlah.append(int(0))
                deskripsi.append("")
            if "batu" not in nama:
                nama.append("batu")
                jumlah.append(int(0))
                deskripsi.append("")
            if "air" not in nama:
                nama.append("air")
                jumlah.append(int(0))
                deskripsi.append("")
            sand = int(rng(0))
            stone = int(rng(0))
            water = int(rng(0))
            print(f"Jin menemukan {sand} pasir, {stone} batu, dan {water} air.")
            jumlah[1] = int(jumlah[1])
            jumlah[2] = int(jumlah[2])
            jumlah[3] = int(jumlah[3])
            jumlah[1] += sand
            jumlah[2] += stone
            jumlah[3] += water




def save():
    global usernames, passwords, roles, useramount, ids, pembuat, pasir, batu, air, nama, deskripsi, jumlah
    # membuka file csv untuk ditulis
    with open('user.csv', mode = 'w') as file:

    # menuliskan data
        for i in range(useramount):
            row = usernames[i] + ';' + passwords[i] + ';' + roles[i] + '\n'
            file.write(row)

    with open('bahan_bangunan.csv', mode = 'w') as file:

    # menuliskan data
        for i in range(bahanamount):
            row = nama[i] + ';' + deskripsi[i] + ';' + str(jumlah[i]) + '\n'
            file.write(row)


# Buka file CSV dalam mode baca
with open('user.csv', 'r') as csv_file:
    # Baca isi file
    csv_data = csv_file.read()

    # Inisialisasi beberapa variabel
    usernames = []
    passwords = []
    roles = []
    current_column = ''
    current_row = ''
    in_quotes = False

    # Iterasi setiap karakter dalam data CSV
    for char in csv_data:
        # Periksa apakah saat ini berada di dalam string yang diapit oleh tanda kutip ("")
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False

        # Periksa apakah sudah mencapai akhir kolom
        if char == ',' and not in_quotes:
            current_row += current_column.strip() + ';'
            current_column = ''
        elif char == '\n' and not in_quotes:
            current_row += current_column.strip()
            # Pisahkan data pada setiap baris menjadi list
            row_data = current_row.split(';')
            # Ambil setiap data pada list dan masukkan ke list usernames, passwords, dan roles
            usernames.append(row_data[0])
            passwords.append(row_data[1])
            roles.append(row_data[2])
            current_column = ''
            current_row = ''
        else:
            current_column += char

# Buka file CSV dalam mode baca
with open('candi.csv', 'r') as csv_file:
    # Baca isi file
    csv_data = csv_file.read()

    # Inisialisasi beberapa variabel
    ids = []
    pembuat = []
    pasir = []
    batu = []
    air = []
    current_column = ''
    current_row = ''
    in_quotes = False

    # Iterasi setiap karakter dalam data CSV
    for char in csv_data:
        # Periksa apakah saat ini berada di dalam string yang diapit oleh tanda kutip ("")
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False

        # Periksa apakah sudah mencapai akhir kolom
        if char == ',' and not in_quotes:
            current_row += current_column.strip() + ';'
            current_column = ''
        elif char == '\n' and not in_quotes:
            current_row += current_column.strip()
            # Pisahkan data pada setiap baris menjadi list
            row_data = current_row.split(';')
            # Ambil setiap data pada list dan masukkan ke list usernames, passwords, dan roles
            ids.append(row_data[0])
            pembuat.append(row_data[1])
            pasir.append(row_data[2])
            batu.append(row_data[3])
            air.append(row_data[4])
            current_column = ''
            current_row = ''
        else:
            current_column += char

# Buka file CSV dalam mode baca
with open('bahan_bangunan.csv', 'r') as csv_file:
    # Baca isi file
    csv_data = csv_file.read()

    # Inisialisasi beberapa variabel
    nama = []
    deskripsi = []
    jumlah = []
    current_column = ''
    current_row = ''
    in_quotes = False

    # Iterasi setiap karakter dalam data CSV
    for char in csv_data:
        # Periksa apakah saat ini berada di dalam string yang diapit oleh tanda kutip ("")
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False

        # Periksa apakah sudah mencapai akhir kolom
        if char == ',' and not in_quotes:
            current_row += current_column.strip() + ';'
            current_column = ''
        elif char == '\n' and not in_quotes:
            current_row += current_column.strip()
            # Pisahkan data pada setiap baris menjadi list
            row_data = current_row.split(';')
            # Ambil setiap data pada list dan masukkan ke list usernames, passwords, dan roles
            nama.append(row_data[0])
            deskripsi.append(row_data[1])
            jumlah.append(row_data[2])
            current_column = ''
            current_row = ''
        else:
            current_column += char

# Deklarasi username kosong
usern = str("null")

while True:
    # Mendapatkan jumlah akun
    useramount = int(0)
    for i in usernames:
        useramount += 1
    candiamount = int(0)
    for i in ids:
        candiamount += 1
    bahanamount = int(0)
    for i in nama:
        bahanamount += 1

    opsi = input(">>> ")

    if opsi == "login":
        login()
    elif opsi == "logout":
        logout()
    elif opsi == "summonjin":
        summonjin()
    elif opsi == "hapusjin":
        hapusjin()
    elif opsi == "ubahjin":
        ubahjin()
    elif opsi == "bangun":
        bangun()
    elif opsi == "kumpul":
        kumpul()
    elif opsi == "save":
        save()
    elif opsi == "print":
        print(usernames)
        print(passwords)
        print(roles)
        print(amount)
