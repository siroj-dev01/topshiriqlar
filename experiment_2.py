import math

# # Qatorni hisoblash funksiyasi
# def calculate_series(x):
#     terms = [
#         x,
#         -x**3 / math.factorial(3),
#         x**5 / math.factorial(5),
#         -x**7 / math.factorial(7),
#         x**9 / math.factorial(9),
#         -x**11 / math.factorial(11),
#         x**13 / math.factorial(13)
#     ]
#     result = sum(terms)
#     return result

# # Misol uchun foydalanish
# x = float(input("x qiymatini kiriting: "))
# result = calculate_series(x)
# print("Natija:", result)
# Faktorial hisoblash funksiyasi
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Qatorni hisoblash funksiyasi sikl yordamida
def calculate_series(x):
    result = 0
    sign = 1  # Har bir hadning ishorasini belgilash uchun
    for n in range(1, 14, 2):  # 3, 5, 7, ..., 13 darajalari
        result += sign * (x ** n) / factorial(n)
        sign *= -1  # Ishorani o'zgartirish
    return result

# Misol uchun foydalanish
x = float(input("x qiymatini kiriting: "))
result = calculate_series(x)
print("Natija:", result)