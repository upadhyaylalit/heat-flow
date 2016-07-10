import time 
start = time.time()

#code

l=5
t = [30,50]
dx = 0.5

n=(int)(l/dx)
print "n",n

lista = [(t[0]+t[1])/2]*n
lista.insert(0,t[0])
lista.append(t[1])

print lista

while 

for i in range(1,len(lista)-1):
    diff_x = (lista[i-1]+lista[i+1])
    lista[i]=diff_x/2
    print lista

#diff = [(lista[i]-lista[i+1]) for i in range(len(lista))]

#print diff



#print time.time() - start 
