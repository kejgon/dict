import json
import difflib  # its a library to compare text
# from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or  N if no :" %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return 'The word does not exist. Pleace double check it.'


words = input("Enter word : ")
# SequenceMatcher(None, words, translate(words)).ratio()

# To display our output in terms of paragraphs, line after line.
outPut = translate(words)

if type(outPut) == list:  # this condition works when our outputs is equivalent to list
    for item in outPut:
        print(item)
else:
    print(outPut)
