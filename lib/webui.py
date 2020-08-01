from selenium import webdriver
import pytest
from time import sleep
def login(username='17854225747',password='123456',verify_code='8888'):
    driver = webdriver.Chrome()
    url = 'http:/192.168.1.106:88/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_css_selector('.red').click()
    if username is not None:
        driver.find_element_by_css_selector('.text_cmu').send_keys(username)
    if password is not None:
        driver.find_element_by_css_selector('[type="password"]').send_keys(password)
    if verify_code is not None:
        driver.find_element_by_css_selector('#verify_code').send_keys(verify_code)
    driver.find_element_by_css_selector('[name="sbtbutton"]').click()
    return driver
def register(username,verify_code,password,password2,invite):
    driver=webdriver.Chrome()
    driver.get('http://192.168.1.106:88/Home/User/reg.html')
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('[id="username"]').send_keys(username)
    driver.find_element_by_css_selector('div input[name="verify_code"]').send_keys(verify_code)
    driver.find_element_by_css_selector('[id="password"]').send_keys(password)
    driver.find_element_by_css_selector('[id="password2"]').send_keys(password2)
    driver.find_element_by_css_selector('[name="invite"]').send_keys(invite)
    driver.find_element_by_css_selector('[class="regbtn J_btn_agree"]').click()
    return driver






def limit(number):
    driver=login()
    driver.find_element_by_css_selector('[class="c-n fl"]').click()
    driver.find_element_by_css_selector('[class="wi43 fl"]').clear()
    driver.find_element_by_css_selector('[class="wi43 fl"]').send_keys(number)
    driver.find_element_by_css_selector('[class="gwc-qjs"]').click()
    return driver

def item():
    driver = login()
    driver.find_element_by_css_selector('[class="c-n fl"]').click()
    # text=driver.find_element_by_id('goods_num').text
    # print(text)
    return driver

# 自动添加购物车
def autoadd(num):
    driver = login()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
    driver.find_elements_by_class_name('nav-more-btn')[1].click()
    for i in range(num):
        driver.find_elements_by_class_name('p-btn')[i].click()
        sleep(2)
        try:
            driver.find_element_by_css_selector('#join_cart').click()
            sleep(2)
            driver.switch_to.frame('layui-layer-iframe1')
            driver.find_element_by_xpath('//*[@id="addCartBox"]/div[1]/div/div/a[1]').click()
            driver.switch_to.default_content()
            driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]').click()
        except:
            sleep(2)
            driver.switch_to.frame('layui-layer-iframe1')
            driver.find_element_by_xpath('//*[@id="addCartBox"]/div[1]/div/div/a[1]').click()
            driver.switch_to.default_content()
            driver.refresh()

        sleep(2)
    driver.find_element_by_css_selector('[class="c-n fl"]').click()
    return driver


