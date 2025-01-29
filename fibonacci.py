def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verificar_fibonacci():
    num = int(input("Informe um número: "))
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")
