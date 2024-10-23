str=input()
n = int(input())
str2=""
for i in range(0,len(str)):
    str2=str2+chr(ord(str[i])+n)
print("Encoded text",str2)