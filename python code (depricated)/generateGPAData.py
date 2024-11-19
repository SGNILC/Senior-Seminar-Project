import pandas as pd
import random as r
import csv
from datetime import timedelta
import random

gpa = [
    'gpaID',
    'letter_grade',
    'GPA'
    ]

gpa = pd.DataFrame(columns=gpa)
letter_grades = ['A','B','C','D','F']
values = [3.7,2.7,1.7,0.7,0.0]

def createGPATable():
    for i in range(len(letter_grades)):
        gpa.loc[i,'letter_grade'] = letter_grades[i]
        gpa.loc[i,'GPA'] = values[i]
    gpa['gpaID'] = gpa.index

    return gpa

#For a set of students, Provide a letter grade that matches their GPA
def assignLetterGrade(students):
    
    for _ in range(students.shape[0]):
        studentGPA = students.loc[_,'GPA']
        print(values[0])
        if ( values[0] <= studentGPA):
            students.loc[_,'letter_grade'] = 'A'
            print(students)
        elif (values[1] <= studentGPA):
            students.loc[_,'letter_grade'] = 'B'
        elif (values[2] <= studentGPA):
            students.loc[_,'letter_grade'] = 'C'
        elif (values[3] <= studentGPA):
            students.loc[_,'letter_grade'] = 'D'
        elif (studentGPA == None):
            print('--')
        else:
            print('F')

        #         student.loc[i,[letter_grade]] = gpa[i,['letter_grade']]

# print(students[['GPA','letter_grade']])