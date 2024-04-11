'''
Singleton:
- Creational design pattern.
- Guarantees a class does only has 1 instance.
- 1 Global Access point to that instance.
- Useful when you need that an object becomes available in all parts of the application.
'''
import uuid #unique identifier

class MySingleton:
    _instance = None #stores the unique instance of class MySingleton created.
    id = None
    
    def __new__(cls):
        '''
        Method called to create a new instance of a class. 
        This method creates the object while init initializes it once is created.
        '''
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls)
            cls.id = uuid.uuid4()
            print("Created the new Singleton's instance")
        else:
            print("Singleton's instance already exists in memory")
        return cls._instance #if the instance exists, just returns it. It does not create a new instance.


#Returns always the same instance id even we make the instantiation 3 different times
instance1 = MySingleton()
print(f"Instance 1: {instance1.id}")
instance2 = MySingleton()
print(f"Instance 2: {instance2.id}")
instance3 = MySingleton()
print(f"Instance 3: {instance3.id}")