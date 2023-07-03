cars = ['bmw', 'ford', 'tiggo', 'toyota']
cars.sort() #the cars are now in alphabetical order
print(cars)

cars.sort(reverse=True) #inverse of alphabetical order
print(cars)

#sorted() funcion will maitain the original form of the list but change the display to the user:
alunos = ['alice', 'bruno', 'carlos', 'davi']
print('\nHere is the original list:')
print(alunos)
print('\nHere is the sorted list:')
print(sorted(alunos))
print('\nHere is the original list again:')
print(alunos)

#reverse will inverse the items of the list, but not necessarily in backward alphabetically
print("\nOrdem normal: ")
print(alunos)
alunos.reverse()
print('Inverse order: ')
print(alunos)

#finding the length of a list:
print('\nAmount of cars and students:')
alunos.append('Eurico')
print(len(cars))
print(len(alunos))