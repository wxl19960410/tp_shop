from time import sleep
from lib.webui import *
import pytest,allure
@allure.feature('测试单个商品的数量')
class Test_numlimit:
    def teardown_method(self):
        self.driver.quit()
    @allure.story('商品数量满足要求')
    @pytest.mark.parametrize(
        'num,expectedtxt',[
            ('1','添加收货地址'),
            ('2','添加收货地址'),
            ('100','添加收货地址'),
            ('200','添加收货地址'),
            ('199','添加收货地址')
        ],ids=[
            'num:1',
            'num:2',
            'num:100',
            'num:200',
            'num:199'])
    def test_numlimit_301_305(self,num,expectedtxt):
        self.driver=limit(num)
        text = self.driver.find_element_by_css_selector('[class="layui-layer-title"]').text
        assert text==expectedtxt


    @allure.story('商品数量不满足要求')
    @pytest.mark.parametrize(
        'num,expectedtxt',[
            ('0','商品数量必须大于0'),
            ('201','购买商品数量不能大于200')],
        ids=[
            'num:0',
            'num:201',
        ])
    def test_limit_306_307(self,num,expectedtxt):
        self.driver=limit(num)
        text = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        assert text==expectedtxt


