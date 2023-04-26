# fungsi ini menerima 'string' sebagai string yang akan di split 
def mysplit(string):

    # hitung jumlah kolom dan baris pada 'string'
    kolom = int(0)
    baris = int(0)
    temp = str()
    for i in range (len(string)):
        if string[i] == ';': # kolom ditandai oleh denumerator semicolon
            kolom += 1
        elif string[i] == '\n':
            kolom += 1
            break
    for i in range (len(string)):
        if string[i] == '\n':  # dan baris ditandai oleh '\n'
            baris += 1
            
    # deklarasi matriks berdimensi kolom x baris
    arr = [["" for j in range (kolom)] for i in range (baris)]
    
    # kemudian menetapkan nilai efektif pada elemen arr[1][0]
    arr = [arr, [0,0]]
    
    # dan jumlah kolom pada elemen arr[1][1]
    arr[1][1] = kolom
    
    # setelah matriksnya dibuat, sekarang kita memisahkan 'string' menurut denumerator semicolon
    # dan menyimpannya pada matriks tadi
    kolom = int(0)
    baris = int(0)
    for i in range (len(string)):
        if string[i] != ';' and string[i] != '\n': # ketika elemen 'string' tidak sama dengan semicolon atau '\n'
            temp += string[i] # kita tambahkan elemen tersebut pada temp
        elif string[i] == ';': # kemudian ketika elemennya sudah sama dengan semicolon
            arr[0][baris][kolom] = temp # temp dimasukkan pada matriks,
            kolom += 1 # jumlah kolomnya ditambah satu,
            temp = str() # dan temp dikosongkan kembali
        elif string[i] == '\n': # kemudian ketika elemennya sama dengan '\n' 
            arr[0][baris][kolom] = temp # temp dimasukkan pada matriks,
            temp = str() # temp dikosongkan,
            baris += 1 # jumlah baris ditambahkan satu,
            kolom = int(0) # kolomnya dimulai dari nol lagi, 
            arr[1][0] += 1 # dan nilai efektif bertambah satu
            
    # mengembalikan 'arr' sebagai hasil
    return arr
