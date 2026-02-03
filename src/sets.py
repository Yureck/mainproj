set1 = {"Alice", "Bob", "Charlie", "Diana" }
set2 = {"Charlie", "Diana", "Eve", "Frank" }
interset = set1 & set2
print(interset)  # Output: {'Charlie', 'Diana'}
mod = set1 | set2
print(mod)  # Output: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'}
diff = set1 - set2
print(diff)  # Output: {'Alice', 'Bob'}
symdiff = set1 ^ set2   
print(symdiff)  # Output: {'Alice', 'Bob', 'Eve', 'Frank'}
print(list(set1))