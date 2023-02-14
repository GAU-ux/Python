# import numpy as np
# import random

# l=list(range(100))
# random.shuffle(l)

# print(l)

# q=31
# isFound=False
# for ele in l:
#     if ele==31:
#         print("Found")
#         isFound=True
#         break;
#     if isFound==False:
#         print("Not Found")
# import math
# import random

# l=list(range(100))
# random.shuffle(l)

# def binarySearch(arr,l,r,x):
#     # check base case
#     if r >= l :
#         mid=l+math.floor((r-l)/2)

#         # if element is present at gthe middle itself
#         if arr[mid] == x:
#             return mid
#         # if element is smaller than mid, then it can only be 
#         # present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr,l,mid-1,x)
#         # Else the element can only be present in right subarray
#         else : 
#             return binarySearch(arr,mid+1,r,x)
#     else : return -1



# l.sort();
# arr=l;
# q=31;
# print(binarySearch(arr,0,len(arr)-1,q))



# Find element common in the lists:

# import random
# l1=list(range(100))
# random.shuffle(l1)

# l2=list(range(50))
# random.shuffle(l2)

# cnt=0;
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(i)
#             cnt=cnt+1
# print("The Number of Common Elements : " ,cnt)



# Find elements common in two lists using a Hashtable/Dict
import random
l1=list(range(100))
random.shuffle(l1)

l2=list(range(50))
random.shuffle(l2)

smallList = {};
for ele in l2:
    smallList[ele]=1; # any value is OK. Key is important

cnt=0;
for i in l1:
    if smallList.get(i)!=None:
        print(i);
        cnt+=1;
print("Number of Common ELements :", cnt)




