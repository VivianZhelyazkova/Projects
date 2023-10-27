class CashRegister:

    def __init__(self, money: float):
        self.__money = money

    def get_money(self):
        money = self.__money
        return money

    def add_money(self, amount: float):
        self.__money += amount

    def subtract_money(self, amount: float):
        self.__money -= amount
