str= input()
n = int(input())
flag=1
if len(str)%n!=0:
    flag=0
else:
    test_str=str[0:n]
    for i in range(0,len(str),n):
        if test_str !=str[i:i+n]:
            flag=0
    
if flag==1:
    for i in range(0,len(str),n):
        print(str[i:i+n],end=", ")
else:
    print("can not print")