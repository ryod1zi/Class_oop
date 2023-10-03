# ооп это подход праграмираванию(парадигма)

# класс дает нам общую характеристику которуюбудет исполбзовать обект
# обект -это эгземпляр класса


# class A:
#     string= ''#атрибут класса

#     def first_method(self):#метод класса (функция внутри класса)
#         pass
# first_obj = A()
# first_obj.first_method()







# class Animal:

#     def __init__(self, name, animal_type):
#         self.name = name 
#         self.animal_type = animal_type

#     def get_info(self):
#         print(f'меня зовут {self.name}, я {self.animal_type}')
# dog = Animal('Barsik', 'Dog')
# cat = Animal('Leo', 'Cat')
# dog.get_info()
# cat.get_info()









# class People:
#     # res = 0 атрибут класса 
#     def __init__(self, name, national):
#         self.name=name# атрибут эгземпляра класса 
#         self.national=national

#     def get_info(self):
#         print(f'Привет, меня зовут{self.name}')

#     def teranslate_hello(self, hello):
#         print(f'по национальности я - {self.national} на вашем языке это {hello}')

# american = People('Tom', 'american')
# kyrgyz = People('Aibek', 'kyrgyz')
# russian = People('Kolya', 'russian')

# american.teranslate_hello('hello')
# kyrgyz.teranslate_hello('салам')
# print(american.get_info())
# print(american)








# class SelfBank:
#     total =0

#     def add_sum(self, sum_):
#         self.total += sum_
#         return self.total
    
#     def get_total_sum(self):
#         return self.total
    
#     def min_sum(self, sum_):
#         if self.total - sum < 0:
#             print('недостаточно средств')
#             return self.total
#         self.total -= sum_
#         return self.total
    
# rahim = SelfBank()
# print(rahim.get_total_sum())
# print(rahim.add_sum(99999999999999999999999999999999999999999999999))
# print(rahim.min_sum(10000000000))









# class Car:
#     def __init__(self, auto_owner, auto_mark, auto_madel, auto_year):
#         self.owner = auto_owner
#         self.mark = auto_mark
#         self.model = auto_madel
#         self.year = auto_year
#         self.odometer = 0
#         self.is_going = False

#     def go(self, km):
#         self.is_going = True
#         self.odometer += km

# new_car = Car('Peter', 'Tayota', 'Camry', '2004')
















# import random

# class Sniper:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def shoot(self, target):
#         damage = 20
#         target.health -= damage
#         print(f'{self.name} стреяет {target.name}, у {target.name} осталось {target.health}% здоровья.')

#     def is_alive(self):
#         return self.health > 0

# sniper1 = Sniper('снайпер1')
# sniper2 = Sniper('снайпер2')

# while sniper1.is_alive() and sniper2.is_alive():
#     shooter = random.choice([sniper1, sniper2])  
#     target = sniper2 if shooter == sniper1 else sniper1  

#     shooter.shoot(target)

# if sniper1.is_alive():
#     print(f'{sniper1.name} выиграл')
# elif sniper2.is_alive():
#     print(f'{sniper2.name} выиграл')
# else:
#     print('Ничья')















# class Hogwarts:
#     def __init__(self, name, courage, intelligence, justice, ambition):
#         self.name = name
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition

#     def sorting_hat(self):
#         qualities = {
#             'Gryffindor': self.courage,
#             'Ravenclaw': self.intelligence,
#             'Hufflepuff': self.justice,
#             'Slytherin': self.ambition
#         }
#         dominant_quality = max(qualities, key=qualities.get)
#         return (f'{self.name} поступил в факультет {dominant_quality}')

# student1 = Hogwarts('Rahim', courage=100, intelligence=99, justice=98, ambition=97)
# student2 = Hogwarts('Myrza', courage=16, intelligence=21, justice=12, ambition=43)
# student3 = Hogwarts('Rrysya', courage=14, intelligence=23, justice=20, ambition=13)

# print(student1.sorting_hat())
# print(student2.sorting_hat())
# print(student3.sorting_hat())
