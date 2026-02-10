#1RUA25BCA0011 ASWATHEE S
def wc(sen):
    count=1
    for i in sen:
        if i==' ':
            count+=1
    return count
sen=input("enter a sentence:")
print("word count =",wc(sen))
