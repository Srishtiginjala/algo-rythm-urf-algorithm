

a=input("Enter numbers separated with a space")
l=a.split()
l1=list(map(lambda x:int(x),l))
l1.sort()
b=len(l1)
if b%2!=0:
    print(l1[int((b+1)/2-1)])
else:
    print((l1[int(b/2-1)]+l1[int(b/2)])/2)
