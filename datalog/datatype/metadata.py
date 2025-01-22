'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-21 11:23:01
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 16:35:36
FilePath: /datalog/datalog/datatype/metadata.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from datalog.register import data_type_register
from datalog.datatype.base_datatype import BaseDataType

import json
import yaml
import pickle


@data_type_register.register("metadata")
class Metadata(BaseDataType):
    def __init__(self, cfg=None):
        if cfg is None:
            self.save_format = 'yaml'
        else:
            self.save_format = cfg.get('save_format', 'yaml')
    
    def save(self, data, save_path):
        if self.save_format == 'yaml':
            with open(save_path, 'w') as f:
                yaml.dump(data, f)
        elif self.save_format == 'json':
            with open(save_path, 'w') as f:
                json.dump(data, f)
        elif self.save_format == 'txt':
            with open(save_path, 'w') as f:
                f.write(str(data))
        elif self.save_format == 'pkl':
            pickle.dump(data, open(save_path, 'wb'))
        else:
            raise ValueError(f"Unsupported save format {self.save_format}")
            
        