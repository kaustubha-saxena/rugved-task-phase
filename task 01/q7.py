n = int(input("enter number"))
a=0
b=1 
c=0
print(a,"\t",b,end="\t")
for i in range(2,n):
    c=a+b
    print(c,end="\t")
    a=b
    b=c