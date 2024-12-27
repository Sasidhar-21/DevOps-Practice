# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
if __name__ == "__main__":
    try:
        # Input from the user
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # Calculate factorial
            result = factorial(num)
            print(f"The factorial of {num} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")


#############
#############
iiii

