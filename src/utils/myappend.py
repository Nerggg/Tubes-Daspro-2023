def myappend(target, li):
    temp = [["" for i in range (target[1][1])] for j in range (target[1][0]+1)]
    temp = [temp, [target[1][0]+1,target[1][1]]]
    for i in range (target[1][0]):
        for j in range (target[1][1]):
            temp[0][i][j] = target[0][i][j]
    for i in range (target[1][1]):
        temp[0][target[1][0]][i] = li[i]
    return temp
