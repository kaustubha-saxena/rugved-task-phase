str1=input()
str2=input()
flag =1
for i in str1:
    if i not in str2 or str1.count(i)!=str2.count(i):
        flag=0

if(flag==1):
    print("anagram")
else:
    print("Not anagram")