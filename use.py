from base import Database


def print_rules(key):
    if key == 0:
        rules = 'введите нужную цифру:\n' \
                '1 - создание новой базы данных\n'\
                '2 - открыть уже существующую базу данных\n'\
                '0 - завершить программу\n'
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


def run():
    while 1:
        print_rules(0)
        n = input()
        n = n.replace(' ', '')
        if str(n) not in '120':
            print('неизвестная команда\n')
            continue
        else:
            n = int(n)
        if n == 1 or n == 2:
            s = input('введите название базы данных: ')
            base = Database(s)
            while 1:
                print_rules(1)
                n = input()
                n = n.replace(' ', '')
                if str(n) not in '012345678':
                    print('неизвестная команда\n')
                    continue
                else:
                    n = int(n)

                if n == 1:
                    surname = input('введите фамилию: ').replace(' ', '')
                    name = (input('введите имя: ')).replace(' ', '')
                    patronymic = input('введите отчество: ').replace(' ', '')
                    if surname and name and patronymic:
                        base.add(surname, name, patronymic)
                    else:
                        print('имя введено некорректно\n')

                elif n == 2:
                    surname = input('введите фамилию: ').replace(' ', '')
                    name = input('введите имя: ').replace(' ', '')
                    patronymic = input('введите отчество: ').replace(' ', '')
                    if surname and name and patronymic:
                        base.print_id_via_name(surname, name, patronymic)
                    else:
                        print('имя введено некорректно\n')

                elif n == 3:
                    try:
                        id_ = int(input('введите id: '))
                    except:
                        print('неправильно введено id\n')
                        continue
                    base.print_id(id_)

                elif n == 4:
                    try:
                        id_ = int(input('введите id: '))
                    except:
                        print('неправильно введено id\n')
                        continue
                    base.remove(id_)

                elif n == 5:
                    try:
                        id_ = int(input('введите id: '))
                    except:
                        print('неправильно введено id\n')
                        continue
                    print('введите измененные данные')
                    surname = input('введите фамилию: ').replace(' ', '')
                    name = input('введите имя: ').replace(' ', '')
                    patronymic = input('введите отчество: ').replace(' ', '')
                    if surname and name and patronymic:
                        base.edit(id_, surname, name, patronymic)
                    else:
                        print('имя введено некорректно\n')

                elif n == 6:
                    base.print_table()

                elif n == 7:
                    base.save()

                elif n == 8:
                    base.back_up()

                elif n == 0:
                    break
                else:
                    print('неизвестная команда\n')
        elif n == 0:
            break
        else:
            print('неизвестная команда\n')
