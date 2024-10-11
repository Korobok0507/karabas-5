# Функция контроля корректности ввода
def control():
    while True:
        user_input = input()
        try:
            num = int(user_input)
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Введите корректные данные")

# Создание класса и его атрибутов
class House:
    houses_history = []
    houses_del = []

    # Создание метода __new__
    def __new__(cls, **kwargs):
        instance = super().__new__(cls)
        return instance

    # Создание атрибутов объектов класса
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("Введите текущий год: ")
current = control()

# Цикличный запрос данных у пользователя
while True:
    print("Введите имя дома: ")
    nam = input()
    print("Введите год постройки: ")
    year = control()
    house = House(name=nam, age=current-year)

    # Сортировка объектов
    if house.age <= 150:
        House.houses_history.append(house.name)
    else:
        House.houses_del.append(house.name)

    print("Добавить еще один дом? (да - нажать Enter/нет - ввести: нет): ")
    com = input().lower()
    if com == "нет":
        break

# Вывод на печать значений атрибутов класса
print("Объекты:", ', '.join(House.houses_history), "- ещё пока стоят.")
print("Объекты:", ', '.join(House.houses_del), "- уже развалились.")