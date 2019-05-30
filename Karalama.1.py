import math
import sys
from os import rename

import requests

# print(sys.version)
print(sys.executable)


def greet(x):
    greeting = 'hey, {}'.format(x)
    return greeting


r = requests.get('https://www.google.com')

print(r.status_code)
c = input("Bir sayi giriniz lutfen: ")
print(greet(c))
