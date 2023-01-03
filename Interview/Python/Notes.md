`Inheritance`

```
class X:
    def func1(self):
        pass
    
class Y:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Z(Y):
    def __init__(self,id,name,age):
        super().__init__(id,name)
        self.age = age
   
    def func2(self):
        pass

```

`Inheriting Multiple Class`

```
class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, hours_worked, hour_rate)
```

`Abstract Base Class`
- Python provides the abc module to define abstract base classes.

```
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass
```

`Multiple Inheritence`

    Class Base1:
        Body of the class

    Class Base2:
        Body of the class

    Class Derived(Base1, Base2):
        Body of the class

<!-- https://realpython.com/inheritance-composition-python/ -->


`Decorators`
- Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

- In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.

```
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10)) # 25
```
- Syntax of Decorator

```
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)
```

```
# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

```
<!-- https://www.geeksforgeeks.org/decorators-in-python/ -->

`List comprehension`

    x=[i for i in range(5)] # [0,1,2,3,4]

`Dict Comprehension`

    x=[i : i+2 for i in range(5)]
    # o/p - [{0: 2}, {1: 3}, {2: 4}, {3: 5}, {4: 6}]

`How is memory managed in Python?`

Ans: Memory is managed in Python in the following ways:

    Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
    The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
    Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.


`Lambda Function`
- An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.

        a = lambda x,y : x+y
        print(a(5, 6))

`Ternary Operation`

    [on_true] if [expression] else [on_false]
    x, y = 25
    50big = x if x < y else y

`Exception Handling`

    try:
        pass
    except:
        pass

    IndexError, ValueError, ZeroDivisionError

In Django List of Exception Handling are :

- ObjectDoesNotExist : The base class for DoesNotExist exceptions.
- FieldDoesNotExist: 	It raises when the requested field does not exist.
- EmptyResultSet :- If a query does not return any result, this exception is raised.
- FieldError	It is raised when there is a problem with a model field.
- ValidationError	It is raised when data validation fails form or model field validation.

Django Database Exception
- DatabaseError	It occurs when the database is not available.
- IntegrityError	It occurs when an insertion query executes.
- DataError	It raises when data related issues come into the database.


`ZIP`

- Python zip() function returns a zip object, which maps a similar index of multiple containers. It takes an iterable, convert into iterator and aggregates the elements based on iterables passed. It returns an iterator of tuples.

Signature

    zip(iterator1, iterator2, iterator3 ...)    

`All Sorting Algorithm`


`What are decorators in Python?`

    # decorator function to convert to lowercase
    def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper
    # decorator function to split words
    def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper
    @splitter_decorator # this is executed next
    @lowercase_decorator # this is executed first
    def hello():
    return 'Hello World'
    hello()   # output => [ 'hello' , 'world' ]

Differentiate between deep and shallow copies.

    Shallow copy does the task of creating new objects storing references of original elements. This does not undergo recursion to create copies of nested objects. It just copies the reference details of nested objects.
    Deep copy creates an independent and new copy of an object and even copies all the nested objects of the original element recursive

Write a program for counting the number of every character of a given text file.

The idea is to use collections and pprint module as shown below:

    import collections
    import pprint
    with open("sample_file.txt", 'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)
    print(count_value)

