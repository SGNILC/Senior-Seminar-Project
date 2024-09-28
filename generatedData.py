#Libraries
from faker import Faker
import pandas as pd
import random as r

Faker.seed(0)
fake = Faker(['en_US'])

print(fake.first_name())
print(fake.address())
print(fake.last_name())

#Creating Fake Schools
schools = [
    'school_name',
    'school_address'
    'state'
    'teacher_population', 
    "average_student_teacher_ratio", 
    "student_enrollment", 
    "tuition"
    ]

schools = pd.DataFrame(columns=schools)
school_name = fake.administrative_unit()
school_address = fake.address()
teacher_population = r.randint(500,1000)
average_student_teacher_ratio = 0
student_enrollment = 0
tuition = 0 

for i in range(3):
    for j in range(len(schools.columns)):
        schools.loc[i,'school_name'] = (f"{fake.last_name()} High School")
        schools.loc[i, 'school_address'] = fake.address()
        schools.loc[i, 'state'] = fake.state()
        schools.loc[i, 'teacher_population'] = r.randint(30,100)
        schools.loc[i, 'average_student_teacher_ratio'] = (r.randint(100,200)/100)
        schools.loc[i, 'student_enrollment'] = r.randint(500,1000)
        schools.loc[i, 'tuition'] = r.randint(50000,100000)

print(schools)