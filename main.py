import random
from random import randint
from random import randrange
from translate import Translator
import requests
import re
import zipcodes
from bs4 import BeautifulSoup


# Program Functions
def isZipValid(z):
    try:
        if not zipcodes.matching(z):
            return False
        else:
            return True
    except ValueError:
        pass


def random_line(afile):
    return random.choice(open(afile).readlines())


def randomChoice(o1, o2):
    r = randrange(2)
    if r == 1:
        return o1
    elif r == 0:
        return o2


def randomSeason():
    r = randrange(3)
    if r == 0:
        return 'winter'
    elif r == 1:
        return 'spring'
    elif r == 2:
        return 'summer'
    elif r == 3:
        return 'fall'


def getYelpList():
    r = requests.get('https://www.yelp.com/search?find_desc=Things+To+Do&find_loc=' + zipCode)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_meta = soup.find_all('meta', attrs={'data-rh': 'true', 'name': 'description'})
    all_meta = str(all_meta[0])

    counter = 1
    endString = '" data-rh'
    startingSubstring = 0
    endingSubstring = 0
    originalString = ""

    for i in all_meta:
        if (originalString + i) == zipCode[0:counter]:
            originalString += i
            counter += 1
        elif originalString == zipCode:
            break
        startingSubstring += 1

    counter = 1
    originalString = ""
    for i in all_meta:
        if (originalString + i) == endString[0:counter]:
            originalString += i
            counter += 1
        elif originalString == endString:
            break
        endingSubstring += 1

    placeList = all_meta[startingSubstring + 3:endingSubstring - 9]
    placeList = re.sub(r'\([^)]*\)', '', placeList)
    return placeList.split(", ")


# Program
zipValid = False
while not zipValid:
    zipCode = input("Enter a zipcode: ")
    zipValid = isZipValid(zipCode)

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
season = input("Enter current season (E.g winter): ")
translator = Translator(to_lang="es")
list1 = getYelpList()

activity1 = random_line(season)
activity2 = random_line(season)
activity3 = random_line(season)
activity4 = random_line(season)
place1 = list1[randrange(len(list1))]
place2 = list1[randrange(len(list1))]
place3 = list1[randrange(len(list1))]

sentence1 = 'This weekend I ' + activity1 + ' with my ' + randomChoice('family', 'friends') + ' on Friday Afternoon. '

sentence2 = 'On Saturday I woke up around ' + str(
    randint(7, 12)) + ' AM, I was planning to go to ' + place1 + ' with my friend group, we heard ' + randomChoice(
    'good', 'great') + ' things about it. '

sentence3 = '\nAfter that was ' + randomChoice('over', 'done') + ', it was the ' + randomChoice('early',
                                                                                                'late') + ' afternoon and my ' + \
            randomChoice(
                'Aunt', 'Uncle') + ' wanted to go to ' + place2 + ' with me, it was a ' + randomChoice('pretty quaint',
                                                                                                       'picturesque') + ' local ' \
                                                                                                                        'place. '

sentence4 = 'After that ' + randomChoice('fun',
                                         'relaxing') + ' trip, \n' + name1 + ', a friend, and I felt ' + randomChoice(
    'sporadic',
    'unpredictable') + ' so we ' + activity2 + '. Late Saturday night, ' + name1 + 'and I met up with my other ' \
                                                                                   'friend, ' + name2 + '. '

sentence5 = 'We ' + activity3 + ' for a ' + randomChoice('long',
                                                         'short') + ' time, then got a little ' + randomChoice(
    'bored', 'tired') + ' of that so we ' + randomChoice('ditched', 'stopped ') + ' that. '

sentence6 = 'On Sunday, I wanted to ' + randomChoice('keep it light',
                                                     'take it easy') + ', so I ' + activity4 + ' by myself, and ' \
                                                                                               'after I went to ' \
            + place3 + ' to relax. '

sentence7 = '\nSo that was my very ' + randomChoice('eventful', 'exciting') + ' Weekend!'

story = sentence1 + sentence2 + sentence3 + sentence4 + sentence5 + sentence6 + sentence7

print(story)
