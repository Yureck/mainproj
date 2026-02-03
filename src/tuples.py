names = ("Alice", "Bob", "Charlie", "Diana")
names[-1]
print(names[0])  # Output: Alice
#names[1] = "Eve"  # This will raise a TypeError because tuples are immutable    
names.index("Charlie")  # Output: 2
print(names.index("Charlie"))  # Output: 2
print(names.count("Alice"))  # Output: 1
print("Eve" in names)  # Output: False
names[0:2]  # Output: ('Alice', 'Bob')
sorted(names)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']
print(sorted(names))  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']
newtuples = names + ("Eve", "Frank")
print(newtuples)  # Output: ('Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank')

