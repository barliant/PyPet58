print('Welcome owner PyPet58!')

name = 'Annette'
age = 21
weight = 50.5
hungry = True
naughty = True
photo = '(=^o.o^=)__'

print('Hello ' + name)
print(photo)

cat = {
    'name': 'Fluffy',
    'hungry': True,
    'weight': 9.5,
    'age': 5,
    'photo': '(=^o.o^=)_/',
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

pets = [cat, mouse]

print(cat)

print('Hi ' + cat['name'])
print(cat['photo'])

def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print(pet['name'] + ' is not hungry!')

for pet in pets:
    feed(pet)
    print(pet)
