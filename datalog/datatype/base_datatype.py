'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-20 18:35:27
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 10:16:19
FilePath: /datalog/datalog/datatype/base_datatype.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
class BaseDataType:
    def __init__(self):
        pass
    
    def save(self, data):
        raise NotImplementedError
    
    def load(self, data):
        raise NotImplementedError
    
    def trans(self, data):
        raise NotImplementedError
