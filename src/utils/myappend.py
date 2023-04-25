# fungsi ini menerima parameter 'target' sebagai matriks tujuan
# dan 'li' sebagai list yang memiliki jumlah elemen sama dengan jumlah kolom 'target'
def myappend(target, li):    

    # deklarasi matriks yang memiliki satu elemen lebih banyak daripada 'target' yang kita beri nama 'temp'
    temp = [["" for i in range (target[1][1])] for j in range (target[1][0]+1)]
    temp = [temp, [target[1][0]+1,target[1][1]]] # dan menambahkan nilai efektifnya dengan satu

    # memindahkan semua elemen 'target' ke dalam 'temp' menggunakan loop
    for i in range (target[1][0]): # pengulangan sebanyak nilai efektif 'target'
        for j in range (target[1][1]): # pengulangan sebanyak jumlah kolom 'target'
            temp[0][i][j] = target[0][i][j]
            
    # kemudian pada elemen terakhir dari 'temp' kita masukkan elemen dari 'li'
    for i in range (target[1][1]): # pengulangan sebanyak jumlah kolom 'target'
        temp[0][target[1][0]][i] = li[i]
    
    # mengembalikan 'temp' sebagai hasil penambahan 
    return temp
