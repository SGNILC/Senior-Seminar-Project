from IPython.display import display
from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import random as r
import csv
import datetime 
from datetime import timedelta
import random

Faker.seed(0)
r.seed(0)
fake = Faker(['en_US'])

teachers = [
    'teacherID',
    'first_name',
    'last_name',
    "total_Student_Management",
    'schoolID',
    'classID'
    ]

teachers = pd.DataFrame(columns=teachers)

def pushData(row, schoolID, classID):
    teachers.loc[row,'first_name'] =  fake.first_name()
    teachers.loc[row,'last_name'] =  fake.last_name()
    teachers.loc[row,'total_Student_Management'] =  r.randint(10,30)
    teachers.loc[row,'schoolID'] =  schoolID
    teachers.loc[row,'classID'] =  r.randint(0,classID)
    teachers['teacherID'] = teachers.index
