x=input("enter num:")
add=0
temp=x

while(temp>1):
    digit = temp%10
    sum = add+pow(digit,3)
    temp//10
    
    if(x == sum):
      print("yes the number is armstrong number:{0}".format)
    else:
        print("no it is not a armstrong number :")
    break
        
