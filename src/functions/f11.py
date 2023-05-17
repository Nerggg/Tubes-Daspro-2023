from utils import myremove as myr

def hancurkancandi(usern, candi):
    if usern == "Roro":
        hancurkan = int(input("Masukkan ID candi: "))
        if hancurkan <= candi[1][0] - 1:
            while True:
                opt = str(input(f"Apakah anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? "))
                if opt == "y" or opt == "Y":
                    print("\nCandi telah berhasil dihancurkan.")
                    candi = myr.myremove_candi_idx(hancurkan, candi)
                elif opt == "n" or opt == "N":
                    print("\nCandi tidak dihancurkan.")
                break
        else:
            print("Tidak ada candi dengan ID tersebut.")
    else:
        print("Hanya Roro Jonggrang yang dapat menghancurkan candi.")
    return candi
