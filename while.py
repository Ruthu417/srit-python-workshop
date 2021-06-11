''' n=int(input())
it=1
count=0
while it<=n:
    if n%it==0:
        count+=1
    it+=1
if count==2:
    print("prime")
else:print("not prime") '''

a,b=int(input()),int(input())
print("prime numbers using for loop",end=":")
for num in range(a,b+1):
    count=0
    for dig in range(1,num+1):
        if num%dig==0:
            count+=1
    if count==2:
        print(num,end=" ")
        
# using while
