#MODULE 1: OPTION 1

print('         (\-.')
print('         / _`>')
print(' _)     / _)=')
print('(      / _/')
print(' `-.__(___)_')

#MODULE 2: OPTION 2

car = {}

car['car brand'] = input('Enter the car brand: \n')
car['car model'] = input('Enter the car model: \n')
car['car year'] = int(input('Enter the car year: \n'))
car['car starting odometer'] = int(input('Enter the starting odometer reading: \n'))
car['car ending odometer'] = int(input('Enter the ending odometer reading: \n'))
car['estimated miles per gallon consumed'] = float(input('Enter the estimated miles per gallon consumed by the vehicle: \n'))

print(car)

#MODULE 3: OPTION 1

year = int(input("Enter year:\n"))

if year < 1962:
    print("The Ferrari 250 GTO does not exist at this year.")
elif year <=1964:
    print("Your Ferrari 250 GTO is valued at $18,500.")
elif year <= 1968:
    print("Your Ferrari 250 GTO is valued at $6,000.")
elif year <= 1971:
    print("Your Ferrari 250 GTO is valued at $12,000.")
elif year <= 1975:
    print("Your Ferrari 250 GTO is valued at $48,000.")
elif year <= 1980:
    print("Your Ferrari 250 GTO is valued at $200,000.")
elif year <= 1985:
    print("Your Ferrari 250 GTO is valued at $650,000.")
elif year <= 2012:
    print("Your Ferrari 250 GTO is valued at $35,000,000.")
elif year <= 2014:
    print("Your Ferrari 250 GTO is valued at $52,000,000.")
elif year >= 2015:
    print("No estimated value of your Ferrari 250 GTO available at this year.")

#MODULE 4: OPTION 1

list = []
length = 5

for i in range(length):
    value = float(input("Enter five values: "))
    list.append(value)
print("Your five values:", list)

total = 0
for value in list:
    total = total + value
print("Total:", total)

avg = total / len(list)
print("Average:", avg)

max = list[0]
for value in list:
    if value > max:
        max = value
print("Maximum:", max)

min = list[0]
for value in list:
    if value < min:
        min = value
print("Miximum:", min)

interest_list = []
for value in list:
    interest_value = value + value*0.2 #i substituted Original_value with value
    interest_list.append(interest_value)
print("Your five interest values:", interest_list)

#MODULE 5: OPTION 1

def concatenation_rev(string_1, string_2, string_3):
    concatenated_string = string_1 + string_2 + string_3
    return concatenated_string[::-1]

def main():
    s1 = str(input("Enter your first string: \n"))
    s2 = str(input("Enter your second string: \n"))
    s3 = str(input("Enter your third string: \n"))
    rev_str = concatenation_rev(s1, s2, s3)

    print("Concatenation of the three strings in reverse order:", rev_str)

main()

#MODULE 6: OPTION 2

list_a = []
A = int(input("Enter the number of elements for list a (10 is the maximum): \n"))

if A >= 11:
    print("You entered a value over 10, please choose a lower number.")
else:
    for i in range(0, A):
        ele1 = int(input("Enter an integer to add: \n"))
        list_a.append(ele1)

list_b = []
B = int(input("Enter the number of elements for list b (10 is the maximum): \n"))

if B >= 11:
    print("You entered a value over 10, please choose a lower number.")
else:
    for i in range(0, B):
        ele2 = int(input("Enter an integer to add: \n"))
        list_b.append(ele2)

def cartesian_product(list_a, list_b):
    C = []
    for value_a in range(0,len(list_a)):
        for value_b in range(0, len(list_a)):
            value = (list_a[value_a], list_b[value_b])
            C.append(value)
    return C

print("AxB =", cartesian_product(list_a, list_b))
