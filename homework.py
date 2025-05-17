# Завдання 1

# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self, brand: str, model: str, engine: str, color: str, mileage: int, year: int, price: int):
        self.__brand = brand
        self.__model = model    
        self.__engine = engine
        self.__color = color
        self.__mileage = mileage
        self.__year = year
        self.__price = price
    
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_engine(self):
        return self.__engine
    def get_color(self):
        return self.__color
    def get_mileage(self):
        return self.__mileage
    def get_year(self):
        return self.__year
    def get_price(self):
        return self.__price
    
    def set_brand(self, brand: str):
        self.__brand = brand
    def set_model(self, model: str):
        self.__model = model
    def set_engine(self, engine: str):
        self.__engine = engine
    def set_color(self, color: str):
        self.__color = color
    def set_mileage(self, mileage: int):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            return 'Некоректий пробіг'
    def set_year(self, year: int):
        if year > 1886 and year < 2025:
            self.__year = year
        else:
            return 'Некоректний рік'
    def set_price(self, price: int):
        if price >= 0:
            self.__price = price
        else:
            return 'Некоректа ціна'

# Завдання 2

# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). 
# Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній функції (функція hello_friend).

class Language:
    def __init__(self, word: str):
        self.word = word
    def greetings(self):
        pass
class Eng(Language):
    def greetings(self):
        print(self.word)
class Esp(Language):
    def greetings(self):
        print(self.word)
    
eng = Eng('Hello')
esp = Esp('Hola')

def hello_friend(object: Language):
    object.greetings()

hello_friend(eng)
hello_friend(esp)
# Завдання 3

# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. 
# Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
 
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature
 
    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
        
# Завдання 4

# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.

# Завдання 5

# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. 
# Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами. В результаті повинно з’явитися зображення. Перегляньте їх.