'''
Program that Print 4 lists:
a- 50 random numbers from 1 to 99
b- numbers larger that 65 from a
c- even numbers from b
d- [sum of numbers in c , len of c]
'''
import random

lista=[]
listb=[]
listc=[]
listd=[]

for i in range(50):
    num= random.randint(1,99)
    lista.append(num)
print(f"a- 50 random numbers from 1 to 99\n{lista}\n")


for i in lista:
    if i > 65:
        listb.append(i)
print(f"b- Numbers larger that 65 from a\n{listb}\n")


for i in listb:
    if i % 2 == 0:
        listc.append(i)
print(f"c- Even numbers from b\n{listc}\n")  


sum=0
for i in listc:
    sum+=i
listd=[sum,len(listc)]
print(f"d- [sum of numbers in c , length of c]\n{listd}")
