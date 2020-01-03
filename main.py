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

print(cat)

print('Hi ' + cat['name'])
print(cat['photo'])

def feed(pet):
    pet['hungry'] = False
    pet['weight'] = pet['weight'] + 1

print(cat)
feed(cat)
print(cat)
