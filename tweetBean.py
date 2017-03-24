# -*- coding: utf-8 -*-
#-------------------------
#   版本：
#   日期：
#   作者：kk
#-------------------------

class tweetsBean(object):
    def __init__(self,tweet_id,content,like,transfer,pubTime,tools,publisher_id):
        self.tweet_id = tweet_id
        self.content = content
        self.like = like
        self.transfer = transfer
        self.pubTime = pubTime
        self.tools = tools
        self.publisher_id = publisher_id