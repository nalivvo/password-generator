import re
import string
from random import sample

all = string.ascii_letters + string.digits + "!@#$%^&*()"
pattern = re.compile(r"^\d+(\.0+)?$")

while length := input('Enter 0 to end: '):
    if not pattern.match(length):
        print('Please enter a positive integer.')
        continue

    length = int(float(length))
    if not length: break

    a, b = divmod(length, len(all))
    
    password = ''
    for _ in range(a):
        password += ''.join(sample(all, len(all)))
    password += ''.join(sample(all, b))

    print(password)