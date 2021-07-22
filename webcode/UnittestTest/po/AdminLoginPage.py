from utils.seleniumtools import find_element

class AdminLoginPage():

    # 1、把要用到的元素封装成成员变量
    # 构造方法：实例化类的时候，要去对这个类的成员变量赋值，固定的方法，会用就可以
    def __init__(self,d):
        """
            d:driver,浏览器
        """
        self.driver = d  # 在类中新增成员变量driver

        # 登录的账号密码按钮
        self.username = ('name','username')
        self.password = ('name','login_pwd')
        self.loginbtn = ('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
        
        self.nagviurl = 'http://118.24.255.132:19999/shopxo/admin.php'

    # 2、要执行的动作封装成成员方法
    def open_url(self):
        self.driver.get(self.nagviurl)

    def login(self,username,password):
        # 查找账号、密码、按钮框框
        find_element(self.driver,self.username).send_keys(username)
        find_element(self.driver,self.password).send_keys(password)
        find_element(self.driver,self.loginbtn).click()


# admin_login = AdminLoginPage("123")