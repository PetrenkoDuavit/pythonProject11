# HW 11.1
def prime_generator(end):
    for num in range(2, end + 1):  # создаем и перебераем список
        is_prime = True # поумолчанию True
        for i in range(2, int(num ** 0.5) + 1):  # Проверка являится число простым или нет
            if num % i == 0: # проверка если у числа еще один делитель
                # , если в  is_prime = False и прерываем цмкл
                is_prime = False
                break
        if is_prime:
            yield num  # Возвращаем простое число

# HW 11.2

def generate_cube_numbers(end):
    startFrom = 2  # начало с 2-х
    while True: # цикл заканчивается
        numberInCube = startFrom ** 3  # приведение в 3ю степень
        if numberInCube > end: # если чило в кубе больше end заверщаем проверку
            break
        yield numberInCube  # Возвращаем чило в кубе если оно меньше end
        startFrom += 1  # проверяем следующее число




# HW 11.3
def is_even(number):
    num_is_even = str(number)[-1] in "02468" # перевожу в строку и сравниваю с "02468"
    return num_is_even
    # if number & 1: сравнивет с 1 побитово
    #     return False
    # else:
    #     return True



print("HW 11.1")
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

print("HW 11.2")

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')


print("HW 11.3")
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'