def login():
    global usernames, passwords, amount, usern
    if usern != "null":
        print("Anda harus logout terlebih dahulu sebelum login ke akun lain!")
    else:
        usern = str(input("Username: "))
        passw = str(input("Password: "))
        if usern not in usernames:
            print("Username tidak terdaftar!")
        elif usern in usernames and passw not in passwords:
            print("Password salah!")
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
    global usernames, passwords, roles
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

def save():
    global usernames, passwords, roles, amount
    # membuka file csv untuk ditulis
    with open('user.csv', mode = 'w') as file:

    # menuliskan data
        for i in range(amount):
            row = usernames[i] + ';' + passwords[i] + ';' + roles[i] + '\n'
            file.write(row)
            print("saving")

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

# Deklarasi username kosong
usern = str("null")

while True:
    # Mendapatkan jumlah akun
    amount = int(0)
    for i in usernames:
        amount += 1

    opsi = input(">>> ")

    if opsi == "login":
        login()
    elif opsi == "logout":
        logout()
    elif opsi == "summonjin":
        summonjin()
    elif opsi == "save":
        save()
    elif opsi == "print":
        print(usernames)
        print(passwords)
        print(roles)
        print(amount)
