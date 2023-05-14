import random

class User:
    def __init__(self, name, username, email, phone_number=None, bank_details=None):
        self.name = name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.bank_details = bank_details
        
    def __str__(self):
        return f"Name: {self.name}\nUsername: {self.username}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nBank Details: {self.bank_details}"

class UserDatabase:
    def __init__(self):
        self.users = {}
        
    def add_user(self, name, username, email, phone_number=None, bank_details=None):
        user_id = random.randint(10000, 99999)
        user = User(name, username, email, phone_number, bank_details)
        self.users[user_id] = user
        return user_id
    
    def get_user(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        else:
            return None

# Use case
db = UserDatabase()
user_id = db.add_user("Susan", "maina", "susan@gmail.com", "0768390908", "0899876545664566")
user = db.get_user(user_id)
print(user)


import random
import string

# define a function to generate a random password
def generate_password(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# define a function to send password recovery email
def send_recovery_email(email):
    # code to send email with password recovery link or temporary password

# define a function to handle password recovery request
 def handle_recovery_request(email):
    # check if email exists in the database
    if email in user_database:
        # generate a new temporary password
        temp_password = generate_password(8)
        # update user's password in the database
        user_database[email]['password'] = temp_password
        # send password recovery email with the temporary password
        send_recovery_email(email)
        return "Password recovery email sent"
    else:
        return "Email not found in database"

# use
email = input("Enter your email address: ")
print(handle_recovery_request(email))

