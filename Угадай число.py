import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Вы открыли игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У вас есть {max_attempts} попыток.")

    while attempts < max_attempts:
        try:
            guess = int(input("Введите число: "))

            if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print("Поздравляю! Вы угадали число.")
                break

            attempts += 1
            print(f"У вас осталось {max_attempts - attempts} попыток.")

        except ValueError:
            print("Некорректный ввод. Введите целое число.")

    else:
        print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {secret_number}.")

guess_number()