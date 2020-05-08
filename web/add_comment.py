# -*- coding: utf-8 -*-
"""给指定某条微博添加内容"""

import time
from browserfactory import get_browser


def add_comment(weibo_url, content):
    browser = get_browser()
    browser.get(weibo_url)
    browser.implicitly_wait(5)
    content_textarea = browser.find_element_by_css_selector("textarea.W_input")
    content_textarea.clear()
    content_textarea.send_keys(content)
    time.sleep(2)
    comment_button = browser.find_element_by_css_selector(".W_btn_a").click()
    time.sleep(1)
