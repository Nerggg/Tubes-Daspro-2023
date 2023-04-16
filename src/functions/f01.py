def login(usern, user):
    if usern != "null":
        print("Anda harus logout terlebih dahulu sebelum login ke akun lain!")
        return usern
    else:
        temp = usern
        userada = False
        passada = False
        usern = str(input("Username: "))
        passw = str(input("Password: "))
        for i in range (1, user[1][0]):
            if usern == user[0][i][0]:
                userada = True
                break
        for i in range (1, user[1][0]):
            if passw == user[0][i][1]:
                passada = True
                break
        if not userada:
            print("Username tidak terdaftar!")
            return temp
        elif userada and not passada:
            print("Password salah!")
            return temp
        else:
            print(f"Selamat datang, {usern}!")
            return usern
