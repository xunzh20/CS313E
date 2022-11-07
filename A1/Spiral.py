import sys
def creat_spiral (x):
    spiral = [[0 for i in range (x)]for j in range (x)]
    step = 1
    num = 2
    col = row = x//2
    spiral[row][col] = 1
    for i in range (x//2):
        for j in range (step):
            col +=1
            spiral[row][col] = num
            num +=1 
        for k in range (step):
            row +=1
            spiral[row][col] = num
            num +=1
        step +=1
        for m in range (step):
            col -=1
            spiral[row][col] = num
            num +=1
        for n in range (step):
            row -=1
            spiral[row][col] = num
            num +=1
        step +=1
    for g in range (step-1):
        col += 1
        spiral[row][col] = num
        num +=1
    return spiral

def sum_adjacent_numbers (spiral, n):
    sums = 0
    col = 0
    row = 0
    leng = len(spiral)
    for i in range (leng):
        if n in spiral[i]:
            row = i
            col = spiral[i].index(n)
    if (row != 0 and row !=leng-1 and col != leng-1 and col != 0):
        row -=1
        col -=1
        for j in range(3):
            for k in range (3):
                if spiral[row+j][col+k] != n:
                    sums += spiral[row+j][col+k]
        return sums
                    
    # Four edge cases
    if ( row == 0 and col == 0):
        return  spiral[0][1] + spiral[1][0]+spiral[1][1]
    elif ( row == 0 and col == leng-1):
        return  spiral[0][leng-2] + spiral[1][leng-1]+spiral[1][leng-2]
    elif (row == leng-1 and col == 0):
        return spiral[leng-1][1] + spiral[leng-2][0]+spiral[leng-2][1]
    elif (row == leng-1 and col == leng-1):
        return spiral[leng-1][leng-2] + spiral[leng-2][leng-1]+spiral[leng-2][leng-2]
    # Four boundaries cases
    if (row == 0 and (col != 0 or col != leng-1)):
        col -=1 
        for k in range (2):
            for l in range (3):
                if spiral[row+k][col+l] != n:
                    sums += spiral[row+k][col+l]
    elif (row == leng-1 and (col != 0 or col != leng-1)):
        col -=1 
        for k in range (2):
            for l in range (3):
                if spiral[row-k][col+l] != n:
                    sums += spiral[row-k][col+l]
    elif (col == 0 and (row != 0 or row != leng-1)):
        row -=1 
        for k in range (2):
            for l in range (3):
                if spiral[row+l][col+k] != n:
                    sums += spiral[row+l][col+k]
    elif (col == leng -1 and (row != 0 or row != leng-1)): 
        row -=1 
        for k in range (2):
            for l in range (3):
                if spiral[row+l][col-k] != n:
                    sums += spiral[row+l][col-k]
    return sums


if __name__ == '__main__':
    user = sys.stdin.readlines()
    # print(user[0])
    user_input = []
    for j in user:
        user_input.append(int(j))
    # print(user_input)
    h = creat_spiral(user_input[0])
    # for i in h:
    #     print(i)
    result = []
    for i in range (1,len(user_input)):
        result.append(sum_adjacent_numbers(h,user_input[i]))
    for i in result:
        print(i)