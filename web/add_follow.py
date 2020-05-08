# -*- coding: utf-8 -*-
"""加关注"""
import time

from selenium.common.exceptions import NoSuchElementException

from browserfactory import get_browser


# 添加指定的用户
def add_follow(uid):
    browser = get_browser()
    browser.get('https://m.weibo.cn/u/' + str(uid))
    time.sleep(1)

    try:
        # browser.find_element_by_id("follow").click()
        follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
        follow_button.click()

        # 选择分组
        group_button = browser.find_element_by_xpath('//div//a[@class="m-btn m-btn-white m-btn-text-orange"]')
        group_button.click()
    except NoSuchElementException as e:
        print("can not follow")
    time.sleep(1)

    time.sleep(1)
