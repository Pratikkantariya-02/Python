file = open('Youtube.txt', 'w')

try:
    file.write('Chai aur me')
finally:
    file.close()

with open('Youtube.txt','w') as file:
    file.write("Hello")