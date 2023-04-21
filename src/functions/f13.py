import argparse
import os

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", nargs = '?', help = "Folder lokasi database game.")
    args = parser.parse_args()
    if args.nama_folder is None:
        print("Tidak ada nama folder yang diberikan!\n\nUsage: python main.py <nama_folder>")
        return (False, "")
    else:
        address = args.nama_folder
        if os.path.exists(address) and os.path.isdir(address):
            if os.path.isfile(address + "\\user.csv") and os.path.isfile(address + "\\candi.csv") and os.path.isfile(address + "\\bahan_bangunan.csv"):
                print("\nLoading...\n\nGame telah dimuat!\nSelamat Bermain!\n")
                return (True, address)
            else:
                print("Tidak ada database game di folder ini.")
                return (False, "")
        else:
            print(f"Folder \"{address}\" tidak ditemukan.")
            return (False, "")
