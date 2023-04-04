''' List Comprehension '''
# number = [1,2,3]
# new_list = []
# for num in number:
#     num += 1
#     new_list.append(num)
# print(new_list)
# numbers = [1, 2, 3, 4, 5]
# new_list = [num+1 for num in numbers]
# print(new_list)
#
# double = [num*2 for num in range(1,5)]
# print(double)
#
# names = ["Alex", "Beth", "Carolina","Dave", "Elenor", "Hitesh"]
# new_names = [name.upper() for name in names if len(name) > 4]
# print(new_names)

''' Dictionary Comprehension'''
# import random
# names = ["Alex", "Beth", "Carolina","Dave", "Elenor"]
# new_dict = {
#     students: random.randint(1,100) for students in names
# }
# # passed_dict = {
# #     students: new_dict[students] for students in new_dict if new_dict[students] > 60
# # }
#
# passed_dict = {
#     students: score for (students,score) in new_dict.items() if score > 60
# }
#
# print(new_dict)
# print(passed_dict)
# ---------------------------------------------------------
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

# '''Looping throug dictionaries'''
# for (key,value) in student_dict.items():
#     print(value)

'''Looping through dataframe'''
import pandas as pd

student_data = pd.DataFrame(student_dict)
# print(student_data)
# for (key,value) in student_data.items():
#     print(value)

for (index,row) in student_data.iterrows():
    if row.student == "Angela":
        print(row.score)