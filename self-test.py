from groupby import df, money_quantity, all_money

df.must_money = df.must_money.map(lambda x: int(x.replace(',', '')
                                                .removesuffix('.00')))
money_must = df.must_money.sum()
payment_money = money_quantity.money.sum()
print(payment_money, "\n", money_must)

if all_money == payment_money + money_must:
    print("Ok")
    money_quantity.to_csv("money_quantity.csv", index=False)
else:
    print("ERROR!!!!!!")
