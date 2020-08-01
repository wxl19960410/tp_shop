from time import sleep
from lib.webui import *
import pytest,allure
@allure.feature('登录功能')
class Test_login():
    def teardown_method(self):
        self.driver.quit()
    @allure.story('登录失败测试')
    @pytest.mark.parametrize('username,password,verify_code,expectedtext',[
        (None,None,None,'用户名不能为空!'),
        (None,'123456', None, '用户名不能为空!'),
        (None, None, '8888', '用户名不能为空!'),
        (None, '123456', '8888', '用户名不能为空!'),
        ('17854225747', None, None, '密码不能为空!'),
        ('17854225747', None, '8888', '密码不能为空!'),
        ('17854225747', '123456', None, '验证码不能为空!'),
        ('17854225746', '123456', '8888', '账号不存在!'),
        ('17854225747', '12345', '8888', '密码错误!'),
        ('17854225747', '123456', '1234', '验证码错误')],
         ids=[
             '输入账号密码验证码都为空',
             '输入账号验证码都为空',
             '输入账号密码都为空',
             '输入账号为空',
             '输入账号正确，密码验证码为空',
             '输入账号验证码正确，密码为空',
             '输入账号密码正确，验证码为空',
             '全部输入，输入账号不正确',
             '全部输入，输入密码不正确',
             '全部输入，输入验证码不正确'
             ])
    def test_101_110(self,username,password,verify_code,expectedtext):
        self.driver=login(username,password,verify_code)
        alert=self.driver.find_element_by_css_selector('[class="layui-layer-content layui-layer-padding"]').text
        assert alert==expectedtext

    @allure.story('登录成功测试')
    @allure.title('输入正确的账号密码验证码')
    def test_111(self):
        self.driver=login()
        alert=self.driver.find_element_by_css_selector('[title="退出"]').text
        assert alert=='安全退出'



