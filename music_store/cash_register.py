class CashRegister:

    __money = 0

    @staticmethod
    def get_money():
        money = CashRegister.__money
        return money

    @staticmethod
    def add_money(amount: float):
        CashRegister.__money += amount


