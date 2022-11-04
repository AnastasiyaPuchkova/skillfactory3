tickets = int(input('Введите количество билетов, которое хотите приобрести:\n'))
summ = 0
for i in range(tickets):
    age = int(input('Введите возраст посетителя\n'))
    if age < 18:
        summ+=0
        print('Промежуточная сумма', summ)
    elif 18<= age <25:
        summ+= 990
        print('Промежуточная сумма', summ)
    elif age >=25:
        summ+= 1390
        print('Промежуточная сумма', summ)
print('Итого билетов на сумму:', summ)
if tickets>=3:
    summ = (summ*90)/100
    print('!!!Вы получаете скидку 10% при покупке от 3х билетов!!!')
    print('Итого к оплате со скидкой: %i' % summ)

