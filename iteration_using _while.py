list = [4,5,6,7,8,10,11]
target = 18
x=[]
left = 0
right = len(list)-1

while left<right:
    currentSum = list[left]+list[right]
    

    if currentSum ==  target:
        print([left, right])
        x=currentSum
        print(x)
        left = left+1

    elif currentSum<target:
        left = left+1

    elif currentSum>target:
        right = right-1