# -*- coding: utf-8 -*-
"""发文字微博"""
import time

from browserfactory import get_browser


def post_weibo(content):
    browser = get_browser()
    # 跳转到用户的首页
    browser.get('https://m.weibo.cn/')
    browser.implicitly_wait(5)
    # 点击右上角的发布按钮
    post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
    # 在弹出的文本框中输入内容
    content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_key
    time.sleep(2)
    # 点击发布按钮
    post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
    time.sleep(1)
