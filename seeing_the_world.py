places = ['Turkey', 'China', 'France', 'Norway', 'Russia']
print("Places I'd like to know: ")
print("Original order:")
print(places) #will show me in the original order of the list
print("\n Alphabetical order:")
print(sorted(places)) #organized alphabetically but did not modify the list itself
print("\nInverse order:")
print(sorted(places, reverse= True)) #reverse alphabetical order using sorted
print("\nList is still intact:")
print(places)
print("\nReverse:")
places.reverse() #reverse list permanentemente
print(places)
print("\nReverse again:")
places.reverse()
print(places)
print("\nOrdering but with sort:")
places.sort()
print(places)
print("\nInverse alphabet but with sort:")
places.sort(reverse=True)
print(places)
