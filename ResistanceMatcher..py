from sys import argv

def is_valid(resistor,target, tolerance):
    s = 0 
    for r in resistor:
        s += 1/r
    s = 1/s
    if(s>(target*(1-tolerance/100) and s < (1+tolerance/100))):
        return (True, ((s-target)/target)*100)
    
def main():
    target = float(argv[1])
    tolerance = float(argv[2])
    num_resistor = int(argv[3])
    filename = argv[4]
    with open(filename, 'r') as f:
        data = f.readlines()
    resistors = []
    for line in data:
        resistors.append(float(line))
    
    
    
if __name__ == '__main__':
    main()