import pandas as pd

def assignmentLetterGrade(assignment, gradesTable):
    
    for _ in range(assignment.shape[0], ):
        score = assignment.loc[_,'score']
        print(score)
        if ( score >= 90):
            assignment.loc[_,'grade'] = 'A'
        #     print(students)
        elif (score >= 80):
            assignment.loc[_,'grade'] = 'B'
        elif (score >= 70):
            assignment.loc[_,'grade'] = 'C'
        elif (score >= 60):
           assignment.loc[_,'grade'] = 'D'
        else:
            assignment.loc[_,'grade'] = 'F'
    print(assignment)

assignment = pd.read_csv('assignment.csv')
gradesTable = pd.read_csv('assignment_grade .csv')

assignment = pd.DataFrame(assignment)
gradesTable = pd.DataFrame(gradesTable)
print(assignmentLetterGrade(assignment,gradesTable))