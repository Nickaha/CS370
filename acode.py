def acoding(cipher):
    result = []
    first = list(cipher)
    result.append(first)
    if (len(cipher)==1):
        return 1

    for i in range(len(cipher)-1):
        com = cipher[i:i+2]
        if(int(com)<27):
            res = acoding(cipher[i+2])
        

acoding("25114")