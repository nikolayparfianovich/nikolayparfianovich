test_list = input("Введите числа через запятую")
if (len(test_list)) in range(1, 500):
    new_list = test_list.split(",")
    for i in range(0, len(new_list)):
        new_list[i] = int(new_list[i])
else:
    print("Объем заказов не может быть меньше 0 и большее 500")

days = int(input("Введите количество дней: "))
if days < 1 or days > 50000:
    print("Количество дней должно быть больше 0 и меньше 50000")

condition = int(sum(new_list) / days)
print(f"Mинимальное условие {condition}")
