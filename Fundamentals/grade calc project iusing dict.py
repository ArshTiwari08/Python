# Creating a dictionary which
# consists of the student name,
# assignment result test results
# and their respective lab results

# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
        "assignment": [82, 56, 44, 30],
        "test": [80, 80],
        "lab": [67.90, 78.72]
        }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
        "assignment": [77, 82, 23, 39],
        "test": [78, 77],
        "lab": [80, 80]
        }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
        "assignment": [29, 89, 60, 56],
        "test": [65, 56],
        "lab": [50, 40.6]
        }

# Function calculates average
def get_avarage(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum/len(marks)

# Function calculates total average
def caluculate_total_avarage (student):
    assignment = get_avarage(student["assignment"])
    test = get_avarage(student["test"])
    lab = get_avarage(student["lab"])
    return((0.1 * assignment +0.7 * test + 0.2 * lab))
    
def assign_letter_grade(score):
    if score>=90:
        return("A")
    elif score>=80:
        return("B")
    elif score>=70:
        return("C")
    elif score>=60:
        return("D")
    else:
        return "E"
# Function to calculate the total
# average marks of the whole class

def class_avarage_is(student_list):
    result_list =[]
    for student in student_list:
        stu_avg = caluculate_total_avarage(student)
        result_list.append(stu_avg)
        return get_avarage(result_list)
    

students = [jack, james, dylan, jess, tom]

for i in students:
    print(i["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Avarage marks of %s is :%s " % (i["name"],caluculate_total_avarage(i)))
    print("letter grede of %s is :%s" %(i["name"],assign_letter_grade(caluculate_total_avarage(i))))

    print()

class_av = class_avarage_is(students)
print("Class Avarge is %s" %(class_av))
print("Latterm Garde of the class is %s" % (assign_letter_grade(class_av)))