bicycles = ["górski","trekingowy","miejski","szosowy"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])#ostatnia wartość
msg=f"Moim pierwszym rowerem był {bicycles[-1].title()}"
print(msg)
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles[0] = 'ducati'
print (motorcycles)
motorcycles.append("Hd")
print (motorcycles)
motorcycles.insert(0,"honda")
print (motorcycles)
del motorcycles[0]
print (motorcycles)
pop_motorcycles = motorcycles.pop(1)
print(motorcycles)
print (pop_motorcycles)
motorcycles.remove("ducati")
print (motorcycles)
motorcycles.append("ducati")
motorcycles.append("honda")
# motorcycles.sort()
print (motorcycles)
print (sorted(motorcycles))
print (motorcycles.reverse())
