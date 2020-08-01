import pytest,allure
from lib.webui import   *
import time
@allure.feature('注册功能')
class Test_register():
    def teardown_method(self):
        self.driver.quit()
    test_datas=[
 ({'username':'1334567891','verify_code':'8888','password':'123456','password2':'123456','invite':'17854225747'},'请用手机号或邮箱注册','手机号输入10位'),
({'username':'133456789123','verify_code':'8888','password':'123456','password2':'123456','invite':'17854225747'},'请用手机号或邮箱注册','手机号输入12位'),
({'username':'23345678912','verify_code':'8888','password':'123456','password2':'123456','invite':'17854225747'},'请用手机号或邮箱注册','手机号第一位不为1'),
({'username':'12345678912','verify_code':'8888','password':'123456','password2':'123456','invite':'17854225747'},'请用手机号或邮箱注册','手机号第二位为2'),
({'username': '17854225750', 'verify_code':'8888','password':'12345', 'password2':'12345','invite': '17854225747'},'密码为6-16位大小写英文字母、数字或符号组合','输入密码为5位'),
({'username':'13345678912','verify_code':'1234','password':'123456','password2':'123456','invite':'17854225747'},'验证码错误','验证码设置错误：1234'),
({'username':'13345678912','verify_code':'8888','password':'123456','password2':'12345','invite':'17854225747'},'两次输入密码不一致','第二次密码设置为：12345'),
({'username':'17854225747','verify_code':'8888','password':'123456','password2':'123456','invite':'17854225747'},'账号已存在','输入已注册账号'),
]
    @allure.story('注册失败检测')
    @allure.title('{title}')
    @pytest.mark.parametrize('test_input,expectedtext,title',test_datas)
    def test_register_201_208(self,test_input,expectedtext,title):
        self.driver=register(test_input['username'],test_input['verify_code'],test_input['password'],test_input['password2'],test_input['invite'])
        alert=self.driver.find_element_by_css_selector('[class="layui-layer-content layui-layer-padding"]').text
        assert alert==expectedtext
    @allure.story('注册成功检测')
    @allure.title('使用规定的格式正确注册')
    def test_register_209(self):
        self.driver=register('13456278912','8888','123456','123456','17854225747')
        alert=self.driver.find_element_by_css_selector('[title="退出"]').text
        assert alert=='安全退出'
