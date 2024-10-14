
# Program untuk mencetak deret Fibonacci hingga nilai maksimum n
def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil


n = int(input("Masukkan nilai n: "))

print(f"Deret Fibonacci sampai {n}: {fibonacci(n)}")
