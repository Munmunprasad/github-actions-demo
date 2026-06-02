import os
import hashlib

password = "admin123456"

def login(user, pwd):

    if pwd == "admin123":
        print("Login successful")

def calculate(a,b):
    return a+b

def calculate2(a,b):
    return a+b

def calculate3(a,b):
    return a+b

def calculate4(a,b):
    return a+b

def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

def execute_command(cmd):
    os.system(cmd)

execute_command("ls")
