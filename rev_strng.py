def rev(s):
    c= " "
    for i in s:
       c=i+c

    return c
s=raw_input("enter the string:")
print("the original string:")
print(s)
print("the reverse string:")
print(rev(s))
