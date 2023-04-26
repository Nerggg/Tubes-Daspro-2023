from utils import myappend as app

# fungsi ini menerima 'usern' sebagai username pemain saat itu
# dan matriks 'user' yang berisi data seluruh user
def summonjin(usern, user):

    # jika username saat itu bukan Bondowoso
    if usern != "Bondowoso":
        print("Hanya Bandung Bondowoso yang dapat mensummon jin!")
        return user # dan kembalikan 'user' yang belum diedit
        
    # tetapi jika username saat itu adalah Bondowoso
    else:
        # deklarasi array yang berisi username, password, dan role dari jin yang akan disummon
        temp = ["temp", "temp", "temp"]
        
        # input jenis jin yang akan dipanggil dari pemain
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - bertugas membangun candi")
        
        while True: # selama input tidak valid maka permainan akan terus bertanya kepada user
            opt = int(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            if opt == 1:
                print("\nMemilih jin \"Pengumpul\"")
                temp[2] = "jin_pengumpul" # memasukkan jin pengumpul pada bagian role 
                break
            elif opt == 2:
                print("\nMemilih jin \"Pembangun\"")
                temp[2] = "jin_pembangun" # memasukkan jin pembangun pada bagian role 
                break
            else:
                print(f"\nTidak ada jenis jin bernomor: \"{opt}\"!")
                
        # input username jin dari pemain
        namajin = input("\nMasukkan username jin: ")
        
        # cek apakah username sudah diambil atau belum
        userada = False
        for i in range (1, user[1][0]):
            if namajin == user[0][i][0]:
                userada = True
                break
                
        while userada: # jika sudah diambil
            print(f"\nUsername \"{namajin}\" sudah diambil!") 
            namajin = input("\nMasukkan username jin: ") # permainan akan terus meminta pemain untuk mengulangi input
            for i in range (1, user[1][0]): # kemudian dicek ulang apakah username yang barusan diinput sudah diambil atau belum
                if namajin == user[0][i][0]: # jika sudah diambil
                    userada = True # maka loop akan terus mengulang
                    break
                userada = False # tetapi jika belum diambil, maka kita akan keluar dari loop
                
        # input password jin dari pemain
        passjin = input("Masukkan password jin: ")
        while len(passjin) < 5 or len(passjin) > 25: # jika panjang password yang dimasukkan tidak sesuai
            print("\nPassword panjangnya harus 5-25 karakter!")
            passjin = input("Masukkan password jin: ") # maka permainan akan terus meminta pemain untuk mengulangi input
            
        # jika password sudah sesuai
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"\nJin {namajin} berhasil dipanggil!") # maka jin akan dipanggil
        temp[0] = namajin
        temp[1] = passjin
        
        # mengembalikan matriks hasil penambahan 'temp' pada 'user'
        return app.myappend(user, temp) 
