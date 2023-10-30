#python functions: concatenate and reverse strings

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
