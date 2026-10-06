order_name = input('Введите название заказа: ')
customer_name = input('Введите имя заказчика: ')

item1_name = input('Название первой позиции: ')
item1_qty = int(input('Количество первой позиции: '))
item1_price = float(input('Цена единицы первой позиции (руб.): '))

item2_name = input('Название второй позиции: ')
item2_qty = int(input('Количество второй позиции: '))
item2_price = float(input('Цена единицы второй позиции (руб.): '))

delivery_cost = float(input('Стоимость доставки (руб.): '))
paid_amount = float(input('Внесённая сумма (руб.): '))

cost1 = item1_qty * item1_price
cost2 = item2_qty * item2_price
total_items_cost = cost1 + cost2
total_with_delivery = total_items_cost + delivery_cost
total_qty = item1_qty + item2_qty
change = paid_amount - total_with_delivery

print('\n' + '=' * 30)
print(f'Заказ: {order_name}')
print(f'Заказчик: {customer_name}')
print('=' * 30)
print(f'{item1_name} | {item1_qty} | {item1_price:.2f} | {cost1:.2f}')
print(f'{item2_name} | {item2_qty} | {item2_price:.2f} | {cost2:.2f}')
print('=' * 30)
print(f'Стоимость товаров: {total_items_cost:.2f} руб.')
print(f'Стоимость доставки: {delivery_cost:.2f} руб.')
print(f'Общая сумма: {total_with_delivery:.2f} руб.')
print(f'Общее количество: {total_qty}')
print(f'Сдача: {change:.2f} руб.')
print('=' * 30)
