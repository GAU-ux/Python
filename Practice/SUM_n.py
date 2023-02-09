n=int(input())

if (n==0):
    print(0)
else:
    numberStr=input()
    s=numberStr.split()
    sum=0
    for i in s:
        sum=sum+int(i)
    print(sum)