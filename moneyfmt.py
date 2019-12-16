class MoneyFmt:
    def __init__(self, cash):
        self.cash = cash

    def update(self, cash):
        self.cash = cash
        # return

    def repr(self, cash):
        self.cash = cash
        self.cash = float(input('Enter your integer: '))

    def str(self):
        if self.cash >= 0:
            return '${:,.2f}'.format(self.cash)
        else:
            return '-${:,.2f}'.format(-self.cash)


# test!!

# cash_user = MoneyFmt(12345678.021)
# print(cash_user.str())
# cash_user.update(1555.86878)
# print(cash_user.str())
# cash_user.update(-1323.862458)
# print(cash_user.str())



# def dollarize():
#     money = float(input('Enter your integer: '))
#     Formatted_money = ' $ {:,.2f}'.format(money)
#     print(Formatted_money)
#
# dollarize()