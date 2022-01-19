def expand(c):
    d=c[1]-c[0]
    for i in range(2,len(c):
        if abs(c[i]-c[i-1])>d:
            d=abs(c[i]-c[i-1])
        else:
            return False
    return True
a=list(map(int(input()))).split()
out=expand(a)
print(out)
