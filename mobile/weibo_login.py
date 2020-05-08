# -*- coding: utf-8 -*-
from browserfactory import get_browser
import time


# 登录微博
def weibo_login(username, password):
    browser = get_browser()
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login')  # 手机版登录页
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_id("loginName").send_keys(username)
    browser.find_element_by_id("loginPassword").send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_id("loginAction").click()
    time.sleep(1)

