#Define course data
class Course:

    def __init__(self, name: str):

        self.__course_name = name
        self.__course_grade = 0
        self.__course_credit = 0


    def name(self):
        return self.__course_name

    def grade(self):
        return self.__course_grade
    
    def credit(self):
        return self.__course_credit

    def add_grade(self, grade: int):
        if grade < self.__course_grade:
            return
        self.__course_grade = grade

    def add_credit(self, credit: int):
        if self.__course_credit != 0:
            return
        self.__course_credit = credit

#Save all courses as objects and encapsulation
class CourseStatistic:

    def __init__(self):

        self.__courses = {}
        self.__statistics = {}

    def add_course(self, name: str, grade: int, credit: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        self.__courses[name].add_grade(grade)
        self.__courses[name].add_credit(credit)


    def get_data(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]

#Statistic data
    def statistics(self):

        total_courses = len(self.__courses)

        if total_courses == 0:
            return 0

        total_credits = 0
        grades_sum = 0

        grades = [0, 0, 0, 0, 0, 0, 0]

        for course in self.__courses.values():
            total_credits += course.credit()
            grades_sum += course.grade()
            grades[course.grade()] += 1

   
        mean = grades_sum / total_courses

        self.__statistics["total_courses"] = total_courses
        self.__statistics["total_credits"] = total_credits
        self.__statistics["grades_mean"] = round(mean, 1)


        self.__statistics["grades"] = grades

        return self.__statistics
#Main program
class CourseApplication:

    def __init__(self):

        self.__course = CourseStatistic()
 
    def menu(self):
        print("1 add course"
        "\n2 get course data"
        "\n3 statistics"
        "\n0 exit")

    def add_course(self):
        course_name = input("course: ")
        course_grade = int(input("grade: "))
        course_credit = int(input("credits: "))

        self.__course.add_course(course_name, course_grade, course_credit)

    def course_data(self):
        course_name = input("course: ")

        course_data = self.__course.get_data(course_name)

        if course_data == None:
            print("no entry for this course")
            return
        
        course_name = course_data.name()
        grade = course_data.grade()
        credit = course_data.credit()

        print(f"{course_name} ({credit} cr) grade {grade}")

        

    def courses_statistic(self):
       data =  self.__course.statistics()

       if data == 0:
        return

       total_courses = data["total_courses"]
       total_credits = data["total_credits"]
       grades_mean = data["grades_mean"]

       print(f"{total_courses} completed courses, a total of {total_credits} credits")
       print(f"mean {grades_mean}")
       print("grade distribution")

       for grade in range(5, 0, -1):

           grades_count = data["grades"][grade]
           row = "x" * grades_count
           print(f"{grade}: {row}")

    def execute(self):
        self.menu()

        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.course_data()
            elif command == "3":
                self.courses_statistic()
            else:
                self.menu()


application = CourseApplication()
application.execute()