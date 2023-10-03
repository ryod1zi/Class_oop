#  Создайте программу по следующему описанию. Создайте  родительские классы: Smartphone и Watch. От этих классов  создайте дочерний класс Smartwatch.
# В родительских классах должны быть методы: в Smartphone - метод call, который должен звонить на определенный номер, и в Watch - метод see_time, 
# который выдает вам реальное время на данный момент.  Создайте объект от класса SmartWatch и вызовите оба метода. 
# Также в обоих родительских классах должен быть реализован метод where_to_wear, который говорит вам, где нужно носить данный гаджет. 
# В классе Smartphone он выдает вам строку “You can keep me anywhere”, а в классе Watch - строку “You should wear me on your hand”.
# Данный метод наследуется и в дочернем классе, и должен выдавать вам строку “You should wear me on your hand”. Вызовите и этот метод у объекта класса Smartwatch.



from datetime import datetime
class Smartphone:
    def call(self, phone_number):
        print(f'Calling {phone_number}')

    def where_to_wear(self):
        print('You can keep me anywhere')

class Watch:
    def see_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'Current time is {current_time}')

    def where_to_wear(self):
        print('You should wear me on your hand')

class Smartwatch(Smartphone, Watch):
    pass

smartwatch = Smartwatch()

smartwatch.call('222-222-222') 
smartwatch.see_time()  

smartwatch.where_to_wear()





# Создайте программу по следующему описанию. Есть классы: Instagram, TikTok. Когда вы создаете объекты от этих классов, то вам необходимо указать в аргументах username и пароль,
# таким образом вы регистрируетесь в каждой из соцсети. Далее в  классе Instagram есть метод post_post, который будет принимать в качестве аргументов название поста, username
# и пароль  вашего пользователя. Если пароль и пользователь указаны  верно, то вам выдается сообщение: “Successfully created”.  Аналогично с классом TikTok: метод post_video, 
# принимает  название видео, username и пароль, при верном вводе выдается сообщение “Successfully created”. При создании поста или же видео, у вашего юзера должно увеличиться 
# количество постов в одной из соцсети в зависимости от того, где вы его  опубликовали. Создайте миксин, который будет проверять верны ли пароль и username пользователя при 
# попытке создания поста или видео.




class AuthMixin:
    def authenticate(self, username, password):
        return username == self.username and password == self.password

class Instagram(AuthMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = 0  

    def post_post(self, post_title, username, password):
        if self.authenticate(username, password):
            self.posts += 1
            print(f"Successfully created post '{post_title}' on Instagram. Total posts: {self.posts}")
        else:
            print("Authentication failed. Unable to create post on Instagram.")

class TikTok(AuthMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.videos = 0 

    def post_video(self, video_title, username, password):
        if self.authenticate(username, password):
            self.videos += 1
            print(f"Successfully created video '{video_title}' on TikTok. Total videos: {self.videos}")
        else:
            print("Authentication failed. Unable to create video on TikTok.")

instagram_user = Instagram(username="user_instagram", password="password_instagram")
tiktok_user = TikTok(username="user_tiktok", password="password_tiktok")

instagram_user.post_post(post_title="My First Post", username="user_instagram", password="password_instagram")
tiktok_user.post_video(video_title="Funny Dance", username="user_tiktok", password="password_tiktok")

instagram_user.post_post(post_title="Another Post", username="wrong_user", password="wrong_password")
tiktok_user.post_video(video_title="Cool Video", username="wrong_user", password="wrong_password")
