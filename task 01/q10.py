number=list(input())
# lst = list(number)
print(number)
sum=0
def convert_single(n):
    sum=0
    while(1>0):
        sum=0
        while(n>0):
            sum = sum + n%10
            n=int(n/10)
        if sum >9:
            n=sum
        else:
            break
    return sum

for i in range(0,len(number)):
    if( len(number)-i)%2==0:
        number[i]= int(number[i])+int(number[i])
        if number[i]>9:
            number[i]=convert_single(number[i])



for i in number:
    sum = sum+int(i)
print(sum)
if sum % 10==0:
    print("valid")
else:
    print("not valid")


