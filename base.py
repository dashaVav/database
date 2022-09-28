import os
import random
import os.path
from distutils.dir_util import copy_tree


class Database:
    def __init__(self, folder):
        self.copy, self.testing_table_txt, self.variants_txt, self.student_txt = None, None, None, None
        self.student_id = 1
        self.ver = folder
        self.version_txt = ''
        if not os.path.exists(folder):
            os.mkdir(folder)
        if not os.path.exists(folder + '\\' + 'version.txt'):
            f = open(folder + '\\' + 'version.txt', 'a+')
            f.write('0')
            f.close()
            os.mkdir(folder + '\\' + '0')
            self.version = 1
            os.mkdir(folder + '\\' + '1')
            self.change_version()
            self.update()
            self.add_from()
            self.variants()
        else:
            f = open(folder + '\\' + 'version.txt', 'r')
            self.version = f.readline()
            self.version = int(self.version)
            f.close()
            os.mkdir(folder + '\\' + str(self.version))
            copy_tree(folder + '\\' + str(self.version - 1), folder + '\\' + str(self.version))
            self.change_version()
            self.update()
            if not os.path.exists(folder + '\\' + str(self.version) + '\\' + 'students.txt'):
                self.add_from()
                self.variants()

    def change_version(self):
        self.student_txt = self.ver + '\\' + str(self.version) + '\\' + 'students.txt'
        self.variants_txt = self.ver + '\\' + str(self.version) + '\\' + 'variants.txt'
        self.testing_table_txt = self.ver + '\\' + str(self.version) + '\\' + 'testing_table.txt'
        self.copy = self.ver + '\\' + str(self.version) + '\\' + 'copy.txt'
        self.version_txt = self.ver + '\\' + str(self.version)

    # past id from students.txt
    def update(self):
        if not os.path.exists(self.student_txt):
            return 0
        with open(self.student_txt) as f:
            s = f.readlines()
        self.student_id = int(s[len(s) - 1].split(' ', 1)[0]) + 1

    # add  id_students in testing_table
    def add_testing_table(self):
        file = open(self.testing_table_txt, 'a+')
        file.write(str(self.student_id - 1) + ' ' + str(random.randint(1, 99)) + '\n')
        file.close()

    def duplicate(self, name, surname, patronymic):
        if not os.path.exists(self.student_txt): return 1
        with open(self.student_txt, 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                return 0
        return 1

    # no people with the same name
    def add(self, name, surname, patronymic):
        if self.duplicate(name, surname, patronymic) != 0:
            file = open(self.student_txt, 'a+')
            file.write(' '.join([str(self.student_id), name, surname, patronymic]) + '\n')
            self.student_id += 1
            file.close()
            self.add_testing_table()
            print('человек добавлен\n')
        else:
            print('человек с таким именем уже существует!\n')

    # add new students from names.txt
    # auto when creating
    def add_from(self):
        if not os.path.exists('names.txt'):
            return 0
        if os.path.exists(self.student_txt):
            return 0
        file = open(self.student_txt, "a+")
        file.close()
        file_names = open("names.txt", encoding="utf8")
        while 1:
            s = file_names.readline()
            if not s:
                break
            s = s.replace('\n', '')
            first_name, second_name, patronymic = s.split(' ')
            self.add(first_name, second_name, patronymic)
        file_names.close()
        print('ученики из файла names.txt загружены в базу данных\n')

    # print student's name by id
    def print_id(self, student_id):
        file = open(self.student_txt, 'r')
        while 1:
            s = file.readline()
            if not s: break
            if int(s.split(' ', 1)[0]) == student_id:
                print('имя человека с id -', s, '\n')
                return 0
        file.close()
        print('нет человека с id -', student_id, '\n')

    def print_id_via_name(self, name, surname, patronymic):
        with open(self.student_txt, 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                print('id - ', id_st, '\n')
                return 0
        print('человек с таким именем не найден!\n')

    def remove_testing_table(self, student_id):
        file = open(self.testing_table_txt, 'r+')
        file_new = open(self.copy, 'a+')
        while 1:
            s = file.readline()
            if not s:
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
        file_new.close()
        file.close()
        os.remove(self.testing_table_txt)
        os.rename(self.copy, self.testing_table_txt)

    def remove(self, student_id):
        f = 0
        file = open(self.student_txt, 'r+')
        file_new = open(self.copy, 'a+')
        while 1:
            s = file.readline()
            if not s:
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
            else:
                f = 1
        file_new.close()
        file.close()
        os.remove(self.student_txt)
        os.rename(self.copy, self.student_txt)
        if f == 1: print('человек с id -', student_id, 'успешно удален\n')
        else: print('человек с id -', student_id, 'не найден\n')
        self.remove_testing_table(student_id)

    # 99 id - 9 var
    def variants(self):
        if os.path.exists(self.variants_txt):
            return 0
        file = open(self.variants_txt, 'a+')
        var = [i // 10 for i in range(100)]
        random.shuffle(var)
        for i in range(1, 100):
            file.write(str(i) + ' ' + 'var' + str(var[i]) + '\n')
        file.close()

    # edit students with id
    def edit(self, student_id, name, surname, patronymic):
        f = 0
        with open(self.student_txt, 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if student_id == id_st: f = 1
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                print('невозможно отредактировать!\n')
                return 0
        if f == 0:
            print('нет человека с id -', student_id, '!\n')
            return 0

        file = open(self.student_txt, 'r+')
        file_new = open(self.copy, 'a+')
        while 1:
            s = file.readline()
            if not s:
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
            else:
                file_new.write(' '.join([str(s.split(' ', 1)[0]), name, surname, patronymic]) + '\n')
        file_new.close()
        file.close()
        os.remove(self.student_txt)
        os.rename(self.copy, self.student_txt)
        print('фио человека изменено\n')

    def print_table(self):
        file_testing_table = open(self.testing_table_txt, 'r')
        while 1:
            s = file_testing_table.readline()
            if not s:
                break
            s = s.replace('\n', '')
            student_id, student_var = s.split(' ')

            file = open(self.student_txt, 'r')
            while 1:
                str_ = file.readline()
                str_ = str_.replace('\n', '')
                name = str_.split(' ', 1)
                if student_id == name[0]:
                    break
            file.close()

            file = open(self.variants_txt, 'r')
            while 1:
                str_ = file.readline()
                str_ = str_.replace('\n', '')
                var = str_.split(' ')
                if student_var == var[0]:
                    break
            file.close()
            print(*(name[1:3]), var[1])
        file_testing_table.close()
        print()

    # def at_exit(self):
    #     self.save()

    def save(self):
        os.remove(self.ver + '\\' + 'version.txt')
        f = open(self.ver + '\\' + 'version.txt', 'a+')
        f.write(str(self.version))
        f.close()
        self.version += 1
        os.mkdir(self.ver + '\\' + str(self.version))
        copy_tree(self.ver + '\\' + str(self.version - 1), self.ver + '\\' + str(self.version))
        self.change_version()

    def back_up(self):
        if self.version - 1 >= 0:
            os.remove(self.student_txt)
            os.remove(self.variants_txt)
            os.remove(self.testing_table_txt)
            os.rmdir(os.path.join(self.version_txt))
            self.version -= 1
            os.remove(self.ver + '\\' + 'version.txt')
            f = open(self.ver + '\\' + 'version.txt', 'a+')
            f.write(str(self.version))
            f.close()
            self.change_version()
        else:
            print('база данных очищена!')
