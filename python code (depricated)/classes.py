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
from assigngrade import *
Faker.seed(0)
r.seed(0)
fake = Faker(['en_US'])

#Creating Fake Schools
classes = [
    'classID',
    'class_name',
    'teacherID_FK',
    'student_count', 
    "assignments", 
    "student_teacher_ratio", 
    ]

classes = pd.DataFrame(columns=classes)
class_names = DynamicProvider (
    provider_name='class_names',
    elements=['Chemestry','Biology','Computer Science','Senior Seminar','Art I', 'Art II', 'Film', 'Astronomy']
)
    
teachers = pd.read_csv('teachers.csv')
teacherCount = len(teachers.index)


for _ in range(teacherCount):
    class_name = r.choice(['Chemestry','Biology','Computer Science','Senior Seminar','Art I', 'Art II', 'Film', 'Astronomy'])
    teacherID = teachers['teacherID']
    student_count = round((teachers.loc[_, 'total_Student_Management']) / r.choice([1,2,3]))
    # assignments = assignments['assignmentID']
    student_teacher_ratio = (f"1: {round(student_count)}")
   
    classes.loc[_,'class_name'] = (f"{class_name}")
    classes['teacherID_FK'] = teachers['teacherID']
    classes.loc[_,'student_count'] = student_count
    classes.loc[_,['student_teacher_ratio']] = student_teacher_ratio
    classes['classID'] = classes.index

# CSV for school SOURCE: https://www.geeksforgeeks.org/how-to-create-a-csv-file-using-python/
csv_file_path = 'classes.csv'

classes.to_csv(csv_file_path, index=False)

print(f"CSV file {csv_file_path} created successfully.")
print(classes)