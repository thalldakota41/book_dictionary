import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Sorry, word variation not availible."
        else:
            return "We didn't understand your query."
    else: 
        return "The word doesn't exist. Try again!"

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)
