import math

def calculate_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        sin_sum = sum(math.sin(j) for j in range(1, i + 1))
        total_sum += 1 / sin_sum
    return total_sum

n = int(input("n qiymatini kiriting: "))
result = calculate_sum(n)
print(f"Yig'indi: {result}")
