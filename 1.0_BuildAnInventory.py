#create an automobile class that will be used by a dealership as a vehicle inventory program

class Automobile:
    def __init__(self):
        self.__make = " "
        self.__model = " "
        self.__color = " "
        self.__year = 0
        self.__mileage = 0
    
    def add_vehicle(self):
        self.__make = input("Enter the make: \n")
        self.__model = input("Enter the model: \n")
        self.__color = input("Enter the color: \n")
        self.__year = int(input("Enter the year: \n"))
        self.__mileage = int(input("Enter the mileage: \n"))
    
    def __str__(self):
        return('%s %s %s %d Mileage: %d' % (self.__make, self.__model, self.__color, self.__year, self.__mileage))
    
    
vehicle_list = []   

def update(vehicle_list):
        x = int(input("Enter the position of the car you want to update: \n"))
        updated_vehicle = car.add_vehicle()
        updated_vehicle = car.__str__()
        vehicle_list[x - 1] = updated_vehicle
        print('Your vehicle list is updated.') 

user = True
while user:
    print ("""
    1. Add a vehicle
    2. Delete a vehicle
    3. Update a vehicle
    4. View vehicle inventory
    5. Export vehicle inventory
    6. Quit program
    """)
    num = int(input("Please enter a number: \n"))
    if num == 1:
        car = Automobile()
        car.add_vehicle()
        vehicle_list.append(car.__str__())
    elif num == 2:
        for i in vehicle_list:
            vehicle_list.pop((int(input("Enter the position of the car you want to to delete: \n"))) - 1)
    elif num == 3:
        update(vehicle_list)
    elif num == 4:
        print(vehicle_list)
    elif num == 5:
        file = open('vehicle_list.txt', 'w')
        file.write(str(vehicle_list))
        file.close()
    elif num == 6:
        print("Thank you for using this program. Goodbye.")
        break
    else:
        print("That is not a valid option. Please try again.")
