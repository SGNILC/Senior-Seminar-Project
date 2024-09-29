#Libraries
from IPython.display import display
from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import random as r
import csv
import math
Faker.seed(0)
r.seed(0)
fake = Faker(['en_US'])

print(fake.first_name())
print(fake.address())
print(fake.last_name())

#Creating Fake Schools
schools = [
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
    for j in range(len(schools.columns)):
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

#display(schools[['school_address','teacher_population', 'student_enrollment', 'average_student_teacher_ratio']])

# CSV for school SOURCE: https://www.geeksforgeeks.org/how-to-create-a-csv-file-using-python/
csv_file_path = 'schools.csv'

#schools.to_csv(csv_file_path, index=False)

#print(f"CSV file {csv_file_path} created successfully.")

# Creating Fake Students
Faker.seed(1)
students = [
    'first_name',
    'last_name',
    'preferred_name',
    'class', 
    "graduation_year",
    'DOB'
    # "class_Grade",
    # 'age',
    # 'Ethnicity',
    # 'gender',
    # 'sex',
    # 'letter_grade',
    # 'socio_economic_tier',
    # "disciplinary_action_count"
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
    date = pd.date_range(start='1/1/2006', end='1/1/2010')
    df = pd.DataFrame(date)
    date = df.sample(n=1 , random_state=0)
    return date

for i in range(14):
    for j in range(len(schools.columns)):
        # state = fake.state()
        # teacher_population = r.randint(30,100)
        # average_student_teacher_ratio = 0
        # student_enrollment = r.randint(500,1000)
        # tuition =  r.randint(50000,100000)
    
        first_name = fake.first_name()
        last_name = fake.last_name()
        end = r.randint(0,len(first_name))
        preferred_name = first_name[:end]
        class_level = fake.class_levels()
        graduation_year = fake.grad_year()
        dob = createBirthday()
    # class_Grade =
    # age =
    # Ethnicity =
    # gender =
    # sex =
    # letter_grade =
    # socio_economic_tier =
    # disciplinary_action_count =

        students.loc[i,'first_name'] = first_name
        students.loc[i, 'last_name'] = last_name
        students.loc[i, 'preferred_name'] = preferred_name
        students.loc[i, 'class'] = class_level
        assignClassLevel(class_level)
        print(dob)
        #students.loc[i, 'DOB'] = dob

        print(dob)

           

        # schools.loc[i, 'average_student_teacher_ratio'] = (student_enrollment / teacher_population) / 100
        # schools.loc[i, 'student_enrollment'] = student_enrollment
        # schools.loc[i, 'tuition'] = tuition
print(students)