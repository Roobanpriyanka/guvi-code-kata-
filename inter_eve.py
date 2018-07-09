beg=int(input("enter the first number:"))
end=int(input("enter the last number :"))
print("the even numbers are ")
for n in range(beg,end+1):
   if(n%2)==0:
    print(n)
