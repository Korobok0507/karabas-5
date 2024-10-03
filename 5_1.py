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

    # Вывод на печать атрибутов по заданным пользователем данным
    def info(self):
        print(f'Название жилого комплекса: {self.name}, Этажность: {self.number_of_floors}')

# Запрос атрибута name (название)
print("Введите название жилого комплекса:")
name = input()

# Запрос атрибута number_of_floors (этажность) и цикл проверки на корректность ввода
while True:
    print("Введите этажность:")
    user_input = input()

    try:
        number_of_floors = int(user_input)
        break
    except ValueError:
        print("Введите корректные данные")


# Создание объекта house с атрибутами name и number_of_floors (название и этажность)
house = House(name, number_of_floors)

# Запрос этажа и проверка корректности ввода
while True:
    print("Введите этаж:")
    user_input = input()

    try:
        new_floor = int(user_input)
        house.go_to(new_floor)
        break
    except ValueError:
        print("Введите корректные данные")

# Вызов метода info для объекта house
house.info()