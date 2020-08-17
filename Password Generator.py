"""This programme generates a strong password
        using lowercase and uppercase letters, numbers and symbols"""

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#*_-[{}]/."

all = lower + upper + numbers + symbols
length = 16

password = "".join(random.sample(all, length))
print(f"Password is: {password}")