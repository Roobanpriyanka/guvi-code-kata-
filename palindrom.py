d = 1


while d==1:
    p = raw_input("Enter a sentence or value : ")

    p = p.split()

    r = p[::-1]

    if p == r:
        print "palindrom"

    else:
        print "Not a palindrom"
