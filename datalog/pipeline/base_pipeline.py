'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-21 14:52:07
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 15:46:39
FilePath: /datalog/datalog/pipeline/base_pipeline.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
import os

class BasePipeline:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            os.makedirs(self.path)
    
    def save(self, data, meta_data, save_name):
        raise NotImplementedError