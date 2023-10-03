# class Transport:
#     def move(self):
#         print('движемся')

# class Boat(Transport):
#     def move(self):
#         super().move()
#         print('плывет')

# class Car(Transport):
#     def move(self):
#         super().move()
#         print('едет')

# car = Car()
# boat = Boat()
# car.move()
# boat.move()











# class Call:
#     def call(self):
#         print('call')

# class Mail:
#     def send_letter(self):
#         pass

# class Phone(Call, Mail):
#     pass

# phone = Phone()
# print(issubclass(Phone))
# print(isinstance(Phone, Mail))

# issubclass - проверяет является ли один класс под классом другого
# isinstance - 



# class Parent1:
#     def method(self):
#         print('asdf')

# class Parent2:
#     def method(self):
#         print('ddddd')

# class Child(Parent1, Parent2)
#     pass
# child = Child()
# child.method()








# class A:
#     def __str__(self) -> str:
#         return 'A'
    
# class B(A):
#     def __str__(self) -> str:
#         return 'B'
    
# class C(A):
#     def __str__(self) -> str:
#         return 'C'
    
# class D(B, C):
#     pass

# d = D()



#  Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию
# должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона. 
# У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

# Создайте два дочерних класса от Smartphone - Iphone и Samsung.
# У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.
# А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.
# Создайте объекты от данных классов и примените все методы.


# class Person:
#     def __init__(self, name) -> None:
#         self.name = name    

#     def display_info(self):
#         print(f'Name: {self.name}')

# class Employee(Person):
#     def work(self):
#         print('work!!!!')

# john = Person('John')
# tom = Employee('tom')
# john.display_info()
# tom.display_info()



# class SmartPhone:
#     def __init__(self, name, color, memory, batter) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.batter = 0
# class InfoPhone(SmartPhone):
#     def __str__(self) -> str:
#         super().__str__()
#         print(f'info:/n{self.name}/n{self.color}/n{self.memory}/n{self.batter}')
    

# class Smartphone():
#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self) -> str:
#         return f'Name: {self.name}, Memory: {self.memory}'
    
#     def charge(self, num):
#         self.battery += num

# class Iphone(Smartphone):
#     def __init__(self, name, color, memory) -> None:
#         super().__init__(name, color, memory)
#         self.ios = '17.0'

#     def send_imessage(self):
#         return f'Send by: {self.name}'
    


# class Samsung(Smartphone):
    
#     def __init__(self, name, color, memory) -> None:
#         super().__init__(name, color, memory)
#         self.android = '9.0'

#     def show_time(self):
#         from datetime import datetime
#         cur = datetime.now()
#         return f'{cur.hour}:{cur.minute}:{cur.second}'
    
    
# samsung = Samsung('Samsung', 'Black', '256')
# iphone = Iphone('Iphone', 'White', '512')

# print(samsung)
# print(iphone)
# print(' ')
# samsung.charge(30)
# print(samsung.battery)
# print(' ')
# iphone.charge(40)
# print(iphone.battery)
# print(' ')
# print(samsung.show_time())
# print(' ')
# print(iphone.send_imessage())











# Mixin - это классы примеси задачей которых является резшерение функционаладругого класса
# Mixin - ипользуется для добавление одних и тех же методов в разные классы






# Создайте класс ColorMixin, который содержит атрибут color и методы set_color и get_color. Затем создайте классы Car и Fruit, которые наследуются от ColorMixin,
# чтобы добавить атрибут и методы для работы с цветом. Создайте объекты разных классов и установите и получите их цветы. 
# # реши мне

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Задач под таким ключем уже существует.'
#         self.todos[key] = todo
#         return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         if key not in self.todos:
#             return 'Такого ключа нет.'
#         deleted = self.todos.pop(key)
#         return deleted

# class UpdateMixin:
#     def update(self, key, new_value):
#         if key not in self.todos:
#             return 'Такого ключа нет.'
#         self.todos[key] = new_value
#         return self.todos       

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())

# class Notes(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

# todo = Notes()
# print(todo.create('oop', 'python'))
# print(todo.create('paring', 'python1'))
# print(todo.create('Jango', 'python2'))
# print(todo.create('Datatipe', 'python3'))

# print(todo.delete('java'))
# print(todo.delete('python'))

# print(todo.update('java', 'string'))
# print(todo.update('python1', 'Linux'))

# print(todo.read())







