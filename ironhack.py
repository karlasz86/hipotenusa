_CATETO=0
_CATETO2=0

listacateto =[]

x = range(1, 101)
cateto = list(x)
print(cateto)

y = range(3,303,3)
cateto2= list(y)
print(cateto2)

for item in cateto and cateto2:
    if item>0:
        micateto=cateto[_CATETO]
        _CATETO+=1
        micateto2=cateto2[_CATETO2]
        _CATETO2+=1
        
        print(micateto**2, "+ ", micateto2**2, " = ", micateto**2+micateto2**2)
