import moneyfmt

cash_user = moneyfmt.MoneyFmt(12345678.021)
print(cash_user.str())
print(cash_user.update(1555.86878))
cash_user.update(-1323.862458)
print(cash_user.str())
