
name = 'Bill'
age = 100

if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice')
elif age > 2000:
    print('Unlike you, Alice is not an undead Vampire!')
elif age > 100:
    print('You are not Alice, grannie.')

print('Enter your name: ')
name = input()

if name:
    print('Hi ' + name)
else:
    print('No Name Entered.')
