#python dictionary

#create empty dictionary
car = {}

#add entries
car['car brand'] = input('Enter the car brand: \n')
car['car model'] = input('Enter the car model: \n')
car['car year'] = int(input('Enter the car year: \n'))
car['car starting odometer'] = int(input('Enter the starting odometer reading: \n'))
car['car ending odometer'] = int(input('Enter the ending odometer reading: \n'))
car['estimated miles per gallon consumed'] = float(input('Enter the estimated miles per gallon consumed by the vehicle: \n'))

#output dictionary
print(car)
