def sum_square():
    odd=0
    even=0
    list=[1,4,9,12,13,30,18]
    for a in list:
        if a%2!=0:
            odd+=(a**2)
        else:
            even+=(a**2)
    print(odd,even)

sum_square()
