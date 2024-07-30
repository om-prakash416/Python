# Function to print Fibonacci series
def fibonacci_series(n):
    if n <= 0:
        print("Number of terms must be positive.")
    elif n == 1:
        print("Fibonacci sequence: 0")
    else:
        a, b = 0, 1
        print("Fibonacci sequence:", end =" ")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
# Input from the user
number_of_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci series
fibonacci_series(number_of_terms)

