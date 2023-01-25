# Func to calculate average
def average(person: dict):

    courses_sum = 0
    total_courses = 0
    

    for course in person.values():
        
        if course == person["name"]:
            continue
        
        courses_sum += course 
        total_courses += 1

    average = courses_sum / total_courses

    return average

def smallest_average(person1: dict, person2: dict, person3: dict):
# Pass each dict to calculate average
    person_one_average = average(person1)
    person_two_average = average(person2)
    person_three_average = average(person3)

    

    if person_one_average < person_two_average and person_one_average < person_three_average:
        return person1
    elif person_two_average < person_one_average and person_two_average < person_three_average:
        return person2
    elif person_three_average < person_one_average and person_three_average < person_two_average:
        return person3




if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))