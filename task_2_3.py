# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников: ['инженер-конструктор Игорь',
# 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']. Известно, что имя сотрудника всегда
# в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'


info = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for idx in info:
    word_idx = idx.split()
    name = word_idx[-1]
    print(f'Привет, {name.title()}!')

