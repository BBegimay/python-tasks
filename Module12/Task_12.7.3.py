
per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}

money = int(input("How much money do you want to put?"))
percents = list(per_cent.values())
deposit = []
maximum = 0

for percent in percents:
    earn = money * percent / 100
    deposit.append(earn)

    if earn > maximum:
        maximum = earn

print(deposit)
print("The maximum amount that you can earn is:", maximum)
