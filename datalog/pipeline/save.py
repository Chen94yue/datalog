'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-21 14:58:41
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 16:41:17
FilePath: /datalog/datalog/pipeline/save.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from datalog.register import data_type_register
from datalog.pipeline.base_pipeline import BasePipeline
from datalog.utils.timestamp import get_timestamp13
import os

class SavePipeline(BasePipeline):
    def __init__(self, cfg):
        path = cfg['path']
        super(SavePipeline, self).__init__(path)
        self.cfg = cfg
        self.data_save = data_type_register.get_data_type(cfg['data_type'], cfg['data_type_cfg'])
        self.meta_save = data_type_register.get_data_type(cfg['meta_data'], cfg['meta_data_cfg'])
            
    def save(self, data, meta_data, source_name):
        time_stamp = get_timestamp13()
        data_save_path = os.path.join(self.path, f'{source_name}_{time_stamp}.{self.cfg["data_type_cfg"]["save_format"].split("_")[-1]}')
        meta_data_save_path = os.path.join(self.path, f'{source_name}_{time_stamp}.{self.cfg["meta_data_cfg"]["save_format"]}')        
        self.data_save.save(data, data_save_path)
        self.meta_save.save(meta_data, meta_data_save_path)
    
    
    
        
        

