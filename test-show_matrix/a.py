from liblibra_core import *
from PYXAID2 import *
from libra_py import *


a = CMATRIX(4,4)
for i in range(0,4):
    for j in range(0,4):
        a.set(i,j,0.5*i+j, 0.1*(i-j))

x="/home/eric/src/Libra/for_develop/test/test-show_matrix"

a.real().show_matrix(x)

f=open("o","r")
fr=f.readlines()
f.close()

for i in fr:
    print float(i.split())*2
