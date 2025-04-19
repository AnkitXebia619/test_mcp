def add_two_numbers(a, b):
    """
    Function to add two numbers
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of the two numbers
    """
    return a + b

def main():
    # Get input from user
    print("Program to add two numbers")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Call the function and display result
        result = add_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main()
