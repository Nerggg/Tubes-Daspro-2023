import os

# fungsi ini menerima matriks 'user' yang berisi data seluruh user,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# matriks 'bahan' yang berisi bahan-bahan yang dimiliki pemain,
# dan string 'address' yang berisi alamat lokasi file data game
def save(user, candi, bahan, address):

    print("(ketik \"./save\" jika kamu ingin menyimpan di direktori yang sama dengan sebelumnya)")
    foldername = input("Masukkan nama folder: ")

    folder = "\\" + foldername

    print("\nSaving...")

    if foldername == "./save":

        # buka file 'user.csv'
        with open(address + '\\user.csv', 'w') as csv:

            for i in range(user[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'user'
                row = user[0][i][0] + ';' + user[0][i][1] + ';' + user[0][i][2] + '\n' # deklarasi string row yang berisi satu kolom user
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'bahan_bangunan.csv'
        with open(address + '\\bahan_bangunan.csv', 'w') as csv:

            for i in range(bahan[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'bahan'
                row = bahan[0][i][0] + ';' + bahan[0][i][1] + ';' + str(bahan[0][i][2]) + '\n' # deklarasi string row yang berisi satu kolom bahan
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'candi.csv'
        with open(address + '\\candi.csv', 'w') as csv:

            for i in range(candi[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'candi'
                # deklarasi string row yang berisi satu kolom candi
                row = str(candi[0][i][0]) + ';' + candi[0][i][1] + ';' + str(candi[0][i][2]) + ';' + str(candi[0][i][3]) + ';' + str(candi[0][i][4]) + '\n'
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # output pemberitahuan keberhasilan save
        print(f"\nBerhasil menyimpan data di folder {address}\n")

    elif os.path.exists(address + folder) and os.path.isdir(address + folder):

        # buka file 'user.csv'
        with open(address + '\\user.csv', 'w') as csv:

            for i in range(user[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'user'
                row = user[0][i][0] + ';' + user[0][i][1] + ';' + user[0][i][2] + '\n' # deklarasi string row yang berisi satu kolom user
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'bahan_bangunan.csv'
        with open(address + '\\bahan_bangunan.csv', 'w') as csv:

            for i in range(bahan[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'bahan'
                row = bahan[0][i][0] + ';' + bahan[0][i][1] + ';' + str(bahan[0][i][2]) + '\n' # deklarasi string row yang berisi satu kolom bahan
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'candi.csv'
        with open(address + '\\candi.csv', 'w') as csv:

            for i in range(candi[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'candi'
                # deklarasi string row yang berisi satu kolom candi
                row = str(candi[0][i][0]) + ';' + candi[0][i][1] + ';' + str(candi[0][i][2]) + ';' + str(candi[0][i][3]) + ';' + str(candi[0][i][4]) + '\n'
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # output pemberitahuan keberhasilan save
        print(f"\nBerhasil menyimpan data di folder {address + folder}\n")

    else:

        print(f"\nMembuat folder {address + folder}...\n")

        os.mkdir(os.path.join(address, foldername))

        # buka file 'user.csv'
        with open(address + folder + '\\user.csv', 'w') as csv:

            for i in range(user[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'user'
                row = user[0][i][0] + ';' + user[0][i][1] + ';' + user[0][i][2] + '\n' # deklarasi string row yang berisi satu kolom user
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'bahan_bangunan.csv'
        with open(address  + folder + '\\bahan_bangunan.csv', 'w') as csv:

            for i in range(bahan[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'bahan'
                row = bahan[0][i][0] + ';' + bahan[0][i][1] + ';' + str(bahan[0][i][2]) + '\n' # deklarasi string row yang berisi satu kolom bahan
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # buka file 'candi.csv'
        with open(address   + folder + '\\candi.csv', 'w') as csv:

            for i in range(candi[1][0]): # lakukan looping sebanyak jumlah baris pada matriks 'candi'
                # deklarasi string row yang berisi satu kolom candi
                row = str(candi[0][i][0]) + ';' + candi[0][i][1] + ';' + str(candi[0][i][2]) + ';' + str(candi[0][i][3]) + ';' + str(candi[0][i][4]) + '\n'
                csv.write(row) # menuliskan row yang telah dibuat pada csv

        # output pemberitahuan keberhasilan save
        print(f"\nBerhasil menyimpan data di folder {address + folder}\n")

