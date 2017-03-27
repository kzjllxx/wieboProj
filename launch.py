# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:48:23
#   作者：kk
#-------------------------

from mongodb.mongoConnector import *
from mongodb.pre_handle_data import *
#连接mongoDB
# mongo = mongoConnector()

handler = pre_handle_data()
handler.separate_sex()

# #构建所有男性的content
# male_temp_content = ""
# for person in male_list:
#     print person["_id"]
#     for temp_bean in mongo.getUserTweetsByID(person["_id"]):
#         print "adding :"+temp_bean["Content"]
#         male_temp_content += temp_bean["Content"]

