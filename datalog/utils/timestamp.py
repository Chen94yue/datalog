'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-20 18:44:24
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 10:12:23
FilePath: /datalog/datalog/utils/timestamp.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
import time

def get_timestamp13():
    timestamp13 = int(time.time() * 1000)
    return timestamp13

def get_datetime():
    date = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    return date