# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv_data):
    return [x.split(';') for x in csv_data.split('\n')]

# Уважаемый наставник! Закомменченные принты - это не плохой код. Это я для себя оставил.
# Мне так проще было понять, что я сделал. Пусть будет. Потом поржу над собой, если вернусь к этому коду.
#print(_read(csv))


def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))

#print(_sort(_read(csv)))


def _filter(data):
    return [x for x in data if int(x[1]) > 10]

#print(_filter(_sort(_read(csv))))


if __name__ == '__main__':
     print(get_users_list())
