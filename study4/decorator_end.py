# Author:Fuhong Gao
#需求：假设有一个网站，包括index页面（不需要登录），home页面（需要登录），bbs页面（需要登录）。
user,passwd = 'gfh','iloveguxiao1314' #定义本地的用户名和密码
#以下是定义的一个装饰器（嵌套了三层函数）：
def auth(auth_type):
    print("authentication type:",auth_type) #打印传进来的参数是不是“local”和“ldap”
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args,**kwargs)
                    print("-------after authentication-------")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password!\033[0m")
            elif auth_type == "ldap":
                print("\033[30;1mlog in through ldap...\033[0m")
        return wrapper
    return outer_wrapper
def index():
    print("Welcome to index page...")
@auth(auth_type = "local") #使用本地用户名、密码登录
def home():
    print("Welcome to home page...")
    return "from home..."
@auth(auth_type = "ldap") #使用ldap方式登录
def bbs():
    print("Welcome to bbs page...")
    return "from bbs..."
index()
print(home())
bbs()
