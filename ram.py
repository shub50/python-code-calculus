def f(x):
    return x*x*x
    
def RAM(a, b, n):
    h = (b - a) / n
    x = a
    i = 1
    LRAM = 0.0
    RRAM = 0.0
    MRAM = 0.0
    for i in range(n):
        if x == b:
            print ('i = ', i)
        else:
            LRAM = LRAM + f(x)*h
            x1 = a + (i+1)*h
            RRAM = RRAM + f(x1)*h
            MRAM = MRAM + f((x + x1)/2)*h
            x = x1
    return 'Left RAM = {} Right RAM = {} MRAM = {}.'.format(LRAM,RRAM,MRAM)

def main():
     a = int(input('Left end point: '))
     b = int(input('Right endpoint: '))
     n = int(input('Number of subintervals: '))
     print (RAM(a, b, n))
    
main() 
        
