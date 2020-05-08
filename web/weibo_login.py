# -*- coding: utf-8 -*-
from browserfactory import get_browser
import time


# 登录微博
def weibo_login(username, password):
    browser = get_browser()
    # 打开微博登录页
    browser.get('https://weibo.com/')  # 电脑版登录页
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_css_selector("[node-type='username']").send_keys(username)
    browser.find_element_by_css_selector("[node-type='password']").send_keys(password)
    time.sleep(1)
    # 点击登录

    browser.find_element_by_css_selector("[node-type='submitStates']").click()
    time.sleep(1)
