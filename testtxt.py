import random
def writenum():
    with open('input10.txt','w') as outfile:
        outfile.write('5000\n')
        for i in range(5000):
            outfile.write(str(random.randint(1,1000000)))
            outfile.write(' ')
writenum()