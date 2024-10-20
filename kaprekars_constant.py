def kaprekarRec(n, prev): 
    if n == 0:
        return 0

    # Store current n as previous number 
    prev = n

    # Get four digits of the given number 
    digits = [0] * 4
    for i in range(4):
        digits[i] = n % 10
        n = n // 10  # Use integer division

    # Sort all four digits in ascending order 
    digits.sort()
    
    # Get the number in ascending order
    asc = 0
    for i in range(4):
        asc = asc * 10 + digits[i]

    # Get the number in descending order
    desc = 0
    for i in range(3, -1, -1):
        desc = desc * 10 + digits[i]

    # Get the difference of the two numbers 
    diff = abs(asc - desc)

    # Print the current step
    print(f"{desc} - {asc} = {diff}")

    # If the difference is the same as previous, 
    # we have reached Kaprekar's constant 
    if diff == prev:
        return diff

    # Else recur
    return kaprekarRec(diff, prev) 

# A wrapper over kaprekarRec() 
def kaprekar(n): 
    rev = 0
    return kaprekarRec(n, rev)

# Driver code 
try:
    number = int(input("Enter a four-digit number with distinct digits: \n"))
    
    # Check if the number has four distinct digits
    if len(set(str(number))) != 4 or number < 1000 or number > 9999:
        print("Please enter a valid four-digit number with distinct digits.")
    else:
        print(f"Starting with {number}:")
        final_result = kaprekar(number)
        print(f"Kaprekar's constant reached: {final_result}")
except ValueError:
    print("Invalid input. Please enter a four-digit number.")
