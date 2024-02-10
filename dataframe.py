import pandas as pd

path = "analytic_example_1.csv"
df = pd.read_csv(path)
# print(df.head())
print(df.shape)
print(df.columns)
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

print('\n--------------df.dtypes---------------------------\n', df.dtypes)
print("\n--------------df.describe())----------------------\n", df.describe())
print("\n", df[['name_of_product_service', 'unit_cost', 'margin_%']])
print("\n---------------------must_money-----------\n", df.must_money)


