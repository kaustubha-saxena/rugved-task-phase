str= input()
word=0
character=0
sentence=0
sent_list=str.split(".")
lst=[]
sentence=len(sent_list)
print(sent_list)

for i in sent_list:
    for j in i:
        character=character+1
    lst=i.split(" ")
    word= word+len(lst)


print("Coleman-Liau index=",5.89*(character/word)-0.3*(sentence/word)-15.8)


