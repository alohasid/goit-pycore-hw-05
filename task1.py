def caching_fibonacci():
    cache = {}

    def fibonacci(number):
        if number in cache:
            return cache[number]
        if number == 0 or number == 1:
            value = number
        else:
            value = fibonacci(number - 1) + fibonacci(number - 2)
        cache[number] = value
        return value

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

# print(fib(100500)) # maximum recursion depth exceeded :)
# print (fib(1013)) # 1030 is a maximum number that produce -> 22646159983680509813226762371589617212021546986373121106984311874200271128724548996298102829204501278281258708076897935331177617946596443868211548085027657747351869076024218103527970817405235977065646186641973733
