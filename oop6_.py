# агрегация слабая связь
# композиция сильная связь


# class Engine:
#     value = 2.3

# class Wheel:
#     size = 15

# class Korobka:
#     tipe = 'avtomat'


# class Car:
#     def __init__(self, korobka) -> None:
#         self.korobka = korobka           #  ---  Композиция
#         self.engine = Engine()           #  ---  Агрегация
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

# korobka = Korobka()
# car = Car(korobka)

# print(car.engine.value)
# print(car.wheels[0].size)


# =================== Композиция 

# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)
    

# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def full_salary(self):
#         return f'Total {self.salary.get_total() + self.bonus} '
    
# employee = Employee(1000, 20)
# print(employee.full_salary())



# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)
    

# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus

#     def full_salary(self):
#         return f'Total {self.pay.get_total() + self.bonus}'

# salary = Salary(200)
# employee = Employee(salary, 15)
# print(employee.full_salary())



# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100


# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.batter = Battery()

# class Samsung:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
    

# iphone = Iphone('black')

# battery = Battery()
# samsung = Samsung(battery, 'white')



# =================== Методы в ооп 


# Методы экземпляра 

# Методы класса

# Статические методы 


# class A:
#     def instance_method(self):
#         print('Метод обьекта')
#         print('Первый аргумент ', self)

# obj_a = A()
# obj_a.instance_method()


# Методы класса нужны для создания обьектов и измененя атрибутов класса 
# Для того чтобы сделать метод методом класса нужно обернуть в декоратор

# class B:
#     @classmethod
#     def class_method(cls):
#         print('Класс Метод')
#         print('Первый аргумент: ', cls)

# obj_b = B()
# obj_b.class_method()



# class Car:
#     color = 'blue'

#     @classmethod
#     def change_color(cls, value):
#         print(cls)
#         cls.color = value

#     def change_color(self, value):
#         print(self)
#         self.color = value

# mers = Car()
# tayota = Car()

# print(mers.color)
# print(tayota.color)
# mers.change_color('vailet')
# print(mers.color)
# tayota.change_color('yellow')
# print(tayota.color)
# Car.change_color('orenge')
# print(mers.color)
# print(tayota.color)



# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()

#     def __del__(self):
#         self._dec_counter()
#         del self
    
#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

#     @classmethod
#     def _dec_counter(cls):
#         cls.counter -= 1

# obj1 = C()
# obj2 = C()
# obj3 = C()
# del obj2
# print(C.counter)



# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.radius = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(self.radius*2)
#         print(self.ingredients)

#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, 'mocorella', 'chedder', 'goland', 'parmizan')
#         return pizza
    
# pizza = Pizza(15, 'peperoni', 'mocorella', 'ananas')
# pizza2 = Pizza.four_cheese(16)
# pizza3 = Pizza.four_cheese(23)

# for i in [pizza, pizza2, pizza3]:
#     i.cook()




#1 Создайте класс MathUtils с staticmethod под названием multiply, который принимает два аргумента и возвращает их произведение.


# class MathUtils:
#     @staticmethod
#     def multiply(x, y):
#         return x + y
    
# result_sum = MathUtils.multiply(5, 3)

# print('произведение:', result_sum)




# 2)Создайте класс DateUtils с classmethod под названием is_valid_date, который принимает строку в формате даты (например, "2023-07-18") и проверяет,
# является ли эта дата действительной. Метод должен возвращать True, если дата действительна, и False в противном случае.
# from datetime import date
# class DateUtils:





# from datetime import datetime

# class DateUtils:
#     @classmethod
#     def is_today(cls, date_string):
#         try:
#             parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
#         except ValueError:
#             return False
        
#         current_date = datetime.now().date()
        
#         return parsed_date.date() == current_date

# date_str = '2023-10-03'

# dateutils = DateUtils
# res = dateutils.is_today(date_str)
# print(res)






# 3)Создайте класс StringUtils с staticmethod под названием is_palindrome, который принимает строку и проверяет, является ли она палиндромом (читается одинаково слева направо и 
# справа налево). Метод должен возвращать True, если строка является палиндромом, и False в противном случае.



# class StringUtils:
#     @staticmethod
#     def is_palindrome(input_string):
#         cleaned_string = input_string.lower()

#         cleaned_string = cleaned_string.replace(' ', '')

#         return cleaned_string == cleaned_string[::-1]

# word = input('Введите строку: ')
# result = StringUtils.is_palindrome(word)

# print(result)









# 4)Создайте класс Shape с staticmethod под названием get_circle_area, который принимает радиус и возвращает площадь круга. Площадь круга вычисляется по формуле πr^2, 
# где π примерно равно 3.14159.


# import math

# class Shape:
#     @staticmethod
#     def get_circle_area(radius):
#         area = math.pi * radius**2
#         return area

# radius = 5
# area = Shape.get_circle_area(radius)

# print(f'Площадь круга с радиусом {radius} равен {area:.2f}')











# 5)Создайте класс FileUtils с classmethod под названием get_file_extension, который принимает имя файла в виде строки и возвращает его расширение. Если файл не имеет расширения,
# метод должен возвращать пустую строку. Например, для файла "document.txt" метод должен вернуть ".txt".


class FileUtils:
    @classmethod
    def get_file_extension(cls, file_name):
        parts = file_name.split('.')
        
        if len(parts) > 1:
            return '.' + parts[-1]
        else:
            return ''

file_name = 'document'
extension = FileUtils.get_file_extension(file_name)

print(extension)
