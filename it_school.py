import mysql

import mysql.connector
from configs import Configs
from const import Const
from dbHandler import dbHandler
from Student import Student
from Teacher import Teacher
from Directors import Director
from prettytable import PrettyTable
from StudentPoints import StudentPoints

handler = dbHandler()



def register_user(account_type):

    first_name = input("Введите имя >>> ")
    last_name = input("Введите фамилию >>> ")
    user_name = input("Введите логин >>> ")
    password = input("Введите пароль >>> ")

    if account_type == "student":

        student = Student(first_name, last_name, user_name, password)
        handler.insert_student(student)

    elif account_type == "teacher":

        subject = input("Введите ваш предмет >>> ")
        teacher = Teacher(first_name, last_name, user_name, password, subject)
        handler.insert_teacher(teacher)

    elif account_type == "director":

        director = Director(first_name, last_name, user_name, password)
        handler.insert_director(director)


def login_user(account_type):

    user_name = input("Введите логин >>> ")
    password = input("Введите пароль >>> ")

    if account_type == "student":

        student = Student(None, None, user_name, password)
        result = handler.select_student(student)
        counter = 0
        for i in result:
            counter += 1
        if counter >= 1:
            print(student.getUserName())

            print("Успешный вход. Добро пожаловать.")
            main_fun("student", student)
        else:
            print("Неверный логин или пароль.")

    elif account_type == "teacher":

        teacher = Teacher(None, None, user_name, password, None)
        result = handler.select_teacher(teacher)
        counter = 0
        for i in result:
            counter += 1
        if counter >= 1:
            print("Успешный вход. Добро пожаловать.")
            main_fun("teacher", None, teacher)
        else:
            print("Неверный логин или пароль.")

    elif account_type == "director":

        director = Director(None, None, user_name, password)
        result = handler.select_director(director)
        counter = 0
        for i in result:
            counter += 1
        if counter >= 1:
            print("Успешный вход. Добро пожаловать.")
            main_fun("director", None, director)
        else:
            print("Неверный логин или пароль.")

def show_student_menu():
    print("""
    
     1.	Показать список предметов (Показывает список предметов на котором учится студент)
     2.	Показать список оценок (Показывает предмет и оценки по тем или иным предметам)
     3.	Показать список заданий (Показывает список домашних работ по тем или иным предметам)
     4.	Показать список экзаменов (Показывает список экзаменов по тем или иным предметам с датами)
     5.	Показать список зачетов (Показывает список зачетов по тем или иным предметам с датами)
     6.	Показать мой максимальный бал (Показывает сумму максимального бала за тот или иной предмет)
     7.	Показать мой минимальный бал. (Показывает сумму минимального бала за тот или иной предмет)
     8.	Выход (Выходит из программы)
     
     """)

def show_teacher_menu():
    print("""
    
    1. Показать список предметов (Показывает список предметов, которую ведет учитель)
    2. Показать список оценок (Показывает список студентов - предмет на который они были записаны, показывает оценки каждого из студентов)
        ◦ Напишите название предмета: >>>(После того как здесь будет написана название предмета выведутся оценки для всех студентов, которые зарегистрированы на тот или иной предмет)
    3. Показать количество студентов (Показывает количество студентов для каждого предмета)
    4. Показать список экзаменов (Показывает список экзаменов по, которым ведет этот студент)
    5. Показать список зачетов (Показывает список зачетов по, которым ведет этот студент)
    6. Показать максимальный бал (Показывает сумму максимального бала того или иного студента за определенный предмет)
        ◦ Наберите название предмета для, которого вы бы хотели посмотреть бал: >>>(После того как здесь будет написана название предмета выведется максимальная оценка и имя студента с максимальной оценкой)
    7. Показать мой минимальный бал. (Показывает сумму минимального бала того или иного студента за определенный предмет)
            ▪ Наберите название предмета для, которого вы бы хотели посмотреть бал: >>>(После того как здесь будет написана название предмета выведется минимальная оценка и имя студента с максимальной оценкой)

    8. Выход (Выходит из программы)
    
    """)

