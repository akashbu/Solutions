nums = [2,3,-2,4]

res = nums[0]
maxele = nums[0]
minele = nums[0]

for i in range(1,len(nums)):
    if nums[i] < 0:
        minele, maxele = maxele, minele
    maxele = max(nums[i], maxele*nums[i])
    minele = min(nums[i], minele*nums[i])
    res = max(res, maxele)

print(res)