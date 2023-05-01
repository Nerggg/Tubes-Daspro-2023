from functions import f14

# fungsi ini menerima matriks 'user' yang berisi data seluruh user,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# matriks 'bahan' yang berisi bahan-bahan yang dimiliki pemain,
# dan string 'address' yang berisi alamat lokasi file data game
def exit(user, candi, bahan, address):

    opt = str()

    # bertanya kepada pemain apakah ingin menyimpan game atau tidak
    # selama input tidak valid maka program akan terus bertanya kepada pemain
    while True:
        opt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
        if opt == 'y' or opt == 'Y' or opt == 'n' or opt == 'N':
            break

    if opt == 'y' or opt == 'Y':
        f14.save(user, candi, bahan, address) # kita panggil fungsi save

    # mengembalikan 'false' agar program berhenti
    return False