def show_director_menu():
    print('''
    1. Показать список предметов (Показывает список предметов, который есть в образовательном центре)
    2. Показать количество студентов (Показывает количество студентов для каждого предмета)
    3. Показать список учителей (Показывает количество учителей и предмет, который они ведут)
    4. Добавить учителя
        ◦ Введите имя учителя, которого вы хотите добавить: (Вводится имя учителя для добавления в запись)
        ◦ Введите предмет, который ведет этот учитель: (Вводится предмет, который ведет этот новый преподаватель)
    5. Удалить учителя
        ◦ Введите имя учителя, которого вы хотите удалить из списка учителей: (Вводится имя учителя, которого необходимо удалить из списка учителей)
    6. Добавить студента
        ◦ Введите имя студента, которого вы хотите добавить: (Вводится имя студента для добавления в запись)
    7. Удалить студента
        ◦ Введите имя студента, которого вы хотите удалить из списка студентов: (Вводится имя студента, которого необходимо удалить из списка студентов)
        ◦ 
    8. Выход (Выходит из программы)
''')


def main_fun(account_type, student=None, teacher=None, director=None):

    if account_type == "student":

        show_student_menu()
        operationStudent = int(input("Выберите из списка: "))

        while operationStudent != 8:
            if operationStudent == 1:
                subjects_list = handler.select_subjects()
                for subject in subjects_list:
                    print(str(subject[0]) + ") " + str(subject[1]))
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))

            elif operationStudent == 2:
                grades_list = handler.select_grade(student)
                table = PrettyTable(["Math", "Programming Langs", "Human & computer", "German", "English", "Algorithms"])
                table.add_row([grades_list[0][5],
                               grades_list[0][6],
                               grades_list[0][7],
                               grades_list[0][8],
                               grades_list[0][9],
                               grades_list[0][10]])
                print(table)
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))
            elif operationStudent == 3:
                hw_list = handler.select_hw()
                table = PrettyTable(["Math", "Programming Langs", "Human & computer", "German", "English", "Algorithms"])
                table.add_row([hw_list[0][1],
                              hw_list[0][2],
                              hw_list[0][3],
                              hw_list[0][4],
                              hw_list[0][5],
                              hw_list[0][6]])
                print(table)
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))

            elif operationStudent == 4:
                exam_list = handler.select_exams(student)
                table = PrettyTable(["Math", "Programming Langs", "Human & computer", "German", "English", "Algorithms"])
                table.add_row([exam_list[0][11],
                               exam_list[0][12],
                               exam_list[0][13],
                               exam_list[0][14],
                               exam_list[0][15],
                               exam_list[0][16]])
                print(table)
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))

            elif operationStudent == 5:
                credit_list = handler.select_credits(student)
                table = PrettyTable(["Math", "Programming Langs", "Human & computer", "German", "English", "Algorithms"])
                table.add_row([credit_list[0][17],
                               credit_list[0][18],
                               credit_list[0][19],
                               credit_list[0][20],
                               credit_list[0][21],
                               credit_list[0][22]])
                print(table)
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))

            elif operationStudent == 6:

                subject_min = int(input("Math <- 1\nProgramming Langs <- 2\nHuman & computer <- 3"
                                    "\nGerman <- 4\nEnglish <- 5\nAlgorithms <- 6"
                                    "\nВыберите из списка: "))

                if subject_min == 1:
                    math_min = handler.select_max_math(StudentPoints(student.getUserName()))

                    print(math_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 2:
                    pl_min = handler.select_max_pl(StudentPoints(student.getUserName()))

                    print(pl_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))

                elif subject_min == 3:
                    hci_min = handler.select_max_hci(StudentPoints(student.getUserName()))

                    print(hci_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 4:
                    math_min = handler.select_max_german(StudentPoints(student.getUserName()))

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 5:
                    math_min = handler.select_max_english(StudentPoints(student.getUserName()))

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 6:
                    math_min = handler.select_max_algorithms(StudentPoints(student.getUserName()))
                    # table = PrettyTable(["Math", "Programming Langs"])
                    # table.add_row([math_min[0][1],
                    #            math_min[0][2]])
                    # print(table)

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))


            elif operationStudent == 7:

                subject_min = int(input("Math <- 1\nProgramming Langs <- 2\nHuman & computer <- 3"
                                    "\nGerman <- 4\nEnglish <- 5\nAlgorithms <- 6"
                                    "\nВыберите из списка: "))
                if subject_min == 1:
                    math_min = handler.select_min_math(StudentPoints(student.getUserName()))

                    print(math_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 2:
                    pl_min = handler.select_min_pl(StudentPoints(student.getUserName()))

                    print(pl_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))

                elif subject_min == 3:
                    hci_min = handler.select_min_hci(StudentPoints(student.getUserName()))

                    print(hci_min)

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 4:
                    math_min = handler.select_min_german(StudentPoints(student.getUserName()))

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 5:
                    math_min = handler.select_min_english(StudentPoints(student.getUserName()))

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))
                elif subject_min == 6:
                    math_min = handler.select_min_algorithms(StudentPoints(student.getUserName()))

                    print(str(math_min[0]))

                    show_student_menu()
                    operationStudent = int(input("Выберите из списка: "))


            elif operationStudent == 8:
                print(
                "Выберите действие:\n"
                "1 - Регистрация\n"
                "2 - Вход\n"
                "3 = Выход из программы"
                )
                operation = input("Ввод >>> ")

                if operation == "1":
                    acc_type = input("Введите тип аккаунта >>> ")
                    register_user(acc_type)
                elif operation == "2":
                    acc_type = input("Введите тип аккаунта >>> ")
                    login_user(acc_type)

                elif operation == "3":
                    break

            else:
                print("Error! Вы ввели неправильные данные.\nПовторите попытку...")
                show_student_menu()
                operationStudent = int(input("Выберите из списка: "))


                break



    elif account_type == "teacher":

        show_teacher_menu()

        operationTeacher = int(input("Выберите из списка: "))

        while operationTeacher != 8:

            if operationTeacher == 1:

                subject = handler.select_subject(teacher)
                table = PrettyTable(["subject"])
                table.add_row([subject[0][5]])

                print(table)



                show_teacher_menu()

                operationTeacher = int(input("Выберите из списка: "))

            elif operationTeacher == 2:
                pass

            elif operationTeacher == 3:

                count_of_student = handler.select_subject_count_of_students()

                for i in count_of_student:
                    print(str(i[0]) + ") "+ str(i[1]) +" "+ str(i[2]))

                show_teacher_menu()

                operationTeacher = int(input("Выберите из списка: "))

            elif operationTeacher == 4:

                exam = handler.select_exam_teacher(teacher)
                table = PrettyTable(["Subject", "Exams"])
                table.add_row([exam[0][5],
                               exam[0][6]])
                print(table)
                show_teacher_menu()

                operationTeacher = int(input("Выберите из списка: "))

            elif operationTeacher == 5:

                credit = handler.select_exam_teacher(teacher)
                table = PrettyTable(["Subject", "Credits"])
                table.add_row([credit[0][5],
                               credit[0][7]])
                print(table)
                show_teacher_menu()

                operationTeacher = int(input("Выберите из списка: "))

            elif operationTeacher == 6:
                subject = int(input("Math <- 1\nProgramming Langs <- 2\nHuman & computer <- 3"
                                    "\nGerman <- 4\nEnglish <- 5\nAlgorithms <- 6"
                                    "\nВыберите из списка: "))

                if subject == 1:
                    math_max = handler.select_max_math_points()

                    print(math_max)

                    show_teacher_menu()

                    operationTeacher = int(input("Выберите из списка: "))
                elif subject == 2:
                    pl_max = handler.select_max_programming_langueges_points()

                    print(pl_max)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 3:
                    hci = handler.select_max_human_computer_interaction_points()

                    print(hci)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 4:
                    german = handler.select_max_german_points()

                    print(german)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 5:
                    english = handler.select_max_english_points()

                    print(english)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 6:
                    al = handler.select_max_algorithms_and_data_structure_points()

                    print(al)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

            elif operationTeacher == 7:

                subject = int(input("Math <- 1\nProgramming Langs <- 2\nHuman & computer <- 3"
                                    "\nGerman <- 4\nEnglish <- 5\nAlgorithms <- 6"
                                    "\nВыберите из списка: "))

                if subject == 1:
                    math_max = handler.select_min_math_points()

                    print(math_max)

                    show_teacher_menu()

                    operationTeacher = int(input("Выберите из списка: "))
                elif subject == 2:
                    pl_max = handler.select_min_programming_langueges_points()

                    print(pl_max)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 3:
                    hci = handler.select_min_human_computer_interaction_points()

                    print(hci)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 4:
                    german = handler.select_min_german_points()

                    print(german)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 5:
                    english = handler.select_min_english_points()

                    print(english)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))

                elif subject == 6:
                    al = handler.select_min_algorithms_and_data_structure_points()

                    print(al)

                    show_teacher_menu()
                    operationTeacher = int(input("Выберите из списка: "))


    elif account_type == "director":
        print("213123123515ef")
        show_director_menu()
        operationDirector = int(input("Выберите из списка: "))

        while operationDirector != 8:

            if operationDirector == 1:
                subjects_list = handler.select_subjects()
                for subject in subjects_list:
                    print(str(subject[0]) + ") " + str(subject[1]))

                show_director_menu()
                operationDirector = int(input("Выберите из списка: "))
            elif operationDirector == 2:

                count_of_student = handler.select_subject_count_of_students()

                for subject in count_of_student:
                    print(str(subject[0]) + ") "+ str(subject[1]) +" "+ str(subject[2]))

                show_director_menu()
                operationDirector = int(input("Выберите из списка: "))

            elif operationDirector == 3:

                teachers = handler.select_teachers()
                print(teachers)

                table = PrettyTable(["Name", "Subject"])

                table.add_row([teachers[0][1], teachers[0][5]])
                table.add_row([teachers[1][1], teachers[1][5]])
                table.add_row([teachers[2][1], teachers[2][5]])

                print(table)
                print(teachers)

                show_director_menu()
                operationDirector = int(input("Выберите из списка: "))

            elif operationDirector == 4:

                first_name = input("Введите имя >>> ")
                last_name = input("Введите фамилию >>> ")
                user_name = input("Введите логин >>> ")
                password = input("Введите пароль >>> ")

                subject = input("Введите ваш предмет >>> ")
                teacher = Teacher(first_name, last_name, user_name, password, subject)
                handler.insert_teacher(teacher)

                show_director_menu()
                operationDirector = int(input("Выберите из списка: "))
            elif operationDirector == 5:
                    mycursor = mysql.connector.connect(
                        host=Configs.dbHost,
                        user=Configs.dbUser,
                        password=Configs.dbPassword,
                        database=Configs.dbname
                    ).cursor()

                    user_name = input("Введите юзернейм учителя: ")
                    sql = "DELETE FROM " + Const.TEACHERS_TABLE + " WHERE " + Const.TEACHER_USER_NAME == user_name

                    mycursor.execute(sql)
                    mysql.connector.connect(
                        host=Configs.dbHost,
                        user=Configs.dbUser,
                        password=Configs.dbPassword,
                        database=Configs.dbname
                    ).commit()


                    show_director_menu()
                    operationDirector = int(input("Выберите из списка: "))

            elif operationDirector == 6:

                first_name = input("Введите имя >>> ")
                last_name = input("Введите фамилию >>> ")
                user_name = input("Введите логин >>> ")
                password = input("Введите пароль >>> ")

                student = Student(first_name, last_name, user_name, password)
                handler.insert_student(student)

                show_director_menu()
                operationDirector = int(input("Выберите из списка: "))











if __name__ == "__main__":

    while True:
        try:
            print(
                "Выберите действие:\n"
                "1 - Регистрация\n"
                "2 - Вход\n"
                "3 = Выход из программы"
            )
            operation = input("Ввод >>> ")

            if operation == "1":
                acc_type = input("Введите тип аккаунта >>> ")
                register_user(acc_type)
            elif operation == "2":
                acc_type = input("Введите тип аккаунта >>> ")
                login_user(acc_type)

            elif operation == "3":
                break
        except:
            print("Error! Вы ввели неправильные данные.\nПовторите попытку...")
            # q =__name__ == "__main__"


