'''Creating Classes'''
class User:
    def __init__(self,id,name):
     """Constructor using __init__ method to initialise the attributes for the objects we can create
        it is called every time user creates a new object"""
     self.user_id = id
     self.user_name = name
     self.followers = 0
     self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1



user_1 = User("001","Hitesh")
user_2 = User("002","Angela")
# print(user_1.user_id,user_1.user_name)
user_1.follow(user_2)
print(user_1.following,user_1.followers,user_2.following,user_2.followers)

