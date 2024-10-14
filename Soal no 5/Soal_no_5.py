# Function to print number pattern
def print_number_pattern(n):
    for i in range(1, n + 1):
        print(f"{str(i) * i}")

# Example usage
n = int(input("Enter the value of n: "))
print_number_pattern(n)

