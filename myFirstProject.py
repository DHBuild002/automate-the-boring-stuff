# This Program says Hello and asks for my name

print('Hello World')

print('What is your name?') # ask for name
myName = input()

print('It is good to meet you, ' + myName)
print('The Length of your name is:')
print(len(myName))

print('What is your age?') #ask for their age
myAge = input()

print('You will be ' + str(int(myAge) + 1)  + ' in a year.')
