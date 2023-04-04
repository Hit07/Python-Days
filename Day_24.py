# File System
"""Reading/Opening/Writing/Closing Files"""
#
# with open("file.txt",mode="w") as file:
#     file.write("\njulie")
#     file.write("2")


with open("../../Desktop/file.txt",mode="r") as file:
# file.write("hello there")
    print(file.read())

# with open("file.txt",mode="x") as file:
#     file.write("\nXX")
#     file.write("2")


