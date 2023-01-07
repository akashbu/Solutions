prices = [7,1,5,3,6,4]
maxProfit = 0
left_pointer = 0 #buy
right_pointer = 1 #sell

while(right_pointer<len(prices)):
    if(prices[right_pointer]<prices[left_pointer]):
        left_pointer = right_pointer
    elif (prices[right_pointer] - prices[left_pointer]>maxProfit):
        maxProfit=prices[right_pointer] - prices[left_pointer]
    right_pointer = right_pointer + 1

print(maxProfit)