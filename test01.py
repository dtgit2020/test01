import sys
import requests
import os
import math

# run python3 -m venv venv to make virtual enviromnent
# pip install requests
# use black formatter

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet("World"))
# print(greet("Corey"))

r = requests.get("https://www.google.com")
print(r.status_code)

name = input("Your Name?")
print("Hello,", name)
