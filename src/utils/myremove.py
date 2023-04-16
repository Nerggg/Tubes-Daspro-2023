def myremove_user(target, li):
    count = int(0)
    for i in range (1, li[1][0]):
        if li[0][i][0] == target:
            count += 1
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-count)]
    temp = [temp, [li[1][0]-count,li[1][1]]]
    for i in range (temp[1][0]):
        if li[0][i][0] == target:
            continue
        else:
            for j in range (temp[1][1]):
                temp[0][i][j] = li[0][i][j]
    return temp

def myremove_candi(target, li):
    count = int(0)
    for in range (1, li[1][0]):
        if if[0][i][1] == target:
            count += 1
    temp = [["" for i in range (li[1][1])] for j in range (li[1][0]-count)]
    temp = [temp, [li[1][0]-count,li[1][1]]]
    for i in range (temp[1][0]):
        if li[0][i][1] == target:
            continue
        else:
            for j in range (temp[1][1]):
                temp[0][i][j] = li[0][i][j]
    return temp
