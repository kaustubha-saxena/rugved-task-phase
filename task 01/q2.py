str=input()
str2=""
lst = str.split(" ")
for i in range(0,len(lst)-1):
    for j in range(0, len(lst)-1-i):
        if lst[j][0]>lst[j+1][0]:
            temp = lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp

for i in lst:
    str2=str2+i+" "

print(str2)
for i in range(0,len(str)):
    if str.index(str[i])==i:
        print(str[i], " ", str.count(str[i]))