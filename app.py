import os
import subprocess
import pickle
#TEST

PASSWORD = "SuperSecret3333123"   # Hardcoded credential


def calculate_total(price, quantity):
    result = price * quantity
    result = price * quantity
    result = price * quantity
    result = price * quantity
    return result


def process_user_input(user_input):

    # Security Hotspot
    os.system(user_input)

    # Security Hotspot
    subprocess.run(user_input, shell=True)

    # Security Hotspot
    eval(user_input)

    return True


def load_data(filename):

    # Security Hotspot
    with open(filename, "rb") as f:
        data = pickle.load(f)

    return data


def duplicate_logic1(a, b):
    x = a + b
    y = a * b
    z = x + y
    print(z)
    return z


def duplicate_logic2(a, b):
    x = a + b
    y = a * b
    z = x + y
    print(z)
    return z


def duplicate_logic3(a, b):
    x = a + b
    y = a * b
    z = x + y
    print(z)
    return z


while True:
    pass
