import random,string


d = dict();

# given a long URL, get a short URL
def getShortURL(longURL):
    # length = random value in 6-10
    l = random.randint(6,10);
    
    
    # generate random characters into a string of length l
    chars = string.ascii_lowercase
    shortURL = ''.join(random.choice(chars) for i in range(l))
    
    
    # check if this string is already present in dict d
    if shortURL in d:
        return getShortURL(longURL);
    else:
        d[shortURL] = longURL;
        
    
    r = "https://www.shortURL.com/"+shortURL
    return r;

def getLongURL(shortURL):
    
    # extarct key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
    k = shortURL[25:];
    
    
    if k in d:
        return d[k];
    else:
        return None;






class ShortURL:
    
    def __init__(self): # constructor; not must, but, good to have;  initialize all attributes here
        self.d=dict();

    # given a long URL, get a short URL
    def getShortURL(self, longURL): # first argument to all methods is "self" => this object
        # length = random value in 6-10
        l = random.randint(6,10);
        

        # generate random characters into a string of length l
        chars = string.ascii_lowercase
        shortURL = ''.join(random.choice(chars) for i in range(l))
        

        # check if this string is already present in dict d
        if shortURL in self.d:
            return getShortURL(longURL);
        else:
            self.d[shortURL] = longURL;

        
        r = "https://www.shortURL.com/"+shortURL
        return r;

    def getLongURL(self, shortURL):

       # print(self.d); # print statemnt for debugging
        
        # extarct key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
        k = shortURL[25:];
        

        if k in self.d:
            return self.d[k];
        else:
            return None;


s = ShortURL()  # constructor being called itselff
print(type(s))
print(s.getShortURL("appliedcourse.com"))
print(s.getShortURL("gate.appliedcourse.com"))
print(s.getLongURL("https://www.shortURL.com/qigmstv"))
print(s.d)

# class EmptyCLass:
#     pass

# e = EmptyCLass();
# print(type(e))

# Class variables shared by all objects

# Class: group all variables/attributes and functions/methods into a soingle logical unit

class ShortURL1:
    
    URLPrefix = "https://www.shortURL.com/"; # class variable shared by all objects
    
    def __init__(self): # constructor; not must, but, good to have;  initialize all attributes here
        self.d=dict();

    # given a long URL, get a short URL
    def getShortURL(self, longURL): # first argument to all methods is "self" => this object
        # length = random value in 6-10
        l = random.randint(6,10);
        

        # generate random characters into a string of length l
        chars = string.ascii_lowercase
        shortURL = ''.join(random.choice(chars) for i in range(l))
        

        # check if this string is already present in dict d
        if shortURL in self.d:
            return getShortURL(longURL);
        else:
            self.d[shortURL] = longURL;

        
        r = self.URLPrefix + shortURL
        return r;

    def getLongURL(self, shortURL):

       # print(self.d); # print statemnt for debugging
        
        # extarct key from URL https://www.shortURL.com/mxzmuis ---> mxzmuis
        k = shortURL[25:];
        

        if k in self.d:
            return self.d[k];
        else:
            return None;
