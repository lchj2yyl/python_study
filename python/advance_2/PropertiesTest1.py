class Money(object):
    def __init__(self):
        self.__money = 'test'

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money
    money = property(get_money, set_money)
a = Money()
print a.get_money()
a.set_money('nihao')
print a.get_money()

print a.money
a.money = 'nihao'
print a.money
