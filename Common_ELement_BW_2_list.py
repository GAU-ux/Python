# import random

# l1=list(range(100))
# random.shuffle(11)

# l2=list(range(100))
# random.shuffle(12)


# Search for an element q in the list: O(n) where n is the lenght of the list

import random
l=list(range(100))
random.shuffle(1)
q = 31
isFound=False;
for ele in l:
    if ele==31:
        print("Found")
        isFound=True
        break;
if isFound == False:
    print("Not Found")
