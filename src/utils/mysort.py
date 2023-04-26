# fungsi ini menerima 'li' sebagai matriks yang akan disorting
def stringsort(li):
    
    # sorting dengan algoritma bubble sort
    for i in range(li[1][0]):
        for j in range(1, li[1][0]):
            if li[0][j-1] > li[0][j]: # ketika elemen selanjutnya memiliki nilai lebih besar
                (li[0][j-1], li[0][j]) = (li[0][j], li[0][j-1]) # maka kedua elemen tersebut ditukar
                
    # mengembalikan 'li' sebagai hasil
    return li
