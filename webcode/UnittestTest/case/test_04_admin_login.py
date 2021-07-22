import time
import unittest
from selenium import webdriver
from utils.common import cookie
from po.AdminLoginPage import AdminLoginPage

class TestCaseAdminLogin(unittest.TestCase):    
    @classmethod    
    def setUpClass(cls):        
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()        
        cls.admin_login_page = AdminLoginPage(cls.driver)       # 类的实例化对象        
        
    @classmethod    
    def tearDownClass(cls):        
        cls.driver.quit()    
    
    def setUp(self):        
        self.admin_login_page.open_url()    
    
    def test_01_login_failed(self):        
        self.admin_login_page.login("admin", "123456")    
    
    def test_02_login_success(self):        
        self.admin_login_page.login("admin", "shopxo")
