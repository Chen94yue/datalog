'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-21 14:33:38
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 14:50:53
FilePath: /datalog/datalog/process/base_process.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''

class BaseProcess:
    def __init__(self):
        pass
    
    def process(self, data):
        raise NotImplementedError