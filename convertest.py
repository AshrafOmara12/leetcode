__author__ = 'Ashraf'

import pandas as pd
import json
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
            for parent in student['parents']:
                parents_data.append(parent)

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
school_id = data['schoolId']
school_name = data['name']
school_timeZone = data['timeZone']
school_schoolAdmins = data['schoolAdmins']
school_managers = data['managers']

columns = ['schoolId', 'Name', 'TimeZone']
df_school_id = pd.DataFrame([school_id], columns= ['School Id'])
df_school_name = pd.DataFrame([school_name], columns= ['school_name'])
df_school_timeZone = pd.DataFrame([school_timeZone], columns= ['school_timeZone'])
df_school_schoolAdmins = pd.DataFrame(school_schoolAdmins)
df_school_managers = pd.DataFrame(school_managers)
df_school_final = pd.concat([df_school_id, df_school_name,df_school_timeZone,df_school_schoolAdmins, df_school_managers], axis=1)
df_school_final_Times =pd.concat([df_school_final]*3188, ignore_index=True)


df_times = pd.DataFrame(studentperclassperteacher_list, columns=['Times'])
# print(df_times)
df_1 = pd.DataFrame(teacher_list)
del df_1['classes']
df_times_1 = pd.concat([df_1, df_times.set_index(df_1.index)], axis=1)
# df_new_1 = df_times_1.assign(Times = df_times_1.Times.apply(lambda x: range(1, x + 1))).explode('Times')
df_new_1 = df_times_1.loc[df_times_1.index.repeat(df_times_1['Times'])].reset_index(drop=True)
del df_new_1['Times']

df_2 = pd.DataFrame(classes_list)
del df_2['students']

df_times_classes = pd.DataFrame(no_of_students_per_class, columns=['Times'])

df_times_2 = pd.concat([df_2, df_times_classes.set_index(df_2.index)], axis=1)

df_new_2 = df_times_2.loc[df_times_2.index.repeat(df_times_2['Times'])].reset_index(drop=True)
del df_new_2['Times']

df_parents = pd.DataFrame(parents_data)

df_students  = pd.DataFrame(student_data)

del df_students['parents']


df_final = pd.concat([df_school_final_Times.set_index(df_new_1.index),df_new_1, df_new_2.set_index(df_new_1.index),df_students.set_index(df_new_1.index), df_parents.set_index(df_new_1.index)], axis= 1)

df_final.columns = ['School Id', 'school_name', 'school_timeZone',
                    'School_Admin_id','School_Admin_UserName',
                    'School_Admin_Email','School_Admin_National_id',
                    'School_Admin_Phone_Number',
                    'Managers_id','Managers_UserName',
                    'Managers_Email','Managers_National_id',
                    'Managers_Phone_Number',
                    'Teachers_id','Teachers_UserName',
                    'Teachers_Email','Teachers_National_id',
                    'Teachers_Phone_Number',
                    'classes_id','classes_name',
                    'classes_schoolyear',
                    'Students_id','Students_UserName',
                    'Students_Email','Students_National_id',
                    'Students_Phone_Number',
                    'Parents_id','Parents_UserName',
                    'Parents_Email','Parents_National_id',
                    'Parents_Phone_Number']

df_final.to_csv('report_all.csv', encoding = 'utf-8-sig', index=False)
