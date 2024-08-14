import math

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел.")
    return math.factorial(n)

def main():
    try:
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)
        
        if number < 0:
            raise ValueError("Введенное число должно быть положительным.")
        
        factorial = calculate_factorial(number)
        print(f"Факториал числа {number} равен {factorial}")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()