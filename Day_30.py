'''Exception Handling'''

# try:
#     file = open("file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["key"])
#
# except FileNotFoundError:
#     file = open("file.txt", mode="w")
#     file.write("Something")
#
# except KeyError as err:
#     print(f"key {err} not found")
#
# else:
#     print(file.read())
#
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("I raised an error")
# ===================================================
'''BMI'''
height = float(input("enter height:"))
weight = int(input("enter weight:"))

if height > 3:
    raise ValueError("The height cannot be over 3 meters")

bmi = weight / height ** 2
print(bmi)
# # ============================================================
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except:
#         print("Fruit pie")A
#     else:
#         print(fruit + " pie")
#
#------------------------------------------------------
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except:
#         total_likes += 0
#
#
# print(total_likes)

# ----------------------------------------------------