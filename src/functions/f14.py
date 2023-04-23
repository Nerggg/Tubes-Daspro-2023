def save(user, candi, bahan, address):
    with open(address + '\\user.csv', 'w') as csv:

        for i in range(user[1][0]):
            row = user[0][i][0] + ';' + user[0][i][1] + ';' + user[0][i][2] + '\n'
            csv.write(row)

    with open(address + '\\bahan_bangunan.csv', 'w') as csv:

        for i in range(bahan[1][0]):
            row = bahan[0][i][0] + ';' + bahan[0][i][1] + ';' + str(bahan[0][i][2]) + '\n'
            csv.write(row)

    with open(address + '\\candi.csv', 'w') as csv:

        for i in range(candi[1][0]):
            row = str(candi[0][i][0]) + ';' + candi[0][i][1] + ';' + str(candi[0][i][2]) + ';' + str(candi[0][i][3]) + ';' + str(candi[0][i][4]) + '\n'
            csv.write(row)

    print("Save berhasil!")
