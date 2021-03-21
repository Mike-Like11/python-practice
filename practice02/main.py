from f21 import f21
from f23 import f23
from f22 import f22
import K1
print(f21([2004, 2007, 'arc', 1968, 1988]))
print(f21([1998, 2007, 'arc', 1995, 1974]))

def out(tab):
    for i in range(0,len(tab)):
        print(tab[i])
for i in range(0,len(K1.tests['f22'][9])):
    print(i)
    print(f22(K1.tests['f22'][9][i][0])==K1.tests['f22'][9][i][1])
