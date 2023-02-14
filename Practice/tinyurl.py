import random
import string

d = {};

# given a long URL, get a short URL
def getShortURL(longURL):
    # length = random value in 6-10
    l = random.randint(6,10);
    print(l);
    
    # generate random characters into a string of length l
    chars = string.ascii_lowercase
    shortURL = ''.join(random.choice(chars) for i in range(l))
    print(shortURL);
    
    # check if this string is already present in dict d
    if shortURL in d:
        return getShortURL(longURL);
    else:
        d[shortURL] = longURL;
        
    print(d)
    r = "https://www.shortURL.com/"+shortURL
    return r;

def getLongURL(shortURL):
    
    # extarct key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
    k = shortURL[25:];
    print(k)
    
    if k in d:
        return d[k];
    else:
        return None;

print(getShortURL("www.appliedaicourse.com"))
