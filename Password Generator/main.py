import random
import string

char_list = list(string.ascii_letters)
num_list = list(string.digits)
special_list = list(string.punctuation)

char_length = int(input("Enter the number of letters: "))
num_length = int(input("Enter the number of numbers: "))
spec_length = int(input("Enter the number of special characters: "))

password_list = [
    random.choice(char_list) for _ in range(char_length)
] + [
    random.choice(num_list) for _ in range(num_length)
] + [
    random.choice(special_list) for _ in range(spec_length)
]

random.shuffle(password_list)
password ='' .join(password_list)
print("Generated Password: ", password)
