nums = sorted(list(map(int, input().split(","))))  
  
max_val = 0  
min_val = 0  
for i in range(len(nums)):  
    max_val *= 10  
    max_val += nums[-i-1]  
    min_val *= 10  
    min_val += nums[i]  
  
print(abs(max_val - min_val))
