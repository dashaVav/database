import os
import random
import os.path


class Database:
    def __init__(self, folder):
        self.student_id = 1
        # os.mkdir(folder)
        # f = open(folder + '\\' + 'k', 'a+')
        if not os.path.exists(folder):
            os.mkdir(folder)

    # past id from students.txt
    def update(self):
        if not os.path.exists('students.txt'):
            return 0
        with open('students.txt') as f:
            s = f.readlines()
        if len(s) == 0:
            return 0
        self.student_id = int(s[len(s) - 1].split(' ', 1)[0]) + 1

    # add new id_students in testing_table
    def add_testing_table(self):
        file = open('testing_table.txt', 'a+')
        file.write(str(self.student_id - 1) + ' ' + str(random.randint(1, 99)) + '\n')
        file.close()

    def add(self, name, surname, patronymic):
        with open('students.txt', 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                return 0
        file = open('students.txt', 'a+')
        file.write(' '.join([str(self.student_id), name, surname, patronymic]) + '\n')
        self.student_id += 1
        file.close()
        self.add_testing_table()

    # add new students from names.txt
    def add_from(self):
        if os.path.exists('students.txt'):
            return 0

        file_1 = open('students.txt', "a+")
        file_1.close()
        file = open("names.txt", encoding="utf8")
        while 1:
            s = file.readline()
            if not s:
                break
            s = s.replace('\n', '')
            first_name, second_name, patronymic = s.split(' ')
            self.add(first_name, second_name, patronymic)
        file.close()

    # print student's name by id
    def print_id(self, student_id):
        file = open('students.txt', 'r')
        while 1:
            s = file.readline()
            if not s: break
            if int(s.split(' ', 1)[0]) == student_id:
                print(s)
                break
        file.close()

    def remove_testing_table(self, student_id):
        file = open('testing_table.txt', 'r+')
        file_new = open('new_testing_table.txt', 'a+')
        while 1:
            s = file.readline()
            if not s:
                print('not found')
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
        file_new.close()
        file.close()

        os.remove('testing_table.txt')
        os.rename('new_testing_table.txt', 'testing_table.txt')

    def remove(self, student_id):
        file = open('students.txt', 'r+')
        file_new = open('new_students.txt', 'a+')
        while 1:
            s = file.readline()
            if not s:
                print('not found')
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
        file_new.close()
        file.close()

        os.remove('students.txt')
        os.rename('new_students.txt', 'students.txt')
        self.remove_testing_table(student_id)

    # 99 id - 9 var
    def variants(self):
        if os.path.exists('variants.txt'):
            return 0
        file = open('variants.txt', 'a+')
        var = [i//10 for i in range(100)]
        random.shuffle(var)
        for i in range(1, 100):
            file.write(str(i) + ' ' + 'var' + str(var[i]) + '\n')
        file.close()

    def edit(self, student_id, name, surname, patronymic):
        f = 0
        with open('students.txt', 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if student_id == id_st: f = 1
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                print('no')
                return 0
        if f:
            file = open('students.txt', 'r+')
            file_new = open('new_students.txt', 'a+')
            while 1:
                s = file.readline()
                if not s:
                    print('not found')
                    break
                if int(s.split(' ', 1)[0]) != student_id:
                    file_new.write(s)
                else:
                    file_new.write(' '.join([str(s.split(' ', 1)[0]), name, surname, patronymic]) + '\n')

            file_new.close()
            file.close()

            os.remove('students.txt')
            os.rename('new_students.txt', 'students.txt')

    def print_table(self):
        file_testing_table = open('testing_table.txt', 'r')
        while 1:
            s = file_testing_table.readline()
            # print(s)
            if not s:
                break
            s = s.replace('\n','')
            student_id, student_var = s.split(' ')
            file = open('students.txt', 'r')
            while 1:
                str = file.readline()
                str = str.replace('\n', '')
                name = str.split(' ', 1)
                # print(name)
                if student_id == name[0]:
                    break
            file.close()
            file = open('variants.txt', 'r')
            while 1:
                str_ = file.readline()
                str_ = str_.replace('\n', '')
                var = str_.split(' ')
                # print(student_var, var[0])
                if student_var == var[0]:
                    break
            file.close()

            print(*(name[1:3]), var[1])

        file_testing_table.close()


base = Database('hse_students')
base.update()
base.add_from()

base.add_from()
base.variants()
base.print_id(5)
base.add('kk', 'll', 'll')
base.add('kk', 'll', 'll1')
# base.testing_table()
base.remove(8)
base.edit(12, 'Борисоjjjва', 'Елизаветnа',  'Юрьевнkkа')
base.print_table()
# base.testing_table()
# var = [i//10 for i in range(100)]
# print(len(var))
# base.remove('students.txt', 1)
# base.remove('students.txt', 77)
# решить как айди таскать
#
# file = open("names.txt", encoding="utf8")
# s = file.readline()
# s = s.replace("\n", "")
# first_name, second_name, patronymic = s.split(" ")
# print(s)
# print(first_name + "+" + second_name + "=" + patronymic+"=")
# s = file.readline()
# print(s)
#
# file_in = open("data.txt", 'w+')
# file_in.write("1"+" "+first_name + "+" + second_name + "=" + patronymic+"=")

