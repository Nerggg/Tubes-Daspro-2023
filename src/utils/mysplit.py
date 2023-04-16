def mysplit(string):
    kolom = int(0)
    baris = int(0)
    temp = str()
    for i in range (len(string)):
        if string[i] == ';':
            kolom += 1
        elif string[i] == '\n':
            kolom += 1
            break
    for i in range (len(string)):
        if string[i] == '\n':
            baris += 1
    arr = [["" for j in range (kolom)] for i in range (baris)]
    arr = [arr, [0,0]]
    arr[1][1] = kolom
    kolom = int(0)
    baris = int(0)
    for i in range (len(string)):
        if string[i] != ';' and string[i] != '\n':
            temp += string[i]
        elif string[i] == ';':
            arr[0][baris][kolom] = temp
            kolom += 1
            temp = str()
        elif string[i] == '\n':
            arr[0][baris][kolom] = temp
            temp = str()
            baris += 1
            kolom = int(0)
            arr[1][0] += 1
    return arr
