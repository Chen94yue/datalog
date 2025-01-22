'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-20 16:54:12
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-21 16:01:10
FilePath: /datalog/datalog/register.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
class DataTypeRegister:
    def __init__(self):
        self.data_types = dict()
        
    def register(self, data_type):
        def decorator(data_type_fun):
            self.data_types[data_type] = data_type_fun
            return data_type_fun
        return decorator
    
    def get_data_type(self, data_type, *args, **kwargs):
        if data_type not in self.data_types:
            raise ValueError(f"Data type {data_type} not registered")
        return self.data_types.get(data_type, None)(*args, **kwargs)

class ProcessRegister:
    def __init__(self):
        self.processes = dict()
        
    def register(self, process_name):
        def decorator(process_fun):
            self.processes[process_name] = process_fun
            return process_fun
        return decorator
    
    def get_process(self, process_name, *args, **kwargs):
        if process_name not in self.processes:
            raise ValueError(f"Process {process_name} not registered")
        return self.processes.get(process_name, None)(*args, **kwargs)
    
    
data_type_register = DataTypeRegister()
process_register = ProcessRegister()
