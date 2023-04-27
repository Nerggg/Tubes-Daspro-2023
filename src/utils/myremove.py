# fungsi ini menerima 'target' sebagai string nama user yang akan dihapus
# dan matriks 'li' sebagai tempat dimana 'target' akan dihapus
def myremove_user(target, li):

    # deklarasi matriks yang memiliki satu elemen lebih sedikit daripada matriks 'li' yang kita beri nama 'temp'
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-1)]
    temp = [temp, [li[1][0]-1,li[1][1]]]

    # pindahkan semua elemen dari 'li' ke 'temp'
    idx = int(0)
    for i in range (li[1][0]):
        if li[0][i][0] != target: # jika nama pembuat candi tidak sama dengan 'target'
            for j in range (temp[1][1]): # maka elemen tersebut dipindahkan ke 'temp'
                temp[0][idx][j] = li[0][i][j]
            idx += 1

    # mengembalikan 'temp' sebagai hasil
    return temp


# fungsi ini menerima 'target' sebagai string nama pembuat candi yang akan dihapus
# dan matriks 'li' sebagai tempat dimana 'target' akan dihapus
def myremove_candi(target, li):

    # hitung ada berapa candi yang dibangun oleh 'target' dan simpan dalam variabel 'count'
    count = int(0)
    for i in range (1, li[1][0]):
        if li[0][i][1] == target:
            count += 1

    # deklarasi matriks yang memiliki 'count' elemen lebih sedikit daripada matriks 'li' yang kita beri nama 'temp'
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-count)]
    temp = [temp, [li[1][0]-count,li[1][1]]]

    # pindahkan semua elemen dari 'li' ke 'temp'
    idx = int(0)
    for i in range (li[1][0]):
        if li[0][i][1] != target: # jika nama pembuat candi tidak sama dengan 'target'
            for j in range (li[1][1]): # maka elemen tersebut dipindahkan ke 'temp'
                temp[0][idx][j] = li[0][i][j]
                if idx > 0: # ini untuk penomoran id candi
                    temp[0][idx][0] = idx
            idx += 1

    # mengembalikan 'temp' sebagai hasil
    return temp

def myremove_candi_idx(indeks, li):

    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-1)]
    temp = [temp, [li[1][0]-1,li[1][1]]]
    one = int(0)
    for i in range (temp[1][0]):
        if i == indeks:
            one = int(1)
        for j in range (temp[1][1]):
            temp[0][i][j] = li[0][i+one][j]
            if i > 0: # ini untuk penomoran id candi
                temp[0][i][0] = i
    return temp
