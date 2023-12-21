'''
- Get 3 numbers
- Check if they can form a Right Triangle
- with True and False
'''
def right_triangle(numbers):
    numbers.sort()
    if len(numbers) > 3:
        return("You have entered more than 3 numbers, TRY AGAIN")
    else:
        print(f"Your numbers are: {numbers[0]},{numbers[1]},{numbers[2]}\n"
                f"Are they a right triangle? ")
        if numbers[0]**2 + numbers[1]**2 == numbers[2]**2 or numbers[2]**2 + numbers[1]**2 == numbers[0]**2 or numbers[0]**2 + numbers[2]**2 == numbers[1]**2:     #Comparing to see if one of these 3 scenarios are actually true
            print("True")
        else:
            print("False")

numbers=list(map(int, input("Enter Three values: ").split())) #Entering 3 numbers one after another, and the make a list of them for further comparison
right_triangle(numbers)
