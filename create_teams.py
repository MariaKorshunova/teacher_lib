import pandas as pd
import numpy as np
import random

file_excel_list_students = "zr_2021.csv"
number_team_members = 3

students = pd.read_csv(file_excel_list_students, header=None, encoding='mbcs')
number_of_students = len(students.index)
team = 1
group = pd.DataFrame({"Name":[], "Team": []})
while number_of_students > 0:
    i = number_team_members
    while i > 0:
        student = random.randint(0, number_of_students - 1)
        group = group.append({"Name": students.loc[student, 0] , "Team": "Team %(team).0f" % {'team':team}}, ignore_index=True)
        students.drop(labels = [student], axis = 0, inplace = True)
        students.reset_index(drop=True, inplace=True)
        i -= 1
        number_of_students -= 1
    team += 1
    if number_of_students < number_team_members:
        teams = np.array(range(1, team))
        while number_of_students > 0:
            team = random.randint(0, len(teams) - 1)
            group = group.append({"Name": students.loc[number_of_students - 1, 0] ,
                                  "Team": "Team %(team).0f" % {'team':teams[team]}},
                                 ignore_index=True)
            teams = np.delete(teams, team)
            number_of_students -= 1
group = group.sort_values(by='Name')
group.to_excel('./teams.xlsx', index=False)