n=input("Enter the number")
flag=0
for i in range(1,len(n)):
    if n[i]>n[i-1]:
        continue
    else:
        flag=i
        break

n2= n[flag:]
# print(n2)
flag=0
for i in range(0,len(n2)-1):
    if n2[i]<n2[i+1]:
        flag=1
        break

if flag==1:
    print("not hill")
else:
    print("hill")