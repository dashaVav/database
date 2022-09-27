import os
import random
import os.path


class Database:
    def __init__(self, folder):
        self.student_id = 1
        if not os.path.exists(folder):
            os.mkdir(folder)
        self.student_txt = folder + '\\' + 'students.txt'
        self.variants_txt = folder + '\\' + 'variants.txt'
        self.testing_table_txt = folder + '\\' + 'testing_table.txt'
        self.copy = folder + '\\' + 'copy.txt'
        self.update()
        self.add_from()
        self.variants()

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
        else:
            print('cannot be added')

    # add new students from names.txt
    # auto when creating
    def add_from(self):
        if not os.path.exists('names.txt'): return 0
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

    # print student's name by id
    def print_id(self, student_id):
        file = open(self.student_txt, 'r')
        while 1:
            s = file.readline()
            if not s: break
            if int(s.split(' ', 1)[0]) == student_id:
                print(s)
                break
        file.close()

    def print_if_via_name(self, name, surname, patronymic):
        with open(self.student_txt, 'r') as f:
            s = f.readlines()
        for i in s:
            i = i.replace('\n', '')
            id_st, name_, surname_, patronymic_ = i.split(' ')
            if name_ == name and surname_ == surname and patronymic_ == patronymic:
                print(id_st)
                return 0
        print('not found')

    def remove_testing_table(self, student_id):
        file = open(self.testing_table_txt, 'r+')
        file_new = open(self.copy, 'a+')
        while 1:
            s = file.readline()
            if not s:
                print('not found')
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
        file_new.close()
        file.close()
        os.remove(self.testing_table_txt)
        os.rename(self.copy, self.testing_table_txt)

    def remove(self, student_id):
        file = open(self.student_txt, 'r+')
        file_new = open(self.copy, 'a+')
        while 1:
            s = file.readline()
            if not s:
                print('not found')
                break
            if int(s.split(' ', 1)[0]) != student_id:
                file_new.write(s)
        file_new.close()
        file.close()
        os.remove(self.student_txt)
        os.rename(self.copy, self.student_txt)
        self.remove_testing_table(student_id)

    # 99 id - 9 var
    def variants(self):
        if os.path.exists(self.variants_txt):
            return 0
        file = open(self.variants_txt, 'a+')
        var = [i//10 for i in range(100)]
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
                print('cannot edit')
                return 0
        if f == 0:
            print('not found')
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


base = Database('hse_students_math')
base.print_if_via_name('Вавилова', 'Дарья', 'Григорьевна')



base.variants()
# base.print_id(5)
# base.add('kk', 'll', 'll')
base.add('kk8989', 'll', 'll1')
# base.testing_table()
# base.remove(8)
# base.edit(12, 'Борисоjjjва', 'Елизаветnа',  'Юрьевнkkа')
base.print_table()
# base.print_id(89)


base = Database('hse_students_lit')