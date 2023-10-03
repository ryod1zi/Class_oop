# инкапсуляция

# 1) обединение всех свойств и метдов в одну капсулу или класс
# 2) ограничение доступа к методам и отрибутам те скрытие данных

# class Phone:
#     number = '+996222-222-222'

#     def print_number(self):
#         print(f'my numbers is: {self.number}')

# my_phone = Phone()
# my_phone.print_number()

# a = 2 - public
# _a = 2 - protecred
# __a = 2 privat

# class Point:
#     def __init__(self, x=2, y=2, z=2) -> None:
#         self.__x = x
#         self.__y = y
#         self.__z = z 
#     def get_cordinats(self):
#         return self.__x, self.__y, self.__z

#     def set_cordinats(self, x, y, z):
#         if type(x) in (int, float) and type(y) in (int, float) and type(z)
#         self.__x = x
#         self.__y = y
#         self.__z = z


# point = Point(2, 3, 4)
# print(point.get_cordinats)
# point.set_cordinats(1, 4, 3)



# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.__age = age

#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def set_age(self, new_age):
#         if type(new_age) != int:
#             raise ValueError('age must be integer')
#         if 0 < new_age < 100:
#             self.__age = new_age
#         else:
#             raise Exception('age must be in range(0, 100)')
#     @age.getter
#     def get_age(self):
#         return self.age
#     @age.deleter
#     def age(self):
#         if self.__age < 99:
#             raise Exception('we cant delete age')
#         del self.__age
    
# john = Person('john', '18')
# print(john.name)
# john.set_age = 100
# john.delete_age
# print(john.get_age)










# class BankAccount:
#     def __init__(self, account_number, balance) -> None:
#         self.__account_number = account_number
#         self.balance = 0
#     def get_balans(self):
#         return self.balance
#     def set_balans(self, new_balance):
#         if new_balance > 0:
#             self.balance += new_balance
#         else:
#             raise Exception('new_balance должен больше 0')
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             raise Exception('нет денег')
#     @property
#     def account_number(self):
#         return self.__account_number
#     @account_number.getter
#     def get_account_number(self):
#         return self.__account_number








# CRUD   C-create R- read U - update D - delete

# import json 


# class ReadDataMixin:
#     def read(self, file_name):
#         with open(file_name) as file:
#             return json.load(file)


# class PostDataMixin:
#     def create(self, data, file_name, **kwargs):
#         new_id = self.get_max_id(data)
        
#         data.append({'id': new_id, **kwargs})

#         with open(file_name, 'w') as file:
#             json.dump(data, file, indent=4, ensure_ascii=False)

#     def get_max_id(self, data):
#         if data:
#             all_id = [int(i['id']) for i in data]
#             return max(all_id) + 1
#         return 0

# class DeleteMixin:
#     def delete(self, data, file_name, **kwargs):
#         new_id = self.get_max_id(data)
#         data.delete({'id': new_id, **kwargs})
        


# class UpdateDataMixin:
#     def update(self,data,file_name, id, **kwargs):
#         data = self.read(file_name)
#         for post in data:
#             if post.get('id') == id:
#                 post.update(**kwargs)
#         with open(file_name, 'w') as file:
#             json.dump(data, file)





# class ToDo(ReadDataMixin, PostDataMixin, UpdateDataMixin, DeleteMixin):
#     def init(self, user_name) -> None:
#         self.user_name = str(user_name)
#         self.file_name = user_name + '.json'
#         try:
#             self.create_file()
#         except FileExistsError:
#             pass

#     def create_file(self):
#         with open(self.file_name, 'x') as file:
#             json.dump([], file)

# john = ToDo('john')
# john.create(file_name=john.file_name, data=john.read(john))









# class Post:
#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts= []
#         self.id = 0

#     def create_post(self, title, body, image):
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         self.id +=1
#         return{'status': 201, 'msg': 'успешно создан'}
    
#     def retrieve_post(self, post_id):
#         for post in self.post:
#             if post.get('id') == post_id:
#                 return post
#             return {"status": 404, 'msg': 'Not Found'}
    
#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.pop(self.posts.index(post))
#             return {'status': 200, 'msg': 'успешно удален'}
#         return {'status': 404, 'msg': 'not found'}
    
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post.get(id) == post_id:
#                 post.update(**kwargs)
#                 return {'status': 200, 'msg': 'успешно сохранен'}
#             return {'status': 404, 'msg': 'not found'}
        
# post1 = Post('john')
# post2 = Post('mike')

# post1.create_post('good news', 'good news', 'http://helo.kg')
# post2.create_post('bad news', 'bad news', 'http://goodbye.kg')
# post1.create_post('good news2', 'good news', 'http://hello.kg2')

# print(post1.retrieve_post(2))
# print(post2.retrieve_post(1))

# print(post1.update_post(1, title= 'update', body=))







