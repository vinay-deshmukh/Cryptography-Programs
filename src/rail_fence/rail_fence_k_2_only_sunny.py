import itertools as it

main=[]
first=[]
second=[]
ans=[]

# A SIMPLE ROUGH RAILFENCE CODE WHICH
#WORKS ONLY FOR k=2 WHICH SHOULD PROBABLY BE SUFFICIENT FOR CSS PRACS


print("Enter the String")

arr=[x for x in input()]
for i in range(0,len(arr),2): ##
    main.append(arr[i])
    first.append(arr[i])



for i in range(1,len(arr),2):
    main.append(arr[i])
    second.append(arr[i])



print("Encrypted string :", "".join(main).replace(" ",""))

print()

print("Decrypted string :")

for a,b in it.zip_longest(first,second):
    ans.append(a)
    ans.append(b)


print("".join([x for x in ans if x is not None]))    

