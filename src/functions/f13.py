import argparse
import os

# fungsi ini bertujuan untuk mendefinisikan alamat lokasi dari file data game 
# dan fungsi ini dijalankan dengan argparse
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", nargs = '?', help = "Folder lokasi database game.")
    args = parser.parse_args()
    
    # jika tidak ada argumen yang diberikan
    if args.nama_folder is None:
    
        # lakukan output sesuai dengan spesifikasi
        print("Tidak ada nama folder yang diberikan!\n\nUsage: python main.py <nama_folder>")
        return (False, "")
        
    # tetapi jika ada argumen yang diberikan
    else:
    
        # simpan argumen tersebut pada string 'address'
        address = args.nama_folder
    
        # cek apakah lokasi tersebut memang ada atau tidak
        if os.path.exists(address) and os.path.isdir(address):
        
            # jika lokasi ada dan file data game ada disana
            if os.path.isfile(address + "\\user.csv") and os.path.isfile(address + "\\candi.csv") and os.path.isfile(address + "\\bahan_bangunan.csv"):
                # maka permainan dijalankan
                print("\nLoading...\n\nGame telah dimuat!\nSelamat Bermain!\n")  
                return (True, address) # dan kembalikan string 'address'
                
            # tetapi jika lokasi ada tetapi file data game tidak ada disana
            else:
                # maka permainan tidak dijalankan
                print("Tidak ada database game di folder ini.")
                return (False, "")
                
        # tetapi jika folder game tidak ditemukan
        else:
        
            # lakukan output pemberitahuan
            print(f"Folder \"{address}\" tidak ditemukan.")
            return (False, "")
