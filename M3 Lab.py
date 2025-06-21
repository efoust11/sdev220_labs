"""
Name:  Emma Foust
Filename: M3 Lab.py
Description: This program creates the class Vehicle and the subclass Automobile. 
It then asks the user for the attributes of a car and then prints that information in an organized format. 
Inputs that must be numerical are tested for validity before the program continues.

"""

#Vehicle class, with one attribute which contains the vehicle type
class Vehicle():
    def __init__(self, type):
        self.type = type.capitalize().strip()


#Automobile class, with six attributes including one inherited from the parent class Vehicle.
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#The user confirms that the vehicle is a car.
userinput = input("Enter the vehicle type 'Car': ")

vehicle = Vehicle(userinput)

#This loop runs as long as the vehicle is a car
while vehicle.type == "Car":

    #The user inputs a year. 
    #The program checks that the input is an integer greater than 1900.
    year = input("Enter the car's year: ")
    try: 
        int(year)
    except:
        print("That is not a valid year. Please enter a number")
        year = float(0)

    year = float(year)
    while year < 1900 | (year != int(year)):
        year = input("Enter a valid Year: ")
        try: 
            int(year)
        except:
            print("That is not a valid year. Please enter a number")
            year = float(0)
        year = float(year)

    
    #The user inputs the car's make and model
    make = input("Enter the car's make: ")
    model = input("Enter the car's model: ")

    #The user inputs the number of doors.
    #The program checks that the input is a number
    doors = input("Enter Number of Doors (2 or 4): ")
    try: 
        float(doors)
    except:
        print("That is not a valid input. Please enter either 2 or 4.")
        doors = float(0)

    #The program checks if the input is either a 2 or a 4
    doors = float(doors)
    while (doors != 2.0) & (doors != 4.0):
        doors = input("Enter Number of Doors (2 or 4): ")
        try: 
            float(doors)
        except:
            print("That is not a valid input. Please enter either 2 or 4.")
            doors = float(0)
        doors = float(doors)

    #The user inputs the roof type
    roof = input("Enter type of roof (solid or sunroof): ")

    #The program checks if the roof is either 'solid' or 'sunroof'.
    while (roof != "solid") & (roof != "sunroof"):
        roof = input("Enter type of roof (solid or sunroof): ")
    
    #The inputs are added to an Automobile object
    car = Automobile(vehicle.type, int(year), make, model, int(doors), roof)

    #The attributes of the Automobile are formated and printed
    output = (f"Vehicle Type: {car.type} \n Year: {car.year} \n Make: {car.make} \n Model: {car.model} \n Number of doors: {car.doors} \n Type of roof: {car.roof}")
    print(output)

    #The program asks if the user wants to process the data for another car.
    userinput = input("Enter 'Car' to process another car: ")
    vehicle = Vehicle(userinput)