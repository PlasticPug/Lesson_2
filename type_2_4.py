# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например
# «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7
# копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
# остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]

for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп' )



prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
print(id(prices))
prices.sort()
print(id(prices))
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')



prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]

for price in sorted(prices)[::-1][:6]:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп' )


print([f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][:5]])