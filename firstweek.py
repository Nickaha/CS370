def first():
    inputs = input()
    li = list(inputs.split(" "))
    n = int(li[0])
    k = int(li[1])
    a=0
    for i in range(n):
        b=input()
        while int(b) >= 10**9:
            b = input()
        if int(b)%k == 0:
            a+=1
    return a
first()