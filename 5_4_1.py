# Создание класса
class House:
    # Создание атрибута для хранения объектов
    houses_history = []

    # Применение метода __new__
    def __new__(cls, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(kwargs['house'])
        return instance

    # Назначение атрибутов для объектов класса
    def __init__(self, house, age):
        self.house = house
        self.age = age

    # Создание метода __del__
    def __del__(self):
        print(f"Объект {self.house} удален, но он останется в истории")

# Cоздаем несколько объектов класса House
# с последовательной распечаткой значения houses_history
house1 = House(house='Чиполлино', age=25)
print(House.houses_history)
house2 = House(house='Буратино', age=27)
print(House.houses_history)
house3 = House(house='Папа Карло', age=36)
print(House.houses_history)

# проверяем работу метода __del__
del house2
del house3
print(House.houses_history)