import json
from difflib import get_close_matches

data = json.load(open("application1/data.json"))

def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x, data.keys())) > 0:
        yn = input('Did you mean %s instead? Enter Y id yes, or N if no: ' % get_close_matches(x, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(x, data.keys())[0]]
        elif yn == 'N':
            return 'The word doesn\'t exist. Please check it again.'
        else: 
            return 'We didn\'t understand your entry.'
    else:
        return 'The word doesn\'t exist. Please check it again.'

while True:
    entry = input('Enter word (Enter exit() to end): ')
    if entry == 'exit()':
        break

    word = entry
    output = translate(word)

    if type(output)  == list:
        for item in output:
            print(item)
    else:
        print(output)




