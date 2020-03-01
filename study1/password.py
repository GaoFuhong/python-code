# Author:Fuhong Gao

_usrename = "gfh"
_password = "abc123"
username = input("username:")
password = input("password:")
if _usrename == username and _password == password:
    print("Welcome user.txt {_user} login..".format(_user = username))
else:
    print("Invalid username or password!")