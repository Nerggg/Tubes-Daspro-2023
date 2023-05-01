from functions import f14

# fungsi ini menerima matriks 'user' yang berisi data seluruh user,
# matriks 'candi' yang berisi data candi yang telah dibangun,
# matriks 'bahan' yang berisi bahan-bahan yang dimiliki pemain,
# dan string 'address' yang berisi alamat lokasi file data game
def exit(user, candi, bahan, address):

    # bertanya kepada pemain apakah ingin menyimpan game atau tidak
    opt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")

    # jika ingin menyimpan game maka
    if opt == 'y':
        f14.save(user, candi, bahan, address) # kita panggil fungsi save

    # mengembalikan 'false' agar program berhenti
    return False
