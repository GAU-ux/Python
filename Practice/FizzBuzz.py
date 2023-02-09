# n=int(input())

# if n<0 and n>10001:
#     exit()

# lst=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         lst.append("FizzBuzz")
#     elif i%3==0 :
#         lst.append("Fizz")
#     elif i%5==0 :
#         lst.append("Buzz")
#     else:
#         lst.append(i)


# delim=","
# temp=list(map(str,lst))
# res=delim.join(temp)
# print(res)



n=int(input())
separator=","

for i in range(1,n+1):
    if (i==n):
        separator="\n"
    if i%15==0:
        print("FizzBuzz",end=separator)
        continue
    elif i%3==0:
        print("Fizz",end=separator)
        continue
    elif i%5==0:
        print("Buzz",end=separator)
        continue
    else:
        print(i,end=separator)