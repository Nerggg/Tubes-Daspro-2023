def stringsort(li):
    for i in range(li[1][0]):
        for j in range(1, li[1][0]):
            if li[0][j-1] > li[0][j]:
                temp = li[0][j-1]
                li[0][j-1] = li[0][j]
                li[0][j] = temp
    return li
