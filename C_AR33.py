arr = []  
  
n, m = map(int, input().split())  
result = [[0] * n for _ in range(m)]  
for i in range(n):  
    arr.append(input().split())  
  
  
for i in range(n):  
   for j in range(m):  
       result[j][i] = arr[i][j]  
  
for r in result:  
   print(" ".join(r))
