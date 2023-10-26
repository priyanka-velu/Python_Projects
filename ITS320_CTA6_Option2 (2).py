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

