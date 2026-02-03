def hello(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

hello.__doc__ = "Return a greeting message."
print(hello())

def hello1(name):
    if not name:
        return 
    print('Hello,' + name + '!')
hello1(False)
hello1("Alice")

age = 30 

def gggg():
    global age
    age += 1
    print("Inside gggg(), age is:", age)
gggg()
print("Outside gggg(), age is:", age)

def count():
    """A function that uses a static variable to count calls."""
    if not hasattr(count, "calls"):
        count.calls = 0  # Initialize the static variable
    count.calls += 1
    return count.calls
def count1():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)
    
    increment()

count()



def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()

print(increment())  # Output: 1
print(increment())  # Output: 2 
print(increment())  # Output: 3

