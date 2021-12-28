#Problem 32 Project Euler
products=[]
def checkdigitn(n1,n2,n3):
    combine = str(n1)+str(n2)+str(n3)
    b = {i:combine.count(i) for i in set(combine)}
    if len(combine)!=9:
        return False
    keys = b.keys()
    for key in keys:
        if int(key) not in range(1, 10):
            return False
    val = b.values()
    if len(val) != 9:
        return False
    return True

def bruteforce():
    result = 0
    for i in range(2, 10):
        for j in range(1000, 10000):
            product = i*j
            if checkdigitn(i, j, product):
                if product in products:
                    continue
                #print(i, j, product)
                products.append(product)
                result += product
    for i in range(10, 98):
        for j in range(100, 1000):
            product = i*j
            if checkdigitn(i, j, product):
                if product in products:
                    continue
                products.append(product)
                #print(i, j, product)
                result += product
    return result

print(bruteforce())