#python looping

#input five floating point numbers
list = []
length = 5

for i in range(length):
    value = float(input("Enter five values: "))
    list.append(value)
print("Your five values:", list)

#total
total = 0
for value in list:
    total = total + value
print("Total:", total)

#average
avg = total / len(list)
print("Average:", avg)

#maximum
max = list[0]
for value in list:
    if value > max:
        max = value
print("Maximum:", max)

#minimum
min = list[0]
for value in list:
    if value < min:
        min = value
print("Miximum:", min)

#interest rate @ 20%
interest_list = []
for value in list:
    interest_value = value + value*0.2 #i substituted Original_value with value
    interest_list.append(interest_value)
print("Your five interest values:", interest_list)
