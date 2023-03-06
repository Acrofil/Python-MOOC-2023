from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    total_attemts = reduce(credits_sum_helper, attempts, 0) # call reduce pass helper func and list of attempts
    return total_attemts # return all credits of all attempts

def credits_sum_helper(attempts_sum, attempts): # sum all credits
    return attempts_sum + attempts.credits

def sum_of_passed_credits(attempts: list):
    students_pass = list(filter(lambda x: x.grade > 1, attempts)) # filter those with grade greater than 1 in the attempts list
    total_credits = reduce(passed_credits_sum_helper, students_pass, 0) # use reduce to sum total sum of credits for those who pass

    return total_credits

def passed_credits_sum_helper(students_pass, student): # helper func for summing credits for those who pass
    return students_pass + student.credits # sum and return


def average(attempts: list):
    students_who_pass = list(filter(lambda x: x.grade > 1, attempts)) # filter those with grade greater than 1 using lambda and attempts as itterator, convert to list
    sum_of_grades = reduce(average_helper, students_who_pass, 0) # use reduce to sum the grade for those who pass
    avg = sum_of_grades / len(students_who_pass) # find average the sum / total students who pass

    return avg 

def average_helper(avg_sum, avg): # helper func for reduce
    return avg_sum + avg.grade


if __name__ == "__main__":

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)