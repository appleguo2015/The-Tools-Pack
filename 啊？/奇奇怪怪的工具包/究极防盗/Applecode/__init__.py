'''
    __(___
  /  By   \
 |AppleGUO|
 \_______/

I can give you apple: 🍎.
'''
import random


def Encode(text):
    l = list(text)
    l.insert(random.randrange(0, len(l)), '🍎')
    l.insert(random.randrange(0, len(l)), '🍎')
    l.insert(random.randrange(0, len(l)), '🍎')
    text = ''
    for i in range(len(l)):
        text = f'{text}{l[i]}'
        i += 1
    return text

def Unencode(text):
    return text.replace('🍎', '')