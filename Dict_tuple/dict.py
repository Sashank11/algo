myDict = dict()
secondDict = {}
englishtoSpanish = {"one": "uno", "two":"dos", "three":"tres"}

englishtoSpanish['four'] = "cuarto"
#print(englishtoSpanish)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

#traverseDict(englishtoSpanish)

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

#print(searchDict(englishtoSpanish, 'dos'))

#print(englishtoSpanish)
#newDict = {}.fromkeys([1,2,3])
#print(englishtoSpanish.items())
#print(englishtoSpanish.keys())
print(englishtoSpanish.values())
#englishtoSpanish.setdefault('five', 'fres')
#print(englishtoSpanish)
#print(newDict)

newDict = {'a' : 1, 'b': 2}
englishtoSpanish.update(newDict)
print(englishtoSpanish)