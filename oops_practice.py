class usaraccount :
    def __init__(self, name , email , is_active =True):
        self.name = name
        self.email = email 
        self.status = is_active

    def get_profile_info(self):
        print(f"username: {self.name} email: {self.email} active: {self.status}")

    def deactivate_account(self):
        if self.status == True:
            self.status = False

user1 = usaraccount("ash","ash@gmail.com")
user1.get_profile_info()
user1.deactivate_account()
user1.get_profile_info()


