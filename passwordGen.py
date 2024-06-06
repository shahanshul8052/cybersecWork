import random
import string

# Function to generate a random password
def passwordGen(length):
    # Define the alphabet of characters to choose from
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of length 'length'
    password = "".join(random.choice(alphabet) for i in range(length))
    return password

# Generate a password of length 10
password = passwordGen(10)
# Print the password
print(f"Your password is: {password}")