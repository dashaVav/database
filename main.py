from base import Database


def print_rules(key):
    if key == 0:
        rules = 'введите нужную цифру:\n' \
                '1 - создание новой базы данных\n'\
                '2 - открыть уже существующую базу данных\n'\
                '3 - завершить программу\n'
    else:
        rules = 'введите нужную цифру:\n' \
                '1 - добавить человека в базу данных\n' \
                '2 - вывести id человека с указанным именем\n' \
                '3 - вывести имя человека с указанным id\n' \
                '4 - удалить человека из базы данных по id\n' \
                '5 - отредактировать фио человека с id\n' \
                '6 - вывести базу данных\n' \
                '7 - сохранить текущую версию\n' \
                '8 - вернуться назад\n' \
                '0 - закрыть базу данных\n'
    print(rules)


while 1:
    print_rules(0)
    n = int(input())
    if n == 1 or n == 2:
        s = input('введите название базы данных: ')
        base = Database(s)
        while 1:
            print_rules(1)
            n = int(input())
            if n == 1:
                surname = input('введите фамилию: ')
                name = input('введите имя: ')
                patronymic = input('введите отчество: ')
                base.add(surname, name, patronymic)
            elif n == 2:
                surname = input('введите фамилию: ')
                name = input('введите имя: ')
                patronymic = input('введите отчество: ')
                base.print_id_via_name(surname, name, patronymic)
            elif n == 3:
                id_ = int(input('введите id: '))
                base.print_id(id_)
            elif n == 4:
                id_ = int(input('введите id: '))
                base.remove(id_)
            elif n == 5:
                id_ = int(input('введите id: '))
                print('введите измененные данные')
                surname = input('введите фамилию: ')
                name = input('введите имя: ')
                patronymic = input('введите отчество: ')
                base.edit(id_, surname, name, patronymic)
            elif n == 6:
                base.print_table()
            elif n == 7:
                base.save()
            elif n == 8:
                base.back_up()
            elif n == 0:
                break
            else:
                print('неизвестная команда')
    elif n == 3:
        break
    else:
        print('неизвестная команда')
