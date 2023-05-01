from functions import f14
def exit(user, candi, bahan, address):
    opt = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
    if opt == 'y':
        f14.save(user, candi, bahan, address)
    return False
