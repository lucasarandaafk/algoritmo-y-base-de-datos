N=5
a=[5,6,7,8,9]

i1=0

encontrar=int(input("que numero del 5 al 9 quiere encontrar?"))

i2=-1
66
for i in a:
    i2=i2+1
    if encontrar == i:
        print(f"se encontro {encontrar}")
        break
    elif i2==4:
        print(f"no se encontro {encontrar}")