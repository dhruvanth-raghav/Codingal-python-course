class UserAccount:
    def __init__(self):
        self.email = "abc@gmail.com"
        self.__password = "123456789012345678"#Private attribute
        #Private properties can only be accessed from the inside class methods
    def show_password(self):
        masked_password="*" * len(self.__password)
        print("Inside the method, I can see the password", masked_password)
#==========================================================

user= UserAccount()
print("Email:",user.email)
# print("Password:",user.password)

user.email = "sfj@gmail.com"
print("New email:", user.email)

# user.__password = "abcdefgh"
# print(user.__password)  #check later

user.show_password()