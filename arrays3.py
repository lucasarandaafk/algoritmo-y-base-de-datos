N=5
a=[11,22,33,44,55]
print(a)
b=[]
i=0
for i in range(N):
    b.append(a[N - (i + 1)])
print(b)