# -*- coding: utf-8 -*-
# 需要自己下载驱动放到scripts目录下，python需要配置环境变量

from web.weibo_login import weibo_login
from web.add_follow import add_follow

# 设置用户名、密码
username = 'xxxx'
password = "xxxx"
weibo_login(username, password)

# 每天学点心理学 UID
uid = '1890826225'
add_follow(uid)


