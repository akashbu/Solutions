nums = [1,1,1,3,3,4,3,2,2]

#nums = [1,2,3,4]

hashSet = set()
for i in range(len(nums)):
    if nums[i] in hashSet:
        print("True") #return
    else:
        hashSet.add(nums[i])
print("False") #return




# flag = 0
# if (len(set(nums))== len(nums)):
#     print("True 1")
# else:
#     myDict = {i:nums.count(i) for i in nums}
#     print(myDict)
#     for key, value in myDict.items():
#         if value<2:
#             flag = 1
#             break
#     if flag:
#         print("False 2")
#     else:
#         print("True 2") 