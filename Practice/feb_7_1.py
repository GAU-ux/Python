import keyword

print(keyword.kwlist)
# print("\n Total number of keywords : " , len(keyword.kwlist) )

a_12_be=2
print(a_12_be)

for i in range(10):
    print(i)
    print(i*10)
print(i)

if True:
    print("Machine Learning")

if True: print("Machine Learning") 


a = 1 + 2 + 3 + 4 + \
    + 4 + 4  \

print(a)

a = (1+2+3+4+5
    +6+7+8+9+10)

print(a)

# Multiple line comment
a=b=c=10,5.5,"ML"
print(a)
print(b)
print(c)

a=b=c="AI"
print(a)
print(b)
print(c)


print(id(a))
print(id(b))
b="AJ"
print(b)
print(id(b))

a=5
print(a, " is of type " , type(a))
a=2.5
print(a," is of type ",type(a))
a=1+2j
print(a, " is of type ", type(a))
a=True
print(a, " is of type ", type(a))
a="ML"
print(a," is of type ", type(a))


a='''This is online AI
     course '''
print(a)

print("\n\n\n")

print(a[5:10])


#LIST

a = [10,20.5,"Hello Gaurav"]
print(a[2])
