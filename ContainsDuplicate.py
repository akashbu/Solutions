nums = [1,1,1,3,3,4,3,2,2]

#nums = [1,2,3,4]

hashSet = set()
for i in range(len(nums)):
    if nums[i] in hashSet:
        print("True") #return
    else:
        hashSet.add(nums[i])
print("False") #return

