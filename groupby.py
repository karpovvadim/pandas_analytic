from dataframe import df

all_money = df.money.sum()

print("\n-------------all_money------------------\n", all_money)
money_payment_status = df \
    .groupby(['name_of_product_service', 'payment_status'], as_index=False) \
    .agg({"money": "sum"}) \
    .sort_values("money", ascending=False)
print("\n--------------groupby_money------------\n", money_payment_status, "\n",
      money_payment_status.shape)
money_payment_status.to_csv("money_payment_status.csv", index=False)

money_quantity = df \
    .query("payment_status == 'Оплачено'") \
    .groupby(['name_of_product_service'], as_index=False) \
    .aggregate({"money": "sum", "quantity": "count"}) \
    .sort_values("money", ascending=False)
print("-----------money_quantity-----------------------\n", money_quantity, "\n",
      money_quantity.shape)
