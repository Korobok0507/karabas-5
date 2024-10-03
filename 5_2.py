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

    # Определение принадлежнасти заданного этажа введенным
    # данным этажности и вывод на печать результатов
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'Этаж: {new_floor}')
        else:
            print("Такого этажа не существует")

    # Создание спец. методов len и str для класса House
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return self.name

    # Вывод на печать атрибутов по заданным пользователем данным с помощью спец. методов str и len
    def info(self):
        print(f'Название жилого комплекса: {str(self)}, Этажность: {len(self)}')

# Запрос атрибута name (название)
print("Введите название жилого комплекса:")
name = input()

# Запрос атрибута number_of_floors (этажность)
print("Введите этажность:")
number_of_floors = control()


# Создание объекта house с атрибутами name и number_of_floors (название и этажность)
house = House(name, number_of_floors)

# Запрос этажа
print("Введите этаж:")
new_floor = control()

# Вызов метода go_to для объекта house (определения этажа)
house.go_to(new_floor)
# Вызов метода info для объекта house
house.info()