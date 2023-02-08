# a=int(input())
# i=2
# while i<(a):
#     if (a)%i==0:
#         print(str(a) + " is not a prime Number")
#         break
#     i+=1;
# if i==a:
#     print(str(a)+ " is a prime number")
    
num = int(input("Enter a number : ")) #convert string to int

isDivisible=False

i=2

while i<num:
    if num%i==0:
        isDivisible = True
        print("{} is Divisible by {}".format(num,i))
    i+=1

if isDivisible:
    print("{} is Not a Prime Number".format(num))
else:
    print("{} is a Prime Number".format(num))