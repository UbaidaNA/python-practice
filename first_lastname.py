# This prints the first and last names in a sentence using string formating

if __name__ == '__main__':
    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    

def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))

print_full_name(first_name, last_name)