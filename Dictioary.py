import json
from difflib import get_close_matches
data=json.load(open("data.json"))





def A(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0 :
        yn=input("Doyoumean %s  ?.Type Y/N:" % get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return ("Word not exist")
            
            if Q in data:
                return data[w]
            
            
            
            
        else:
            return ("Word does not exit")
            
   
    else:
        return ("safasf")

word=input("Enter Word: ")


output = A(word)

if type(output)==list:

    for P in output:
        print(P)
else:

    print(output)

