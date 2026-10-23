a=[1, 3, 5, 8, 6,]
b=[4, 7, 1, 90]
c=[7, 1, 4, 90,]
r=[]
for x in a:
    if x in b and x in c:
        if x not in r:
            r.append(x)
print(r)