#Nathan Schoenike
#9/9/2025
#Purpose: To create a vehicle superclass and automobile subclass that demonstrates I know 
#how to use inheritance in python.

class Vehicle:
    def __init__(user, vehicleType):
        user.vehicleType = vehicleType
    
    
        
#Automobile Subclass which inherits the vehicle type

class Automobile(Vehicle):
    def __init__(user, make, model, year, doors):
        super().__init__(vehicleType)
        
        user.make = make
        user.model = model
        user.year = year
        user.doors = doors
        user.doors = doors
    
        

    
vehicleType = input("Please enter the type of vehicle (Car, Truck, Motorcycle, Bus, Bicycle): ")
make = input("Please enter the make of the vehicle: ")
model = input("Please enter the model of the vehicle: ")

#while loops to make sure the users input is valid

while True:
    try:
        year = int(input("Please enter the year of the vehicle: "))
        if year < 0:
            print("Invalid number of doors. Please enter an integer over 0")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number .")

while True:
    try:
        doors = int(input("Please enter the number of doors on the vehicle: "))
        if doors < 0:
            print("Number of doors cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of doors.")




#my print functions
# I had to change the doors and year to a string to go along with my constraints I have for the accepted input
self = Automobile(make, model, year, doors)
print("Make: " + self.make)
print("Model: " + self.model)
print("Year: " + str(self.year))
print("Number of Doors: " + str(self.doors))




