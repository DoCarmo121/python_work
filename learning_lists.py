concept = "Collection of items in a particular order"
print(concept) #introduction
grupin_de_reis = ['du', 'japa', 'belga', 'pescoss']
print(grupin_de_reis) #output the list including the square brackets
print(grupin_de_reis[0].title() + " é o mais gostoso da tropa\n" + grupin_de_reis[1].title() + ' é o mais cabaço\nPor outro lado, ' + grupin_de_reis[2].title() + ' é autista, enquanto ' + grupin_de_reis[3].title() + ' é curioso.') #output the first item capitalized
grupin_de_reis[0] = 'Do Carmo' #modifying the first item
print(grupin_de_reis)
grupin_de_reis.append('gordão') #adding a new item to the end of the list
print(grupin_de_reis)
grupin_de_reis.insert(3, 'peit') #adding a new item but in a specific position
print(grupin_de_reis)
del grupin_de_reis[3] #removing a item in a sprecific position. You wont be able to access the removed value after that
grupin_de_reis = ['Do Carmo', 'Japa', 'Belga', 'Pescoss', 'Peit']
popped_item = grupin_de_reis.pop(4) #creating a variable to storage the item 'removed' from the list
print(grupin_de_reis)
print(popped_item)
grupin_de_reis.remove('Japa') #when u dont know the position but the value
print(grupin_de_reis)
very_retarded = 'Pescoss'
grupin_de_reis.remove(very_retarded)
print(very_retarded + ' was kicked from the group because of his behavior')