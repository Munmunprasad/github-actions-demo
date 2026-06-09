# app.py

import os
import sqlite3
import subprocess
import hashlib

# ==================================================
# Hardcoded Credentials (Security Vulnerability)
# ==================================================

DB_PASSWORD = "admin123"
API_KEY = "secret-api-key"
AWS_SECRET = "AKIA_TEST_SECRET"

# ==================================================
# Global Variable (Code Smell)
# ==================================================

counter = 0

# ==================================================
# Duplicate Function #1
# ==================================================

def calculate_discount(price):
    if price > 1000:
        return price * 0.10
    else:
        return price * 0.05

# ==================================================
# Duplicate Function #2
# ==================================================

def calculate_special_discount(price):
    if price > 1000:
        return price * 0.10
    else:
        return price * 0.05

# ==================================================
# SQL Injection Vulnerability
# ==================================================

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user_id

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result

# ==================================================
# Command Injection Vulnerability
# ==================================================

def ping_host(host):
    command = "ping -c 1 " + host
    os.system(command)

# ==================================================
# Security Hotspot
# ==================================================

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

# ==================================================
# Bug - NoneType Error
# ==================================================

def get_name_length():
    name = None
    return len(name)

# ==================================================
# Bug - Division by Zero
# ==================================================

def calculate_average(total, count):
    return total / count

# ==================================================
# Unused Variable
# ==================================================

def print_message():
    temp = "I am not used anywhere"
    print("Hello")

# ==================================================
# Empty Exception Handling
# ==================================================

def process_file():
    try:
        file = open("missing.txt")
        data = file.read()
        print(data)
    except:
        pass

# ==================================================
# Dead Code
# ==================================================

def dead_code():
    return

    print("This will never execute")

# ==================================================
# Long Function / Technical Debt
# ==================================================

def monster_function(age, salary, city, experience):

    if age > 18:

        if salary > 10000:

            if city == "Bangalore":

                if experience > 5:
                    print("Case 1")

                elif experience > 4:
                    print("Case 2")

                elif experience > 3:
                    print("Case 3")

                elif experience > 2:
                    print("Case 4")

                elif experience > 1:
                    print("Case 5")

                else:
                    print("Case 6")

            else:

                if experience > 5:
                    print("Case 7")

                elif experience > 4:
                    print("Case 8")

                elif experience > 3:
                    print("Case 9")

                elif experience > 2:
                    print("Case 10")

                else:
                    print("Case 11")

        else:

            print("Low Salary")

    else:

        print("Minor")

# ==================================================
# Weak Randomness
# ==================================================

def generate_token():
    import random

    return str(random.randint(1000, 9999))

# ==================================================
# Insecure Subprocess
# ==================================================

def run_command(cmd):
    subprocess.call(cmd, shell=True)

# ==================================================
# Too Many Local Variables
# ==================================================

def complex_calculation():

    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    g=7
    h=8
    i=9
    j=10
    k=11
    l=12

    total = a+b+c+d+e+f+g+h+i+j+k+l

    return total

# ==================================================
# Magic Numbers
# ==================================================

def grade(score):

    if score > 91:
        return "A"

    elif score > 81:
        return "B"

    elif score > 71:
        return "C"

    elif score > 61:
        return "D"

    else:
        return "F"

# ==================================================
# Main
# ==================================================

if __name__ == "__main__":

    print_message()

    calculate_discount(2000)

    calculate_special_discount(2000)

    generate_token()

    complex_calculation()

    monster_function(30, 20000, "Bangalore", 5)

    get_user("1 OR 1=1")

    ping_host("google.com")
