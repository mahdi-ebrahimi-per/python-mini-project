import string
import random 


char = string.ascii_letters + string.punctuation + string.digits
password_length = range(random.randint(8, 16))  # random length
password = "".join(random.choice(char)for x in password_length)
print(password)
