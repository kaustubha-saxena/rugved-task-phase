str=input()
lst = list(str.split(" "))
smallest=0
for i in range(0,len(lst)-1):
    smallest = i
    for j in range(i+1,len(lst)):
        if lst[smallest]>lst[j]:
            smallest=j
    temp = lst[smallest]
    lst[smallest]=lst[i]
    lst[i]=temp

print(lst)