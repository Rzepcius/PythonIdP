magicians = ['alicja', 'dawid', 'karolina']
for magician in magicians:
    print (magician)
for magician in magicians:
    print (f"{magician.title()}, to była doskonała sztuczka!")
for magician in magicians:
    print(f"{magician.title()}, to była doskonała sztuczka!")
    print(f"Nie mogę się doczekać Twojej kolejnej sztuczki,{magician.title()}.\n")
print("Dziękuję wszystkim. To był naprawdę wspaniały występ!")
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11,2))
print(even_numbers)
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append (square)
print (squares)
min(numbers)
max(numbers)
sum(numbers)
squares2=[value**2 for value in range(1, 30)]
print(squares2)
print(squares2[0:3])
print(squares2[11:22])
print(squares2[:8])
print(squares2[25:])
print(squares2[-3:])
players = ['karol', 'martyna', 'michał', 'florian', 'ela']

print("Oto trzech pierwszych graczy naszej drużyny:")
for player in players [:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friend_foods = my_foods [:]
my_foods.append("pieróg")
friend_foods.append("zapiekanka")

print ("Moje ulubione potrawy to:")
print (my_foods)

print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_foods)

dimensions = (200, 50)
print (dimensions[0])
print(dimensions[1])
# dimensions[0] = 250
for dimension in dimensions:
    print (dimension)

dimensions = (400, 100)
print("\nWymiary po modyfikacji:")
for dimension in dimensions:
    print(dimension)