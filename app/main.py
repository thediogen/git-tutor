name = input('Enter your name: ')
age = int(input('Enter yout age: '))

print(f'Your name is {name} and you are {age} y.o.')

skin_color = input('Enter your skin color: ')
print(f'Your skin color is {skin_color}')

with open('text.txt', 'r') as text:
    print(text)
    
print('This is quick-test branch')
print('This is "main" branch')
