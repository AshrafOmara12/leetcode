import pandas as pd
import json
import numpy as np
from itertools import pairwise


parents_list = []
classes_list = []
teacher_list = []
parents_data = []
student_data = []
no_of_classes_per_teacher = []
no_of_students_per_teacher = []
no_of_students_per_class = []

with open('division_data_sample.json', encoding='utf-8') as f:
    data = json.load(f)
for teacher in  data['teachers']:
    teacher_list.append(teacher)
    no_of_classes_per_teacher.append(len(teacher['classes']))
    # print(len(teacher['classes']))
    for cclass in teacher['classes']:
        classes_list.append(cclass)
        no_of_students_per_teacher.append(len(cclass['students']))
        no_of_students_per_class.append(len(cclass['students']))
        # print(len(cclass['students']))
        for student in cclass['students']:
            student_data.append(student)
            parents_list.append(student['parents'])

slice_list = []
total = 0
for i in no_of_classes_per_teacher:
    total = total + i
    slice_list.append(total)

actual = []
for i, j in pairwise(slice_list):
   actual.append([i,j])

actual.insert(0, [0,3])
# print((actual))
studentperclassperteacher_list = []

for i in actual:
    studentperclassperteacher_list.append(sum(no_of_students_per_teacher[i[0]:i[1]]))

# print(studentperclassperteacher_list)
df_times = pd.DataFrame(studentperclassperteacher_list, columns=['Times'])
# print(df_times)
df_1 = pd.DataFrame(teacher_list)
del df_1['classes']
df_times_1 = pd.concat([df_1, df_times.set_index(df_1.index)], axis=1)
# df_new_1 = df_times_1.assign(Times = df_times_1.Times.apply(lambda x: range(1, x + 1))).explode('Times')
df_new_1 = df_times_1.loc[df_times_1.index.repeat(df_times_1['Times'])].reset_index(drop=True)
del df_new_1['Times']

# print(df_new_1.head(5))
df_2 = pd.DataFrame(classes_list)
del df_2['students']

df_times_classes = pd.DataFrame(no_of_students_per_class, columns=['Times'])

df_times_2 = pd.concat([df_2, df_times_classes.set_index(df_2.index)], axis=1)

df_new_2 = df_times_2.loc[df_times_2.index.repeat(df_times_2['Times'])].reset_index(drop=True)
del df_new_2['Times']
# print(df_new_2.head(5))

df_students  = pd.DataFrame(student_data)

df_final = pd.concat([df_new_1, df_new_2.set_index(df_new_1.index),df_students.set_index(df_new_1.index)], axis= 1)

df_final.to_csv('report.csv', encoding = 'utf-8-sig')
