''' Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45 '''

start=int(input("enter the starting range: "))
end=int(input("enter the end range: "))
print("prime numbers in the range",start,"to",end)
for i in range(start,end+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i,end=' ')    