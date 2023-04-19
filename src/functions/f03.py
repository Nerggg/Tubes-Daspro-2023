from utils import myappend as app

def summonjin(usern, user):
    if usern != "Bondowoso":
        print("Hanya Bandung Bondowoso yang dapat mensummon jin!")
        return user
    else:
        temp = ["temp", "temp", "temp"]
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - bertugas membangun candi")
        while True:
            opt = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            if opt == 1:
                print("\nMemilih jin \"Pengumpul\"")
                temp[2] = "jin_pengumpul"
                break
            elif opt == 2:
                print("\nMemilih jin \"Pembangun\"")
                temp[2] = "jin_pembangun"
                break
            else:
                print(f"\nTidak ada jenis jin bernomor: \"{opt}\"!")
        namajin = input("\nMasukkan username jin: ")
        userada = False
        for i in range (1, user[1][0]):
            if namajin == user[0][i][0]:
                userada = True
                break
        while userada:
            print(f"\nUsername \"{namajin}\" sudah diambil!")
            namajin = input("\nMasukkan username jin: ")
            for i in range (1, user[1][0]):
                if namajin == user[0][i][0]:
                    userada = True
                    break
                userada = False
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
        temp[0] = namajin
        temp[1] = passjin
        return app.myappend(user, temp)
