Money = float(input ('Введите сумму вклада:'))
Per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

Per1 = Per_cent.get('ТКБ')
Deposit1 = Money/100*Per_cent['ТКБ']

Per2=Per_cent.get('СКБ')
Deposit2 = Money/100*Per_cent['СКБ']

Per3=Per_cent.get('ВТБ')
Deposit3 = Money/100*Per_cent['ВТБ']

Per4=Per_cent.get('СБЕР')
Deposit4 = Money/100*Per_cent['СБЕР']

Deposit = {"ТКБ":Deposit1,"СКБ":Deposit2, "ВТБ":Deposit3, "СБЕР":Deposit4}
print (Deposit)

print ("В ТБК при ставке", Per1 ,"% накопленные средства за год:", Deposit1,"рублей")
print ("В СКБ при ставке", Per2 ,"% накопленные средства за год:", Deposit2,"рублей")
print ("В ВТБ при ставке", Per3 ,"% накопленные средства за год:", Deposit3,"рублей")
print ("В СБЕР при ставке", Per4 ,"% накопленные средства за год:", Deposit4,"рублей")

Maximum = max(Deposit.get('ТКБ'), Deposit.get('СКБ'), Deposit.get('ВТБ'), Deposit.get('СБЕР'))
print ("Максимальная сумма, которую вы можете заработать =", Maximum,"рублей")

