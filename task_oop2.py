# Создайте класс Terminal. Создайте объект-карточку от этого класса, передав номер своей карточки и пин код.
# При этом, необходимо проверить валидность карточки: номер карточки должен содержать строго 16 цифр, а пин код - 4 цифры (для этого используйте инкапсуляцию). 
# При создании карточки в ней содержится 0 сом. Далее в классе должны быть следующие методы:

# метод put, который будет принимать в качестве аргументов: пин код карточки, вторым аргументом - сумму денег, которую вы хотите закинуть на эту карточку.
# Прежде, чем закидывать деньги, необходимо проверить введенный пин код на совпадение (используйте инкапсуляцию)

# метод get_money, который также принимает первым аргументом пин код, вторым аргументом - сумму денег, которую вы хотите извлечь из карточки. 
# Здесь также необходимо использовать валидацию: проверка пин кода + сумма денег должна быть округленной до десятичных чисел, типа 10, 100, 200, 5000 и т.д. 
# (67, 899, 45.6 - невалидные данные). И только после проверки деньги извлекаются.

# Примените данные методы к своей карточке несколько раз и в конце выдайте, сколько денег на карточке. 
# Примечание: нельзя извлечь сумму денег, если она больше, чем сумма денег на карточке; также нельзя вытащить пин код карточки (эти данные должны быть скрыты)






class Terminal:
    def __init__(self, card_number, pin_code):
        if not isinstance(card_number, int) or len(str(card_number)) != 16:
            raise ValueError("Неверный номер карточки")
        
        if not isinstance(pin_code, int) or len(str(pin_code)) != 4:
            raise ValueError("Неверный пин код")
        
        self.__card_number = card_number
        self.__pin_code = pin_code
        self.__balance = 0

    def __validate_pin(self, entered_pin):
        return entered_pin == self.__pin_code

    def put(self, entered_pin, amount):
        if not self.__validate_pin(entered_pin):
            print("Неверный пин код")
            return
        
        if amount <= 0 or amount % 10 != 0:
            print("Невалидная сумма денег")
            return
        
        self.__balance += amount
        print(f"На карточку зачислено {amount} сом. Текущий баланс: {self.__balance} сом")

    def get_money(self, entered_pin, amount):
        if not self.__validate_pin(entered_pin):
            print("Неверный пин код")
            return

        if amount <= 0 or amount % 10 != 0 or amount > self.__balance:
            print("Невалидная сумма денег или недостаточно средств на карточке")
            return
        
        self.__balance -= amount
        print(f"С карточки снято {amount} сом. Текущий баланс: {self.__balance} сом")

    def check_balance(self):
        return self.__balance



my_card = Terminal(card_number=1234567890123456, pin_code=4321)

my_card.put(4321, 100)

my_card.get_money(4321, 30)

print("Текущий баланс на карточке:", my_card.check_balance())
