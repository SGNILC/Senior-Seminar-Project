#Libraries
from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import random as r
import csv
import datetime 
from datetime import timedelta
import random
from generateGPAData import createGPATable
from generateGPAData import assignLetterGrade
from generateTeacherData import *
Faker.seed(0)
r.seed(0)
fake = Faker(['en_US'])

#Creating Fake Schools
schools = [
    'schoolID',
    'school_name',
    'school_address',
    'state',
    'teacher_population', 
    "average_student_teacher_ratio", 
    "student_enrollment", 
    "tuition"
    ]

schools = pd.DataFrame(columns=schools)

for i in range(3):
    school_name = fake.administrative_unit()
    school_address = fake.address()
    state = fake.state()
    teacher_population = r.randint(30,100)
    average_student_teacher_ratio = 0
    student_enrollment = r.randint(500,1000)
    tuition =  r.randint(50000,100000)
   
    schools.loc[i,'school_name'] = (f"{school_name} High School")
    schools.loc[i, 'school_address'] = school_address.replace('\n', " ").replace('Apt.', '')
    schools.loc[i, 'state'] = state
    schools.loc[i, 'teacher_population'] = teacher_population
    schools.loc[i, 'average_student_teacher_ratio'] = (student_enrollment / teacher_population) / 100
    schools.loc[i, 'student_enrollment'] = student_enrollment
    schools.loc[i, 'tuition'] = tuition 
    schools['schoolID'] = schools.index

# CSV for school SOURCE: https://www.geeksforgeeks.org/how-to-create-a-csv-file-using-python/
csv_file_path = 'schools.csv'

schools.to_csv(csv_file_path, index=False)

print(f"CSV file {csv_file_path} created successfully.")

# Creating Fake Students
Faker.seed(1)
students = [
    'studentID',
    'first_name',
    'last_name',
    'preferred_name',
    'class', 
    "graduation_year",
    'dob',
    #"class_Grade",
    'ethnicity',
    'gender',
    'sex',  
    'letter_grade',
    'socio_economic_tier',
    "disciplinary_action_count",
    'GPA'
    ]
students = pd.DataFrame(columns=students)

class_levels = DynamicProvider (
    provider_name = 'class_levels',
    elements=['Freshman','Sophomore','Junior','Senior']
)
grad_year = DynamicProvider (
    provider_name = 'grad_year',
    elements=[2025,2026,2027,2028]
)

fake.add_provider(class_levels)
fake.add_provider(grad_year)

def assignClassLevel(class_level):
    if (class_level == 'Senior'):
        students.loc[i, 'graduation_year'] = 2025
    elif (class_level == 'Junior'):
        students.loc[i, 'graduation_year'] = 2026
    elif (class_level == 'Sophomore'):
        students.loc[i, 'graduation_year'] = 2027
    else:
        students.loc[i, 'graduation_year'] = 2028

def createBirthday():
    beginningDate = datetime.date(2006,1,1)
    endDate = datetime.date(2010,12,31)
    num_of_days = (endDate - beginningDate).days
    random_days = r.randint(1,num_of_days)
    random_date = beginningDate + datetime.timedelta(days=random_days)
    return random_date
def the_sex(gender):
    if (gender == 'Man'):
        sex = 'M'
    elif (gender == "Woman"):
        sex = 'F'
    else:
        sex = r.choice(['M','F'])
    return sex

for i in range(30):
    first_name = fake.first_name()
    last_name = fake.last_name()
    end = r.randint(0,len(first_name))
    preferred_name = first_name[:end]
    class_level = fake.class_levels()
    graduation_year = fake.grad_year()
    dob = createBirthday()
    # class_Grade =
    # age =
    ethnicity = r.choice(['White','Black or African American','American Indian or Alaska Native','Asian','Native Hawaiian and otherPacific Islander','Multiracial','Other'])
    gender = r.choice(['Man','Woman','Non-Binary'])
    gpa = (r.randint(10,40)) / 10
    
    # letter_grade =
    socio_economic_tier = r.choice(['U','M','W'])
    disciplinary_action_count = r.randint(0,200)

    students.loc[i,'first_name'] = first_name
    students.loc[i, 'last_name'] = last_name
    students.loc[i, 'preferred_name'] = preferred_name
    students.loc[i, 'class'] = class_level
    assignClassLevel(class_level)
    students.loc[i, 'dob'] = dob
    students.loc[i, 'ethnicity'] = ethnicity
    students.loc[i, 'gender'] = gender
    students.loc[i, 'sex'] = the_sex(gender)
    students.loc[i, 'socio_economic_tier'] = socio_economic_tier
    students.loc[i, 'disciplinary_action_count'] = disciplinary_action_count
    if (class_level == 'Freshman'):
        students.loc[i, 'GPA'] = None
    else:
        students.loc[i, 'GPA'] = gpa
    students['studentID'] = students.index

display(students)
# CSV for school SOURCE: https://www.geeksforgeeks.org/how-to-create-a-csv-file-using-python/
csv_file_path = 'students.csv'

students.to_csv(csv_file_path, index=False)

print(f"CSV file {csv_file_path} created successfully.")

# Creating Fake Teachers
print(len(schools.index))
schoolCount = len(schools.index)
endingID = 0 #
for i in range(schoolCount):
    teacherCount = schools.loc[i,'teacher_population']
    for _ in range(teacherCount):
        schoolID = schools.loc[i,'schoolID']
        print(endingID)
        pushData(_ + endingID,schoolID,3)
    endingID = teacherCount + endingID
print(teachers)

# CSV for school SOURCE: https://www.geeksforgeeks.org/how-to-create-a-csv-file-using-python/
csv_file_path = 'teachers.csv'
teachers.to_csv(csv_file_path, index=False)
print(f"CSV file {csv_file_path} created successfully.")

#Create GPA Table
gpaTable = createGPATable()
students = pd.read_csv('students.csv')

assignLetterGrade(students)
csv_file_path = 'gpa.csv'
gpaTable.to_csv(csv_file_path, index=False)
print(f"CSV file {csv_file_path} created successfully.")
