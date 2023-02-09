# lst=input()

# if (len(lst)==0 or len(lst)==1):
#     print("Error")
# else :
#     l=(lst.split(','))

#     lst=[*set(l)]
#     if (len(lst)==0 or len(lst)==1):
#         print("Error")
#     else:
#         lst.sort()
#         print(lst[-2])


numberString=input()
l=[ int(i) for i in numberString.split(',') ]
n=len(l)

# Boundary Case
if n<2:
    print("Error")
    exit()

# initiliaze firstmax and max
firstMax=max(l[0],l[1])
secondMax=min(l[0],l[1])

for i in range(2,n):
    if l[i]>firstMax:
        secondMax=firstMax
        firstMax=l[i]
    elif l[i]>secondMax and firstMax!=l[i]:
        secondMax=l[i]

if firstMax==secondMax:
    print("Error")
else:
    print(secondMax) 