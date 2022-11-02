per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = (int(100000))

bank_1 = ("ТКБ")
per_cent_1 = (float(5.6))
profit_1 =(per_cent_1/100*money)

deposit_1 =(round(profit_1))


bank_2 = ("СКБ")
per_cent_2 = (float(5.9))
profit_2 =(per_cent_2/100*money)

deposit_2 =(round(profit_2))


bank_3 = ("ВТБ")
per_cent_3 = (float(4.28))
profit_3 =(per_cent_3/100*money)

deposit_3 =(round(profit_3))


bank_4 = ("СБЕР")
per_cent_4 = (float(4.0))
profit_4 =(per_cent_4/100*money)

deposit_4 =(round(profit_4))


benefit = [deposit_1, deposit_2, deposit_3, deposit_4]

max_deposit = max(benefit)

print('Максимальная сумма, которую вы можете заработать — ' + str(max_deposit))