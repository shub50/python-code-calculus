def fvalue(x,f):
    return eval(f)
    
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
            LRAM = LRAM + fvalue(x,f)*h
            x1 = a + (i+1)*h
            RRAM = RRAM + fvalue(x1,f)*h
            MRAM = MRAM + fvalue((x + x1)/2,f)*h
            x = x1
    return 'Left RAM = {} Right RAM = {} MRAM = {}.'.format(LRAM,RRAM,MRAM)

def main():
     a = int(input('Left end point: '))
     b = int(input('Right endpoint: '))
     n = int(input('Number of subintervals: '))
     f = input('Enter function: ')   
     print (RAM(a, b, n))
    
main() 
        
