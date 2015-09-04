from homestarkov import *

Homestarkov.delete().where(True)

try:
    with open('guyfieri.txt') as fieri_file:
        Homestarkov.create(name="Guy Fieri", path='guyfieri', corpus=fieri_file.read(), tagline='Welcome to Flavortown')
except:
    pass

try:
    with open('cardgage.txt') as cardgage_file:
        Homestarkov.create(name="Senor Cardgage", path='cardgage', corpus=cardgage_file.read(), tagline='Dump Tell No Mandy')
except:
    pass

try:
    with open('homsar.txt') as homsar_file:
        Homestarkov.create(name="Homsar", path='homsar', corpus=homsar_file.read(), tagline='Legitimate Business')
except:
    pass

try:
    with open('hackernews.txt') as hackernews_file:
        Homestarkov.create(name="Hacker News", path='hackernews', corpus=hackernews_file.read(), tagline='Presented by Y Combinator')
except:
    pass

try:
    with open('drewgottlieb.txt') as drew_file:
        Homestarkov.create(name="Drew Gottlieb", path='drew', corpus=drew_file.read(), tagline='Hmm')
except:
    pass
