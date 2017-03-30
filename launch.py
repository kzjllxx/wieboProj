# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:48:23
#   作者：kk
#-------------------------
import codecs
from mongodb.pre_handle_data import *
# from mongodb.data_center import *

handler = pre_handle_data()
handler.get_male_content()
handler.get_female_content()
#已完成 handler.separate_sex()
# datacenter = data_center()



