import os


class Database:
    def __init__(self):
        self.student_id = 1

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

s1 = Database()

s1.add('d', 'g', 'f')
s1.add('d-', 'g', 'f')
s1.add('d=', 'g', 'f')
s1.add('d', 'g', 'f')

s1.add_from("names.txt")
s1.add_from("names.txt")
s1.add('d', 'g', 'f=')
s1.print_id(5)
# s1.remove('students.txt', 1)
# s1.remove('students.txt', 77)
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
