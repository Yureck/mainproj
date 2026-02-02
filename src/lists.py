dogs = ["Buddy", "Max", "Bella", "Lu/ncy  ", "Daisy"]
print("Max" in dogs)
print(dogs[2:4])
print(dogs[-2 ].strip())
print(dogs[::-1])
print(len(dogs))
print(dogs.append("Molly"))
print(dogs.extend(["Charlie", "Luna"]))
print(dogs)


items = ["Buddy", "Max", "Bella", "Lu\n\"cy  ", "Daisy"]
string = "jhdfhfjhdfjk\nkjflkjdg"
print(string)

print(items.count("Max"))
print(items.index("Bella"))
items.pop(2)
print(items)
print(items.__add__(["Rocky", "Zoe"]))
print(items.insert(2, "Zoe"))
items += ["Rocky"]
items += "Rocky"
print(items)
items[1:1] = ["Coco", "Lola"]
print(items)
items.sort()
print(items)
items.sort(key=str.upper, reverse=True )
print(items)

print(sorted(items, key=str.upper))
print(items)