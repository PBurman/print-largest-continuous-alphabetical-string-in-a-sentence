str= input("Enter the String: ")
words= str.split()
a=0
size=[]
for v in words:
        for i in v:
            for x in i:
                a +=1
        size.append(a)
        a=0
print("largest continuous alphabetical string in the sentence is : "+ words[size.index(max(size))])
