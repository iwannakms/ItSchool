import mysql.connector

from configs import Configs
from const import Const
from Student import Student


class dbHandler:
    mydb = mysql.connector.connect(
        host=Configs.dbHost,
        user=Configs.dbUser,
        password=Configs.dbPassword,
        database=Configs.dbname
    )

    mycursor = mydb.cursor()

    def insert_student(self, student):
        sql = "INSERT INTO " + Const.STUDENTS_TABLE + "(" + \
              Const.STUDENT_FIRST_NAME + ", " + \
              Const.STUDENT_LAST_NAME + ", " + \
              Const.STUDENT_USER_NAME + ", " + \
              Const.STUDENT_PASSWORD + ", " + \
              Const.STUDENT_MATH + ", " + \
              Const.STUDENT_PROGRAMMING_LANGUAGE + ", " + \
              Const.STUDENT_HUMAN_COMPUTER_INTERACTION + ", " + \
              Const.STUDENT_GERMAN + ", " + \
              Const.STUDENT_ENGLISH + ", " + \
              Const.STUDENT_ALGORITHM + ') ' + 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        values = (
            student.getFirstName(),
            student.getLastName(),
            student.getUserName(),
            student.getPassword(),
            student.getMathGrade(),
            student.getProgrammingLanguegesGrade(),
            student.getHumanComputerInteractionGrade(),
            student.getGermanGrade(),
            student.getEnglishGrade(),
            student.getAlgorithmsAndDataStructureGrade()
        )

        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_teacher(self, teacher):
        sql = "INSERT INTO " + Const.TEACHERS_TABLE + "(" + \
              Const.TEACHER_FIRST_NAME + ", " + \
              Const.TEACHER_LAST_NAME + ", " + \
              Const.TEACHER_USER_NAME + ", " + \
              Const.TEACHER_PASSWORD + ", " + \
              Const.TEACHER_SUBJECT + ') ' + 'VALUES(%s,%s,%s,%s,%s)'

        values = (
            teacher.getFirstName(),
            teacher.getLastName(),
            teacher.getUserName(),
            teacher.getPassword(),
            teacher.getSubject()
        )

        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def insert_director(self, director):
        sql = "INSERT INTO " + Const.DIRECTOR_TABLE + "(" + \
              Const.TEACHER_FIRST_NAME + ", " + \
              Const.TEACHER_LAST_NAME + ", " + \
              Const.TEACHER_USER_NAME + ", " + \
              Const.TEACHER_PASSWORD + ') ' + 'VALUES(%s,%s,%s,%s)'

        values = (
            director.getFirstName(),
            director.getLastName(),
            director.getUserName(),
            director.getPassword()
        )

        self.mycursor.execute(sql, values)
        self.mydb.commit()




    def points(self, student_points):
        sql = 'INSERT INTO ' + Const.POINTS_TABLE + '(' + Const.POINTS_USER_NAME + ')' + 'VALUES (%s)'

        values = (
            student_points.getPointsUserName()
        )
        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def select_student(self, student):
        sql = "SELECT * FROM " + Const.STUDENTS_TABLE + " WHERE " + \
              Const.STUDENT_USER_NAME + "=%s AND " + \
              Const.STUDENT_PASSWORD + "=%s"

        values = (student.getUserName(), student.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_teacher(self, teacher):
        sql = "SELECT * FROM " + Const.TEACHERS_TABLE + " WHERE " + \
              Const.TEACHER_USER_NAME + "=%s AND " + \
              Const.TEACHER_PASSWORD + "=%s"

        values = (teacher.getUserName(), teacher.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_director(self, director):
        sql = "SELECT * FROM " + Const.DIRECTOR_TABLE + " WHERE " + \
              Const.DIRECTOR_USER_NAME + "=%s AND " + \
              Const.DIRECTOR_PASSWORD + "=%s"

        values = (director.getUserName(), director.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_subjects(self):
        sql = "SELECT * FROM " + Const.SUBJECT_TABLE
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_grade(self, student):
        sql = "SELECT * FROM " + Const.STUDENTS_TABLE + " WHERE " + \
              Const.STUDENT_USER_NAME + "=%s AND " + Const.STUDENT_PASSWORD + "=%s"
        values = (student.getUserName(), student.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_hw(self):
        sql = "SELECT * FROM " + Const.HW_TABLE
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_exams(self, student):
        sql = "SELECT * FROM " + Const.STUDENTS_TABLE + " WHERE " + \
              Const.STUDENT_USER_NAME + "=%s AND " + Const.STUDENT_PASSWORD + "=%s"
        values = (student.getUserName(), student.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_credits(self, student):
        sql = "SELECT * FROM " + Const.STUDENTS_TABLE + " WHERE " + \
              Const.STUDENT_USER_NAME + "=%s AND " + Const.STUDENT_PASSWORD + "=%s"
        values = (student.getUserName(), student.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_max_math(self, student_points):
        sql = "SELECT user_name, max(math_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchone()

    def select_max_pl(self, student_points):
        sql = "SELECT user_name, max(programming_langueges_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_hci(self, student_points):
        sql = "SELECT user_name, max(human_computer_interaction_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_german(self, student_points):
        sql = "SELECT user_name, max(german_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_english(self, student_points):
        sql = "SELECT user_name, max(english_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_algorithms(self, student_points):
        sql = "SELECT user_name, max(algorithms_and_data_structure_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_math(self, student_points):
        sql = "SELECT user_name, min(math_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchone()

    def select_min_pl(self, student_points):
        sql = "SELECT user_name, min(programming_langueges_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_hci(self, student_points):
        sql = "SELECT user_name, min(human_computer_interaction_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_german(self, student_points):
        sql = "SELECT user_name, min(german_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_english(self, student_points):
        sql = "SELECT user_name, min(english_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_algorithms(self, student_points):
        sql = "SELECT user_name, min(algorithms_and_data_structure_points) FROM " + Const.POINTS_TABLE + " WHERE " + \
              Const.POINTS_USER_NAME + "= '" + student_points.getPointsUserName() + "'"
        print(sql)
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_subject(self, teacher):
        sql = "SELECT * FROM " + Const.TEACHERS_TABLE + " WHERE " + Const.TEACHER_USER_NAME + "=%s AND " + Const.TEACHER_PASSWORD + "=%s"
        values = (teacher.getUserName(), teacher.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_subject_count_of_students(self):

        sql = "SELECT * FROM " + Const.SUBJECT_TABLE

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_exam_teacher(self, teacher):
        sql = "SELECT * FROM " + Const.TEACHERS_TABLE + " WHERE " + Const.TEACHER_USER_NAME + "=%s AND " + Const.TEACHER_PASSWORD + "=%s"
        values = (teacher.getUserName(), teacher.getPassword())
        self.mycursor.execute(sql, values)

        return self.mycursor.fetchall()

    def select_max_math_points(self):

        sql = "SELECT user_name, max(math_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()
    def select_max_programming_langueges_points(self):

        sql = "SELECT user_name, max(programming_langueges_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_human_computer_interaction_points(self):

        sql = "SELECT user_name, max(human_computer_interaction_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_german_points(self):

        sql = "SELECT user_name, max(german_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_english_points(self):

        sql = "SELECT user_name, max(english_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_max_algorithms_and_data_structure_points(self):

            sql = "SELECT user_name, max(algorithms_and_data_structure_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

            self.mycursor.execute(sql)

            return self.mycursor.fetchall()

    def select_min_math_points(self):

        sql = "SELECT user_name, min(math_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()
    def select_min_programming_langueges_points(self):

        sql = "SELECT user_name, min(programming_langueges_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_human_computer_interaction_points(self):

        sql = "SELECT user_name, min(human_computer_interaction_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_german_points(self):

        sql = "SELECT user_name, min(german_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_english_points(self):

        sql = "SELECT user_name, min(english_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_min_algorithms_and_data_structure_points(self):

        sql = "SELECT user_name, min(algorithms_and_data_structure_points) FROM " + Const.POINTS_TABLE + " GROUP BY user_name HAVING max(math_points) < 10000000"

        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

    def select_teachers(self):

        # sql = "SELECT CONCAT(first_name, " ", last_name) AS Name, subject FROM " + Const.TEACHERS_TABLE

        sql = "SELECT * FROM " + Const.TEACHERS_TABLE
        self.mycursor.execute(sql)

        return self.mycursor.fetchall()

