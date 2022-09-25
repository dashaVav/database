import os
import random
import os.path


class Database:
    def __init__(self):
        self.student_id = 1

    def update(self):
        with open('students.txt') as f:
            s = f.readlines()
        if len(s) == 0:
            return 0
        i, a, b, c = s[len(s) - 1].split(' ')
        self.student_id = int(i) + 1

    def add(self, name, surname, patronymic):
        with open('students.txt', 'r') as f:
            s = f.readlines()
        z = 1
        for i in s:
            if s == []: break
            i = i.replace('\n', '')
            id_, name_, surname_, patronymic_ = i.split(' ')
            if name == name_ and surname_ == surname and patronymic_ == patronymic:
                z = 0
        if z:
            file = open('students.txt', 'a+')
            file.write(str(self.student_id) + ' ' + name + ' ' + surname + ' ' + patronymic + '\n')
            self.student_id += 1
            file.close()
            file = open('testing_table.txt', 'a+')
            file.write(str(self.student_id - 1) + ' ' + str(random.randint(1, 99)) + '\n')
            file.close()


    def remove(self, file_name, student_id):
        file = open(file_name, 'r+')
        file_new = open('new' + file_name, 'a+')
        while 1:
            s = file.readline()
            if not s:
                print('not found')
                break
            s = s.replace('\n', '')
            id_stud, first_name, second_name, patronymic = s.split(' ')
            if int(id_stud) != student_id:
                file_new.write(s + '\n')

        file_new.close()
        file.close()
        os.remove(file_name)
        os.rename('new' + file_name, file_name)

    def add_from(self, file_name):
        file = open(file_name, encoding="utf8")
        while 1:
            s = file.readline()
            if not s:
                break
            s = s.replace('\n', '')
            first_name, second_name, patronymic = s.split(' ')
            self.add(first_name, second_name, patronymic)
        file.close()

    def print_id(self, student_id):
        file = open('students.txt', 'r+')
        while 1:
            s = file.readline()
            if not s:
                break
            id_st, first_name, second_name, patronymic = s.split(' ')
            if int(id_st) == student_id:
                print(s)
                break
        file.close()

    #99 id - 9 var
    def variants(self):
        if os.path.exists('variants.txt'):
            return 0
        file = open('variants.txt', 'a+')
        var = [i//10 for i in range(100)]
        random.shuffle(var)
        for i in range(1, 100):
            file.write(str(i) + ' ' + 'var' + str(var[i]) + '\n')
        file.close()

    def testing_table(self):
        if not os.path.exists('testing_table.txt'):
            file = open('testing_table.txt', 'a+')
            file_students = open('students.txt', 'r')
            while 1:
                s = file_students.readline()
                if not s:
                    break
                id_st, a, b, c = s.split(' ')
                file.write(str(id_st) + ' ' + str(random.randint(1, 99)) + '\n')
            file_students.close()
            file.close()


    # def edit(self, student_id):
    #     # file = open('students.txt', 'r+')
    #     # while 1:
    #     #     s = file.readline()
    #     #     if not s:
    #     #         break
    #     #     id_st, first_name, second_name, patronymic = s.split(' ')
    #     #     if int(id_st) == student_id:
    #     #         print(s)
    #     #         break
    #     # file.close()
    #
    #     file = open('students.txt', 'r+')
    #     file_new = open('new' + 'students.txt', 'a+')
    #     while 1:
    #         s = file.readline()
    #         if not s:
    #             print('not found')
    #             break
    #         s = s.replace('\n', '')
    #         id_stud, first_name, second_name, patronymic = s.split(' ')
    #
    #         if int(id_stud) != student_id:
    #             file_new.write(s + '\n')
    #
    #     file_new.close()
    #     file.close()
    #     os.remove('students.txt')
    #     os.rename('new' + 'students.txt', 'students.txt')


base = Database()
base.update()
base.add_from("names.txt")
base.add_from("names.txt")
base.variants()
base.print_id(5)
base.add('kk', 'll', 'll')
# base.testing_table()
base.remove('students.txt', 1)
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
#
#
# def testing_table(self):
#     if os.path.exists('testing_table.txt'):
#         file = open('testing_table.txt', 'r')
#         file_students = open('students.txt', 'r')
#         new_file_students = open('new_testing_table.txt', 'a+')
#
#         while 1:
#             s_file = file.readline()
#             s_file_students = file_students.readline()
#
#             print(s_file, s_file_students)
#
#             if (not s_file) and s_file_students:
#                 while 1:
#                     s_file_students = file_students.readline()
#                     if not s_file_students:
#                         break
#                     id_file_students, a, b, c = s_file_students.split(' ')
#                     new_file_students.write(str(id_file_students) + ' ' + str(random.randint(1, 99)) + '\n')
#                 break
#             if not s_file and not s_file_students:
#                 break
#             if s_file_students == '':
#                 break
#             id_file, a = s_file.split(' ')
#             id_file_students, a, b, c = s_file_students.split(' ')
#             if id_file_students == id_file:
#                 new_file_students.write(s_file)
#                 print(s_file)
#             elif id_file_students < id_file:
#                 new_file_students.write(str(id_file_students) + ' ' + str(random.randint(1, 99)) + '\n')
#                 print(str(id_file_students) + ' ' + str(random.randint(1, 99)) + '\n')
#                 s_file_students = file_students.readline()
#
#         file.close()
#         file_students.close()
#         new_file_students.close()
#
#         os.remove('testing_table.txt')
#         os.rename('new_testing_table.txt', 'testing_table.txt')
#     else:
#         file = open('testing_table.txt', 'a+')
#         file_students = open('students.txt', 'r')
#         while 1:
#             s = file_students.readline()
#             if not s:
#                 break
#             id_st, a, b, c = s.split(' ')
#             file.write(str(id_st) + ' ' + str(random.randint(1, 99)) + '\n')
#
#     file_students.close()
#     file.close()
