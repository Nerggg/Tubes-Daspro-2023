# fungsi ini menerima 'usern' sebagai username pemain saat itu
# dan matriks 'user' yang berisi data seluruh user 
def login(usern, user):

    # validasi username apakah kosong atau tidak
    if usern != "": # jika username tidak kosong
        print("Anda harus logout terlebih dahulu sebelum login ke akun lain!") # berarti pemain sudah login ke akun lain dan harus logout terlebih dahulu
        return usern
        
    else: # tetapi jika username kosong
    
        userada = False
        passada = False
        idx = int(0)
        
        # input username dan password pemain
        usern = str(input("Username: "))
        passw = str(input("Password: "))
        
        # lakukan pengecekan username pada matriks 'user'
        for i in range (1, user[1][0]): # cek username pada 'user' dengan loop
            if usern == user[0][i][0]: # jika username tersebut ada pada 'user'
                userada = True # ubah 'userada' menjadi true
                idx = i # dan simpan index username pada variabel idx
                break
        
        # kemudian cek password pada matriks 'user'
        if passw == user[0][idx][1]: # jika password sesuai
            passada = True # ubah 'passada' menjadi true
            
        if not userada: # jika username tidak ada
            print("Username tidak terdaftar!")
            return ""
            
        elif userada and not passada: # jika username ada tetapi password salah
            print("Password salah!")
            return ""
            
        else: # jika username ada dan password benar
            print(f"Selamat datang, {usern}!")
            return usern
