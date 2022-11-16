#. Write a python script to print first 10 multiples of N

'''n=int(input("enter a number:"))
   i=1
   while i<=10:
       print(i*n,end=' ')
       i+=1'''
n=int(input("enter a number: "))
for i in range(1,11):
    print(i*n,end=' ')
    i+=1

