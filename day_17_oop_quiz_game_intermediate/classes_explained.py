class User:

    def __init__(self, user_id, username):  # automatically set values for given attributes
        self.id = user_id                   # (self, attribute1, attribute2) # self.attribute = attribute_variable
        self.username = username            # tying attribute names to methods
        self.followers = 0
        self.following = 0

    def follow(self, user):  # function w.r.t object it is applied too, and parameters
        user.followers += 1  # increase parameter user followers by 1
        self.following += 1  # increase parameter self following by 1


user_1 = User("001", "will")
user_2 = User("002", "shaggy")

print(user_1.followers)

user_2.follow(user_1)

print(user_1.followers)
