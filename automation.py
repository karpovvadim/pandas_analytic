import pandas as pd
from datetime import datetime


df = pd.read_csv("analytic_example_1.csv")
df = df.rename(columns={'Дата оплаты': 'payment_date',
                        'Сумма': 'money',
                        'Наименование товара, услуги': 'name_of_product_service',
                        'Категория дохода': 'income_category',
                        'Количество': 'quantity',
                        'Себестоимость единицы': 'unit_cost',
                        'Себестоимость общая': 'total_cost',
                        'Маржа': 'margin_money',
                        'Маржа, %': 'margin_%',
                        'Статус платежа': 'payment_status',
                        'Тип платежа': 'payment_type',
                        'Должны': 'must_money',
                        'Комментарий': 'comment'
                        })
all_money = df.money.sum()
df.must_money = df.must_money.map(lambda x: int(x.replace(',', '')
                                                .removesuffix('.00')))
money_must = df.must_money.sum()
money_quantity = (df  # .head()  # print - "ERROR!!!!!!"
                  .query("payment_status == 'Оплачено'")
                  .groupby(['name_of_product_service'], as_index=False)
                  .aggregate({"money": "sum", "quantity": "count"})
                  .sort_values("money", ascending=False))

payment_money = money_quantity.money.sum()

today_day = datetime.today().strftime('%y-%m-%d')
file_name = 'money_quantity_{}.csv'
file_name = file_name.format(today_day)

if all_money == payment_money + money_must:
    print("Ok! File {} is written.".format(file_name))
    money_quantity.to_csv(file_name, index=False)
else:
    print("ERROR!!!!!!")

print(df[['name_of_product_service', 'payment_status']], "\n", money_quantity)
