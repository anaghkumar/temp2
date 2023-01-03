`Polymorphism`

    The word “polymorphism” means having many forms. In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form.

    Types of Polymorphism
        Compile-time Polymorphism.
            Function Overloading
            Operator Overloading

        Runtime Polymorphism.
            Function Overriding

`Abstraction`

    Abstraction means displaying only essential information and hiding the details. Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation. 

- Unlike the other high-level language, Python doesn't provide the abstract class itself. We need to import the abc module

        # Python program demonstrate  
        # abstract base class work   
        from abc import ABC, abstractmethod   
        class Car(ABC):   
            def mileage(self):   
                pass  
        
        class Tesla(Car):   
            def mileage(self):   
                print("The mileage is 30kmph")   
        class Suzuki(Car):   
            def mileage(self):   
                print("The mileage is 25kmph ")   
        class Duster(Car):   
            def mileage(self):   
                print("The mileage is 24kmph ")   
        
        class Renault(Car):   
            def mileage(self):   
                    print("The mileage is 27kmph ")   
                
        # Driver code   
        t= Tesla ()   
        t.mileage()   
        
        r = Renault()   
        r.mileage()   
        
        s = Suzuki()   
        s.mileage()   
        d = Duster()   
        d.mileage()  

Numpy and Pandas

Models in Django
 - What is model
 - Fields
 - model's meta class
 - Manager
 - Queryset
 - Relations
 - Raw Query
 - Migrations and fixtures

JOINs or relations in Django syntax
Aggregate Functions in Django ORM
Django middlewares
Logging in Django
Cookies and Session in Django
Pagination
User Customization


Serializers
  - Introduction
  - Fields
  - Validation
  - Custom values
  - Custom validations
  - Foreign keys or relation
  - Nested serializers
  - Context message and variables
  - to_representation and to_internal_value


Pagination
Authentication and Permissions
 - Session based
 - JWT
Swagger