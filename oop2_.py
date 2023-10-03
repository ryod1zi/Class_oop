# наследование полемарфизм инкапсуляция обстракция асоциация 


# class A:
#     pass
# a = A()
# print(dir(a))

# class A:
#     a =2 

# class B(A):
#     pass

# b = B()
# print(b.a)
# print(dir(b))


# наследование это пирцып ооп позволяюший описать новый класс на основе сушествуешего
# дочерний класс наследует все методы и атрибуты родительского


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




# class A():
#     def method(self):
#         print('метод класса А')

# class B(A):
#     def method(self):
#         print('метод в классе В')

# a = A()
# b = B()
# a.method()
# b.method()





# mro method resolution order (порядок поиска отрибутов)

# print(B.__mro__)
# print(B.mro())






# class Person:
#     def __init__(self, name, age, last_name) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.age = age

# class Student(Person):
#     def __init__(self, age, name,  last_name) -> None:
#         super().__init__(self, name, last_name, age)
        





#     def work(self):
#         print('Student is working')

# student = Student('john', 'snow', 25)
# student.work()










# class A:
#     atr = 'name'
#     def __str__(self)-> str:
#         return self.atr
# a = A()
# print(a)




# class MyStr(str):
#     pass
# obj = MyStr('hello')
# print(obj.upper())






# class R:
#     def write(self):
#         with open(self.name, 'w')as file:
#             file.write('f')

# class W:
#     def read(self):


# class A:
#     pass

# class RWA(R, W, A):
#     def __init__(self,name) -> None:
#         super().__init__()
#         self.name = name 
# file= RWA('f.txt')
# file.write












# class MyDict(dict):
#     def get(self, key, default=None):
#         return super().get(key, 'hay')

# my_dict = MyDict()
# my_dict['existing_key'] = 'Hi'
# print(my_dict.get('existing_key'))  
# print(my_dict.get('non_existing_key'))  












# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class SmartPhone(Phone):
#     def make_call(self):
#         print(f'{self.brand} {self.model} звонок!')

# class BasicPhone(Phone):
#     def make_call(self):
#         print(f'{self.brand} {self.model} звонок!')

# smartphone = SmartPhone('Samsung', 'Galaxy S21')
# basicphone = BasicPhone('Nokia', '3310')

# smartphone.make_call()  
# basicphone.make_call()  












# Создайте базовый класс Animal с атрибутами name и species. Затем создайте подклассы Lion, Elephant, и Giraffe, которые наследуются от Animal. 
# Добавьте метод speak для каждого из подклассов, который выводит звук, издаваемый соответствующим животным. Создайте объекты разных подклассов и вызовите их методы speak.

# class Animal:
#     def __init__(self, name, species) -> None:
#         self.name = name
#         self.species = species

# class Lion(Animal):
#     def speak(self):
#         print(self.name, 'арррр')
        
# class Giraffe(Animal):
#     def speak(self):
#         print(self.name, 'пфффф')
        
# class Elephant(Animal):
#     def speak(self):
#         print(self.name, 'пиииииф')
        
# lion = Lion('билал', 'кошка')
# g = Giraffe('JIRAF', 'jivotnoe')
# e = Elephant('lsfsf', 'sdf')

# lion.speak()
# g.speak()
# e.speak()













# Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. 
# От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык.
# При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. 
# Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript.
# Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку
# “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. 
# Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. 
# После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам 
# результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”


# class Languages:
#   def __init__(self, students, leng):
#     self.students = students
#     self.leng = leng
# class Python(Languages):
#   def num(self):
#     print(self.students)
    
# class JavaScript(Languages):
#   def num(self):
#     # super().students
#     print(self.students)
    

# python = Python(23, 'python')
# java = JavaScript(14, 'javascript')

# python.num()
# java.num()










# import random

# class Languages:
#     num_students = 0

#     @classmethod
#     def increase_students(cls):
#         cls.num_students += 1

#     @classmethod
#     def decrease_students(cls):
#         cls.num_students -= 1

# class Python(Languages):
#     def coding(self):
#         return "I am Python student. I am coding now."

# class JavaScript(Languages):
#     def coding(self):
#         return "I am JavaScript student. I am coding now."

# student1 = Python()
# student2 = JavaScript()

# Languages.increase_students()

# random_student = random.choice([student1, student2])

# guess = input("Какого студента выбрали? (Python/JavaScript): ")

# if guess.lower() == "python":
#     result = random_student.coding()
#     if isinstance(random_student, Python):
#         print("Good job!")
#     else:
#         print("No bueno :(")
# elif guess.lower() == "javascript":
#     result = random_student.coding()
#     if isinstance(random_student, JavaScript):
#         print("Good job!")
#     else:
#         print("No bueno :(")
# else:
#     print("Неправильный ввод. Выберите Python или JavaScript.")

# Languages.decrease_students()


# Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. 
# В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс


# class MyList(list):
#     def insert(self, element, index):
#         super().insert(index, element)

# my_list = MyList([1, 2, 3, 4, 5])
# my_list.insert(6, 2) 
# print(my_list) 











# import random

# class Languages:
#     num_students = 0

#     @classmethod
#     def increase_students(cls):
#         cls.num_students += 1

#     @classmethod
#     def decrease_students(cls):
#         cls.num_students -= 1

# class Python(Languages):
#     def coding(self):
#         return "I am Python student. I am coding now."

# class JavaScript(Languages):
#     def coding(self):
#         return "I am JavaScript student. I am coding now."

# student1 = Python()
# student2 = JavaScript()
# Languages.increase_students()

# random_student = random.choice([student1, student2])

# class_mapping = {
#     "python": Python,
#     "javascript": JavaScript,
# }

# guess = input("Какого студента выбрали? (Python/JavaScript): ").lower()

# if class_mapping.get(guess) == random_student.__class__:
#     print("Good job!")
# else:
#     print("No bueno :(")

# Languages.decrease_students()










