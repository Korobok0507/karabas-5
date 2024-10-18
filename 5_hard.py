# Импорт модуля для создания хеш-функций.
import hashlib
# Импорт модуля для работы со временем.
import time

# Создание класса пользователя.
class User:
    # Инициализация атрибутов пользователя (имя, пароль, возраст)
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        # Создание пароля с вызовом метода хеширования пароля.
        self.password = self.hash_password(password)
        self.age = age

    # Создание метода хеширования пароля.
    def hash_password(self, password):
        # Преобразование пароля в байтовую строку, создание объекта хеширования
        # по алгоритму безопасного хеширования SHA-256 в виде
        # шестнадцетиричной строки с последующим преобразованием в целое число
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    # Создание метода сравнения объектов класса User с other
    # по атрибутам с предварительной проверкой на принадлежность other классу User.
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.nickname == other.nickname and self.password == other.password
    def __str__(self):
        return self.nickname

# Создание класса Video с атрибутами:
# название, продолжительность, возрастные органичения (с начальным значением False)
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        # Устанавливаем начальное значение текущего времени = 0
        self.time_now = 0
        self.adult_mode = adult_mode

    # Создание метода __str__ для обращения к
    # объектам класса Video по их атрибуту title (название)
    def __str__(self):
        return self.title

# Создание класса UrTube.
class UrTube:
    # Создание атрибутов класса (список пользователей, список видео, текущий пользователь).
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # Метод идентификации пользователя по имени и паролю
    # (введенный пароль хешируется и его хеш сравнивается с сохранёнными хешами)
    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Пользователь не найден или неверный пароль.")

    # Метод регистрации пользователей по атрибутам: имя, пароль, возраст.
    # Предварительно проверяется наличие введенного имени в списке self.users.
    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            # Автоматический вход после регистрации
            self.current_user = new_user

    # Сброс текущего пользователя.
    def log_out(self):
        self.current_user = None
    # Метод добавления новых видео в список с предварительной
    # проверкой наличия этого видео в списке
    # (в случае отсутствия - новое видео добавляется.
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    # Метод поиска видео по ключевому буквосочетанию (регистр игнорируется).
    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    # Воспроизведение выбранного видео с отсчётом времени.
    def watch_video(self, title):
        # Проверка входа в аккаунт (к просмотру видео
        # пользователь допускается только после входа)
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Начало проверки наличия видео в списке.
        found_video = False  # Флаг для отслеживания, найдено ли видео
        for video in self.videos:
            if video.title == title:
                found_video = True
                # Проверка возраста пользователя соответсвию
                # возрастных ограничения для данного видео.
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                # Цикл воспроизведения с отсчётом времени и
                # выводом текущего времени на консоль.
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now)  # Выводим текущую секунду
                    time.sleep(1)  # Пауза в 1 секунду
                print("Конец видео")
                video.time_now = 0  # Сбрасываем текущее время просмотра.
        # Вывод сообщения об отсутсвии заявленного видео.
        if not found_video:
            print("Видео не найдено.")

# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Ожидается сообщение о возрасте
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Ожидается успешное воспроизведение

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')