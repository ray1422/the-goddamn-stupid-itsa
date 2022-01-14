D = [[1, 0], [0, 1], [-1, 0], [0, -1]]  
t = int(input())  
for u in range(t):  
    arr = []  
    a, b = map(int, input().split())  
    for i in range(a):  
        arr.append(list(map(int, input().split())))  
              
    for i in range(a):  
        for j in range(b):  
            if arr[i][j] == 0:  
                print("_", end="")  
            else:  
                for k in range(4):  
                    x = i - D[k][0]  
                    y = j - D[k][1]  
                    if arr[x][y] == 0 and x >= 0 and x <= a and y >= 0 and y < b:  
                        print("0", end="")  
                        break  
                else:  
                    print("_", end="")  
              
            if j == b-1:  
                print(" ")  
            else:  
                print(" ", end="")  
    if u != t-1:  
        print()
