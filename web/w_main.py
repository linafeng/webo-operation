# -*- coding: utf-8 -*-
# 需要自己下载驱动放到scripts目录下，python需要配置环境变量

from web.weibo_login import weibo_login
from web.add_follow import add_follow
from web.post_weibo import post_weibo
from web.add_comment import add_comment

# 设置用户名、密码
username = 'XXXX'
password = "XXXX"
weibo_login(username, password)

# 每天学点心理学 UID
uid = '1890826225'
# add_follow(uid)

# 给指定的微博写评论
weibo_url = 'https://weibo.com/2598305800/J0Yna7BJx'
# 'https://weibo.com/1890826225/HjjqSahwl'
content = u'感恩'
add_comment(weibo_url, content)
# 自动发微博
content = '每天学点心理学'
post_weibo(content)
