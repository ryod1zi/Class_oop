# print(len([1,2,3,4]))
# print(len('123123'))
# print(len({1:2, 3:4}))

# # полеморфизм это возможность использовать одтн т ьоь же метод для обьектов от разных классов
# # при этом результат меняется в зависимости к какому классу принадлежит обьект



# def sum_elements(a, b):
#     return a + b
# print(sum_elements('a', 'b'))
# print(sum_elements(1,2))






# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def make_sound(self):
#         print('meeeyaaaau')

# class Dog:
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age
#     def make_sound(self):
#         print('gav gav gav gav')
        
# cat = Cat('Cat', 2)
# dog = Dog('dog', 5)

# # for sound in [cat, dog]:
# #     sound.make_sound()

# class ShapeMixin:
#     def __init__(self, name) -> None:
#         self.name = name

#     def area(self):
#         pass

#     def __str__(self) -> str:
#         return self.name
    
# class Circle(ShapeMixin):
#     def __init__(self, radius) -> None:
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         from math import pi
#         return pi*self.resius**2
    
# class Square(ShapeMixin):
#     def __init__(self, length) -> None:
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
#     def __str__(self) -> str:
#         return f'{self.name}-{self.length}'

# a = Square(5)
# b = Circle(7)
# print(a.area())
# print(b.area())
# print(b)
# print(a)




# class Tomato:
#     def type(self):
#         print('vegotable')
#     def color(self):
#         print('red')

# class Apple:
#     def type(self):
#         print('fru')
#     def color(self):
#         print('red')
# def func(obj):
#     obj







# class Shape(ABC):
#     @abstractmethod
#     def calculater_are(self):
#         pass
#     @abstractmethod
#     def calculater_perimetr(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius
#     def calculater_are(self):
#         return self.radius ** 2 *pi
#     def calculater_perimetr(self):
#         return self.radius * 2 *pi

# class Reactengle(Shape):
#     def __init__(self, width, height) -> None:
#         self.height = height
#         self.width = width
#     def calculater_are(self):
#         return self.height * self.width
#     def calculater_perimetr(self):
#         return (self.height + self.width)
    
# circle = Circle(5)
# reactengle =Reactengle(4,6)

# print('площадь круга', circle.calculater_are())
# print('периметр круга', circle.calculater_perimetr())
# print('плошадь прямоугольника', reactengle.calculater_are())
# print('периметыр прямоугольника', reactengle.calculater_perimetr())








# Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. 
# При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. 
# При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку 
# “I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image 
# True, то выдается сообщение “I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice
# message в виде строки и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.

# class WhatsApp:
#     def __init__(self, number) -> None:
#         self.number = number

#     def send(self, text):
#         self.text = text
#         print(f'I am sending a text {text}')
        
# class SnapChat:
#     def __init__(self,number) -> None:
#         self.number = number

#     def send(self,text,image):
#         if image == True:
#             print('I am sending a text ' +text+' with some image')
#         else:
#             print('I am sending a text ' +text+' without image')

# class Telegram:
#     def __init__(self,number, username) -> None:
#         self.number = number
#         self.username = username

#     def send(self,text):
        
#         self.massage = (f'I am sending a voice massage {text}')
#         print(self.massage)

# whatsapp = WhatsApp(777-000-777)
# snapchat = SnapChat(777-000-777)
# telegram = Telegram(777-000-777, 'ryod_zi')

# whatsapp.send('text')
# snapchat.send('ttwt',True)
# telegram.send('voice')








# Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
# а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.








class A:
    def count(self, word):
        vowels = "aeiouAEIOU"
        count_vowels = sum(1 for char in word if char in vowels)
        print(f"Class A: Number of vowels in '{word}': {count_vowels}")

class B:
    def count(self, word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count_consonants = sum(1 for char in word if char in consonants)
        print(f"Class B: Number of consonants in '{word}': {count_consonants}")

obj_a = A()
obj_b = B()

obj_a.count("Rakhim")  
obj_b.count("Rakhim")  
