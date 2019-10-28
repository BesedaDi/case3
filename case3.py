a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('Срок размещения капитала (лет):', a)
print('Начальный капитал ($):', b)
print('Процентная ставка (%/мес.):', c)
print('Инвестиционные вливания ($/мес.):', d)
s = 0
# основа инвистицый investment
# сумма процентов месяц interest
# капитал capital
year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i=1
inv = b
interest = b*c/100
capital = b*c/100+b
g=0
for g in range(a):
    g=g+1
    print('')
    print('')
    print(g, 'год')
    print('--------------------------------------------')
    print('|        |  основа   | сумма % |           |')
    print('|  месяц |инвестиций |за месяц |  капитал  |')
    for i in range(1, 13):
        print('|', format(i, '4.0f'), '  |', format(inv, '0.2f'), '|', format(interest, '4.2f'), '|',
              format(capital, '0.2f'), '|', )
        inv = capital + d
        interest = inv * c / 100
        capital = inv * c / 100 + inv
    print('--------------------------------------------')
