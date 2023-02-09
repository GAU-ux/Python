# num=-100
# print(abs(num))

# True : if all elements in an itearble are true
# False : if any element in an itearble is false

# lst=[1,2,3,4]
# print(all(lst))

# lst=[1,2,3,4,0]
# print(all(lst))

# The dir() tries to return a list of valid

# numbers=[1,2,3]
# print(dir(numbers))

# divmod() return the quotient and remainders as a tuple
# print(divmod(9,2))

# enumerate(iterable,start=0)  method adds counter to an iterable and returns it
# numbers=[10,20,30,40,50]
# for index, num in enumerate(numbers):
#     print("index {0} has value {1}".format(index,num))

# filter() method constructs  an iterator form the elements
# of an iterable for which a function returns true

# def find_positive_number(num):
#     """
#     This function returns the positive number if num is positive
#     """
#     if num>0:
#         return num

# number_list=range(-10,10) # create a list with numbers from -10 to 10
# print(list(number_list))

# positive_num_lst=list(filter(find_positive_number,number_list))
# print(positive_num_lst)

# isinstance(object,classinfo) 
# this function checks if the object is instance
# or subclass of classinfo class

# lst=[1,2,3,4]
# print(isinstance(lst,list))

# t=(1,2,3,4)
# print(isinstance(t,list))

# map() applies a function to all the items in an input_list

# numbers = [1,2,3,4]
# # squared=[]
# # for num in numbers:
# #     squared.append(num**2)
# def powerOfTwo(num):
#     return num**2;
# squared=list(map(powerOfTwo,numbers))
# print(squared)


# reduce()  fucntion is for performing some computation 
# on a list and returning the result.
# 
# It applies a rolling coimputation to sequential pairs 
# of the values in list

# product of elements in a list withot reduce()
# product=1
# lst=[1,2,3,4]
# for num in lst:
#     product*=num
# print(product)

# product of elements in a list with reduce()
# from functools import reduce
# lst=[1,2,3,4]
# def multiply(x,y):
#     return x*y;
# product=reduce(multiply,lst)
# print(product)


# def product_numbers(a,b):
#     """
#     this function returns th eproduct of two numbers
#     """
#     product=a*b
#     return product
# num1=10
# num2=20
# print(" product of {0} and {1} is {2}".format(num1,num2,product_numbers(num1,num2)))

