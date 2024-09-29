#Libraries
from IPython.display import display
from faker import Faker
import pandas as pd
import random as r
import csv

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
        schools.loc[i, 'school_address'] = school_address.replace('\n', " ")
        schools.loc[i, 'state'] = state
        schools.loc[i, 'teacher_population'] = teacher_population
        schools.loc[i, 'average_student_teacher_ratio'] = (student_enrollment / teacher_population) / 100
        schools.loc[i, 'student_enrollment'] = student_enrollment
        schools.loc[i, 'tuition'] = tuition

display(schools[['school_address','teacher_population', 'student_enrollment', 'average_student_teacher_ratio']])

# CSV for school SOURCE: 
csv_file_path = 'schools.csv'

schools.to_csv(csv_file_path, index=False)

print(f"CSV file {csv_file_path} created successfully.")