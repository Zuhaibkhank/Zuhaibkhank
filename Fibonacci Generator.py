# Fibonacci Generation Project

# Step 1: Display an introduction
def introduction():
    print("Welcome to the Fibonacci Sequence Generator!")
    print("This program will generate Fibonacci numbers based on your input.")
    print("The Fibonacci sequence starts with 0 and 1, and each number is the sum of the two preceding numbers.\n")

# Step 2: Function to generate Fibonacci using iteration (efficient for larger sequences)
def fibonacci_iterative(n):
    if n <= 0:
        return "Please enter a positive number."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the first two numbers in the sequence
    fib_sequence = [0, 1]

    # Generate the sequence by iterating through a loop
    for i in range(2, n):
        next_value = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_value)

    return fib_sequence

# Step 3: Function to generate Fibonacci using recursion (less efficient for large n, but demonstrates recursion)
def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive number."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Helper function for recursion
    def recursive_helper(a, b, count):
        if count == 0:
            return []
        else:
            return [a + b] + recursive_helper(b, a + b, count - 1)

    # Start with the first two numbers
    return [0, 1] + recursive_helper(0, 1, n - 2)

# Step 4: Function to get user input and validate it
def get_user_input():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms you want to generate: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Step 5: Main function to execute the project
def main():
    # Show introduction
    introduction()

    # Get user input for the number of terms
    n = get_user_input()

    # Choose method of generation
    print("\nChoose the method for generating Fibonacci sequence:")
    print("1. Iterative method (recommended for larger sequences)")
    print("2. Recursive method (for small sequences, slower)")

    method = input("Enter 1 or 2: ")

    # Generate and display Fibonacci sequence
    if method == '1':
        result = fibonacci_iterative(n)
    elif method == '2':
        result = fibonacci_recursive(n)
    else:
        print("Invalid choice. Using iterative method by default.")
        result = fibonacci_iterative(n)

    # Display the result
    print(f"\nFibonacci sequence of {n} terms:")
    print(result)

# Step 6: Execute the program
if __name__ == "__main__":
    main()