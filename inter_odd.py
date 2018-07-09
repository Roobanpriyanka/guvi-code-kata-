first=int(input("enter the first number:"))
last=int(input("enter the last number :"))
print("the odd numbers with first and last number:")
for n in range(first,last+1):
 if(n%2!=0):
  print(n)
