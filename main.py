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
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


print("HW 11.3")
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'