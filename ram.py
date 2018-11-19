a = int(input('Left end point: '))
b = int(input('Right endpoint: '))
n = int(input('Number of subintervals: '))
f = input('Enter function: ')   

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
        LRAM = LRAM + eval(f)*h
        x1 = x
        x2 = a + (i+1)*h
        x = x2
        RRAM = RRAM + eval(f)*h
        x = 0.5*(x1 + x2)
        MRAM = MRAM + eval(f)*h
        x = x2
print('Left RAM = {} Right RAM = {} MRAM = {}.'.format(LRAM,RRAM,MRAM))
