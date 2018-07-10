first=int(input("enter the number:"))
last=int(input("enter the number:"))
print("the prime numbers between first and last are:") 
for n in range(first,last+1):
  if(n>1):
    for i in range(2,n):
      if(n%i)==0:
        break
    
    else:
     print(n)
