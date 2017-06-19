# names list
# remove quotes from word
# storing in alphabetical order

from urllib.request import urlopen
with urlopen('https://projecteuler.net/project/resources/p022_names.txt') as story:
     text = story.read()
     text = text.decode('utf-8')
text = text.replace('"','')
names = text.split(',') # returns list of strings
names.sort()

def name_score(name,index):
    return name_worth(name)*(index+1)

def name_worth(name):
    return sum(letter_worth(ch) for ch in name)


def letter_worth(char, text ={}):
    if char in text:
        return text[char]
    text[char] = ord(char)-ord('A') +1
    return text[char]

total = sum((name_score(names[i],i)) for i in range(0,len(names)))
print("total is:" + str(total))











'''
     for line in story:
         line_items = line.decode('utf-8').split() #list of strings
         print("lineitems: " + str(line_items))
         for item in line_items:
             item = item.replace('"','')
             story_words.append(item)
     story_words.sort()
     print("story_words: " + str(story_words))
     '''




