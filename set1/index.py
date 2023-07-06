
def printFunction():
    print("Hello World!")

printFunction()

def Datatypes():
    # integer
    age1 = 25
    age2 : int = 30

    print(age1,type(age1))

    # float
    points1 = 20.3
    points2 :float = 13.12

    print(points1,type(points1))


    # String
    name = 'Raj'
    name : str = "Raju"

    print(name,type(name))


    # Boolean
    isBooked = True
    isPresent:bool = False

    print(isBooked,type(isBooked))

    # list
    arr = [1,2,3,4,5,6]
    numbers : list[int] = [1,2,3,4,5]

    print(arr,type(arr))


    # tuple
    directions = (45,60)
    coordinates: tuple[int, int] = (10, 20)

    print(directions,type(directions))


    # dictionary

    person = {"name":'Raj',"age":25}
    newPerson : dict[str,any] = {"name":"hello", "age":12}
    print(person,type(person))

    # set

    alphabets = {"a","b",'c'}
    alphabets: set[str] = {'a','b','c'}

    print(alphabets,type(alphabets))

    print(age1,age2,points1,points2,name,isBooked,isPresent,arr,numbers,directions,coordinates,person,newPerson,alphabets)

Datatypes()


