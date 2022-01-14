chk = [0] * 30  
  
n = int(input())  
val = 0  
arr = list(map(int, input().split()))  
for i in range(n):  
    a, b = arr[i*2:i*2+2]  
    for i in range(a, b):  
        chk[i] += 1  
        val = max(chk[i], val)  
  
print(val)
