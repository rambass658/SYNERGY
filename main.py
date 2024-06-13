import math

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")

    return math.factorial(n)

while True:
    try:
        num = input("Введите положительное целое число: ")

        if not num.isdigit():
            raise ValueError("Некорректный ввод. Введите положительное целое число.")

        num = int(num)

        try:
            factorial = calculate_factorial(num)
            print(f"Факториал числа {num} равен: {factorial}")
        except OverflowError:
            print("Вычисление факториала этого числа требует слишком большого объема памяти.")
        except ValueError as e:
            print(e)

    except Exception as e:
        print("Произошла ошибка:", e)
    else:
        choice = input("Хотите выполнить расчет для другого числа? (Да/Нет): ").lower()
        if choice != "да":
            break