

#1 Создайте класс MathUtils с staticmethod под названием multiply, который принимает два аргумента и возвращает их произведение.


class MathUtils:
    @staticmethod
    def multiply(x, y):
        return x + y
    
result_sum = MathUtils.multiply(5, 3)

print('произведение:', result_sum)




# 2)Создайте класс DateUtils с classmethod под названием is_valid_date, который принимает строку в формате даты (например, "2023-07-18") и проверяет,
# является ли эта дата действительной. Метод должен возвращать True, если дата действительна, и False в противном случае.
# from datetime import date

from datetime import datetime
class DateUtils:
    @classmethod
    def is_today(cls, date_string):
        try:
            parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError:
            return False
        
        current_date = datetime.now().date()
        
        return parsed_date.date() == current_date

date_str = '2023-10-03'

dateutils = DateUtils
res = dateutils.is_today(date_str)
print(res)






# 3)Создайте класс StringUtils с staticmethod под названием is_palindrome, который принимает строку и проверяет, является ли она палиндромом (читается одинаково слева направо и 
# справа налево). Метод должен возвращать True, если строка является палиндромом, и False в противном случае.



class StringUtils:
    @staticmethod
    def is_palindrome(input_string):
        cleaned_string = input_string.lower()

        cleaned_string = cleaned_string.replace(' ', '')

        return cleaned_string == cleaned_string[::-1]

word = input('Введите строку: ')
result = StringUtils.is_palindrome(word)

print(result)









# 4)Создайте класс Shape с staticmethod под названием get_circle_area, который принимает радиус и возвращает площадь круга. Площадь круга вычисляется по формуле πr^2, 
# где π примерно равно 3.14159.


import math

class Shape:
    @staticmethod
    def get_circle_area(radius):
        area = math.pi * radius**2
        return area

radius = 5
area = Shape.get_circle_area(radius)

print(f'Площадь круга с радиусом {radius} равен {area:.2f}')











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
