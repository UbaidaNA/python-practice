# Printing out a triangle of integers. This uses integer division to print out numbers. Numbers should be between 0 and 10

number = int(input("Enter a number: "))
for i in range(1, number + 1):
    print(10**i//9*i) #This divides  10 raised to a certain number by 9 times the same number and prints the numbers after the decimal place
