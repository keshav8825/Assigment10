#Write a python script to print first M multiples of N.
'''n=int(input("enter a number:"))
   m=int(input("enter multiples:"))
   i=1
   while i<=m:
       print(i*n,end=' ')
       i+=1'''
n=int(input("enter a number:"))
m=int(input("enter multiple:"))
for i in range(1,m+1):
    print(i*n,end=' ')
    i+=1
    
