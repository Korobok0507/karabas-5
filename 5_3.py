# Создание функции проверки корректности ввода этажей
def control():
    while True:
        user_input = input()
        try:
            return int(user_input)
        except ValueError:
            print("Введите корректные данные")

# Создание класса и назначение атрибутов для объектов класса
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Создание спец. методов len и str для класса House
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    # Создание спец. методов сравнения и арифметики для класса House
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            raise TypeError("Неподдерживаемый тип операнда для ==")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            raise TypeError("Неподдерживаемый тип операнда для <")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            raise TypeError("Неподдерживаемый тип операнда для <=")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            raise TypeError("Неподдерживаемый тип операнда для >")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            raise TypeError("Неподдерживаемый тип операнда для >=")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            raise TypeError("Неподдерживаемый тип операнда для !=")

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            raise TypeError("Неподдерживаемый тип операнда для +")

    def __radd__(self, value):
          return self.__add__(value)

    def __iadd__(self, value):
          return self.__add__(value)

    # Вывод на печать атрибутов по заданным пользователем данным
    def info(self):
        print(f'Название жилого комплекса: {str(self)}, Этажность: {len(self)}')

# Функция печати сравнений
def infoprint():
    print(f'{house1 == house2} (Проверка равенства)') # __eq__
    print(f'{house1 > house2} (Проверка: первыбольше второго)')  # __gt__
    print(f'{house1 >= house2} (Проверка: первый больше или равен второму)')  # __ge__
    print(f'{house1 < house2} (Проверка: первый меньше второго)')  # __lt__
    print(f'{house1 <= house2} (Проверка: первый меньше или равен второму)')  # __le__
    print(f'{house1 != house2} (Проверка неравенства)')  # __ne__

# Запрос атрибута name (название)
print("Введите название первого жилого комплекса:")
name1 = input()
print("Введите название второго жилого комплекса:")
name2 = input()

# Запрос атрибута number_of_floors (этажность)
print("Введите этажность первого комплекса:")
number_of_floors1 = control()
print("Введите этажность второго комплекса:")
number_of_floors2 = control()

# Создание объектов house с атрибутами name и number_of_floors (название и этажность)
house1 = House(name1, number_of_floors1)
house2 = House(name2, number_of_floors2)

# Вызов метода info для объектов house
house1.info()
house2.info()
# Вызов функции печати сравнений
infoprint()

# Запрос на увеличение этажности каждого жилого комплекса
print("Введите количество этажей, на которое нужно увеличить первый жилой комплекс:")
increase_floors1 = control()
print("Введите количество этажей, на которое нужно увеличить второй жилой комплекс:")
increase_floors2 = control()

# Увеличение на заданное количество этажей
house1 += increase_floors1
house2 += increase_floors2

# Вызов метода info для объектов house после увеличения этажей
house1.info()
house2.info()
# Вызов функции печати сравнений
infoprint()