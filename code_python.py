Nbrhab=3000
while not (Nbrhab<=1000) :
   Nbrhab=int(input(""))
l=[0]*Nbrhab
for i in range (Nbrhab) :
   Fort=int(input(""))
   l[i]=Fort
l.sort()
if Nbrhab%2==0 :
   Nombre=((l[(Nbrhab-1)//2]+l[(Nbrhab//2)])/2)
else :
   Nombre=(l[(Nbrhab-1)//2])
print(Nombre)
      
