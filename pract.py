# sumnum=list(map(int,input("Enter the integer = ").split()))
# print(len(sumnum))
def sum_num():
    sum=0
    for i in range(len(sumnum)):
        sum+=sumnum[i]
        
    print(sum)
sumnum=list(map(int,input("Enter the integer = ").split()))
sum_num()