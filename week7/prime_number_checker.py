def is_prime(n: int) -> bool:
    if n == 2:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    i = 3
    sqrt_n = n ** 0.5

    while i <= sqrt_n:
        if n % i == 0:
            return False
        i += 2

    return True

def prime_number_checker(n: int) -> tuple[int, list[int]]:
    total = 0
    prime_numbers = []

    for i in range(n+1):
        if is_prime(i):
            total += i
            prime_numbers.append(i)

    return total, prime_numbers

n = 100
output = f"{n} is {'prime.' if is_prime(n) else 'not prime.'}"
total, primes = prime_number_checker(n)

print(output, f"Primes up to {n}: {primes}", f"Sum of primes: {total}", sep="\n")
