from functools import wraps
import getpass
from Auth.auth_metodes import *


SESSION={}

def Login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not SESSION.get("user_id"):
            print("You must login")
            email=input("Email:  ")
            password=getpass("Password:  ")
            success,msg=signin(email,password)
            if not success:
                print(msg)
                return None
            SESSION["user_id"]=email
            print(msg)
        return func(*args,**kwargs)
    return wrapper
