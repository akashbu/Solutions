
nums_array= [2,3,4]
ans = []
target = 6
prevMap = {}

for i,n in enumerate(nums_array):
    difference = target - n
    if difference in prevMap:
        ans.append(prevMap[difference])
        ans.append(i)
    prevMap[n] = i

print(ans)
