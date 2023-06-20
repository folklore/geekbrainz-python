from datetime import datetime

class TellerMachine():
    AMOUNT_FILE = 'amount.txt'
    EXIT_PIN_CODE = 0
    MAX_ATTEMPTS_COUNT = 3

    # Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
    DEDUCTION_PERCENT = 1.5
    MIN_DEDUCTION = 30
    MAX_DEDUCTION = 600

    # При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией
    REACH_EDGE_VALUE = 5_000_000
    REACH_EDGE_PERCENT = 10


    def __init__(self):
        self.amount = self.__select_amount()
        self.__looger = self.__Logger()


    def withdrawal(self, card, value):
        # Сумма пополнения и снятия кратны 50 у.е.
        if value % 50 == 0:
            # Процент за снятие — 1.5% от суммы снятия
            deduction = value * self.DEDUCTION_PERCENT / 100

            # Процент за снятие не менее 30 и не более 600 у.е.
            if deduction < self.MIN_DEDUCTION:
                deduction = self.MIN_DEDUCTION
            elif deduction > self.MAX_DEDUCTION:
                deduction = self.MAX_DEDUCTION
            
            total_value = value + deduction

            # При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией
            if value > self.REACH_EDGE_VALUE:
                total_value += (total_value * self.REACH_EDGE_PERCENT / 100)

            # Нельзя снять больше, чем на счёте
            if self.amount >= total_value and card.balance >= total_value:
                self.amount -= total_value
                self.__update_amount()

                card.withdrawal(total_value)
                self.__looger.write(f'Withdrawal    | Summa {total_value}')
                return 'ok'
            elif card.balance < value:
                self.__looger.write(f'Withdrawal    | Not enough minerals)) on the card')
                return 'card deny'
            elif self.amount < value:
                self.__looger.write(f'Withdrawal    | Not enough minerals)) in the ATM')
                return 'atm deny'
        else:
            self.__looger.write(f'Withdrawal    | Multiplicity deny')
            return 'multiplicity deny'


    def replenishment(self, card, value):
        # Сумма пополнения и снятия кратны 50 у.е.
        if value % 50 == 0:
            self.amount += value
            self.__update_amount()

            card.replenishment(value)
            self.__looger.write(f'Replenishment | Summa {value}')
            return 'ok'
        else:
            self.__looger.write(f'Replenishment | Multiplicity deny')
            return 'multiplicity deny'


    def run(self):
        card = Card()
        interface = self.__Interface(self)

        attempts_count = self.MAX_ATTEMPTS_COUNT

        while attempts_count > 0:
            attempts_count -= 1

            pin_code = interface.login()

            if pin_code == self.EXIT_PIN_CODE:
                quit()
            elif card.verify(pin_code):
                interface.greeting()

                break
            else:
                interface.rejection()

                if attempts_count == 0:
                    quit()

        while True:
            # Любое действие выводит сумму денег
            interface.balance(card.balance)

            interface.home()

            route = interface.route()

            # Допустимые действия: баланс, пополнить, снять, выйти
            if route == self.EXIT_PIN_CODE:
                quit()
            elif route == 1:
                interface.balance(card.balance)
            elif route == 2:
                value = interface.withdrawal()
                state = self.withdrawal(card, value)

                interface.withdrawal_result(state)
            elif route == 3:
                value = interface.replenishment()
                self.replenishment(card, value)

                interface.replenishment_result(state)


    def __select_amount(self):
        with open(self.AMOUNT_FILE, 'r') as file:
            return float(file.readline())


    def __update_amount(self):
        with open(self.AMOUNT_FILE, 'w') as file:
            file.write(str(self.amount))


    class __Interface():
        def __init__(self, atm):
            self.atm = atm


        def __header(self):
            print('######################')
            print('#                    #')
            print('# Банк Рога и Копыта #')
            print('#                    #')


        def login(self):
            self.__header()
            print('# Введите пин-код    #')
            print('#                    #')
            return int(input('# >'))


        def greeting(self):
            self.__header()
            print('# Добро пожаловать!  #')
            print('#                    #')
            print('#                    #')


        def rejection(self):
            self.__header()
            print('# Посторонним        #')
            print('#    вход воспрещен! #')
            print('#                    #')


        def home(self):
            self.__header()
            print('# 1 Проверить баланс')
            print('# 2 Снять со счета')
            print('# 3 Внести на счет')


        def route(self):
            return int(input('Введите номер операции (или 0 для выхода): '))


        def balance(self, balance):
            self.__header()
            print('# Ваш баланс:        #')
            print('#                    #')
            print(f'# {balance}')


        def withdrawal(self):
            self.__header()
            print('# Введите сумму      #')
            print('#   снятия ...       #')
            return int(input('# >'))


        def withdrawal_result(self, state):
            self.__header()
            if state == 'ok':
                print('# Не забудьте        #')
                print('#   забрать деньги   #')
            elif state == 'atm deny':
                print('# Недостаточно       #')
                print('#   денег в АТМ      #')
            elif state == 'card deny':
                print('# Недостаточно       #')
                print('#   денег на карте   #')
            elif state == 'multiplicity deny':
                print('# Сумму снятия       #')
                print('#   не кратна 50     #')
            print('#                    #')


        def replenishment(self):
            self.__header()
            print('# Введите сумму      #')
            print('#   пополнения ...   #')
            return int(input('# >'))


        def replenishment_result(self, state):
            self.__header()
            if state == 'ok':
                print('# Деньги успешно     #')
                print('#   зачислены        #')
            elif state == 'multiplicity deny':
                print('# Сумму пополнения   #')
                print('#   не кратна 50     #')
            print('#                    #')


    class __Logger():
        LOG_FILE = 'log.txt'


        def write(self, text):
            with open(self.LOG_FILE, 'a') as file:
                line = f'{datetime.now()} | {text}\n'
                file.write(line)


class Card():
    BALANCE_FILE = 'balance.txt'
    PIN_CODE = 1234


    def __init__(self):
        self.balance = self.__select_balance()


    def verify(self, code):
        return self.PIN_CODE == code


    def withdrawal(self, value):
        self.balance -= value
        self.__update_balance()


    def replenishment(self, value):
        self.balance += value
        self.__update_balance()


    def __select_balance(self):
        with open(self.BALANCE_FILE, 'r') as file:
            return float(file.readline())


    def __update_balance(self):
        with open(self.BALANCE_FILE, 'w') as file:
            file.write(str(self.balance))


atm = TellerMachine()
atm.run()
