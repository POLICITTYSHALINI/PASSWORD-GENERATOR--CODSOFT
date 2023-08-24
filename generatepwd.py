
import random
import string
print(" ****PASSWORD----GENERATOR****")

pg = int(input(" GIVE THE PASSWORD LENGTH"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation


all = lower + upper + number + symbols

temp = random.sample(all,pg)

password = "".join(temp)

print(password)