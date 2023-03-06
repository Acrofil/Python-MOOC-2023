class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
    

def accepted(attempts: list):
    def accept(student: CourseAttempt):
        return student.grade
    
    return filter(accept, attempts)

def attempts_with_grade(attempts: list, grade: int):
    

    return list(filter(lambda x: x.grade == grade, attempts))

def passed_students(attempts: list, course: str):


    students = filter(lambda x: x.grade > 0 and x.course_name == course, attempts)

    return sorted(list(map(lambda student: student.student_name, students)))



if __name__ == "__main__":

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
