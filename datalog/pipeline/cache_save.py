'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-21 16:46:17
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-22 09:47:16
FilePath: /datalog/datalog/pipeline/cache_save.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from datalog.register import data_type_register
from datalog.pipeline.base_pipeline import BasePipeline
from datalog.utils.timestamp import get_timestamp13
import os
from pympler import asizeof
import threading
import time
import psutil

class CacheSavePipeline(BasePipeline):
    def __init__(self, cfg):
        path = cfg['path']
        super(CacheSavePipeline, self).__init__(path)
        self.cfg = cfg
        self.data_save = data_type_register.get_data_type(cfg['data_type'], cfg['data_type_cfg'])
        self.meta_save = data_type_register.get_data_type(cfg['meta_data'], cfg['meta_data_cfg'])
        
        self.cache = list()
        self.cpu_use = 50 # default cpu usage
        self.cache_memory_cost = 0
        
        # check cache memory usage
        self.memory_check_thread = threading.Thread(target=self.memory_check)
    
        # update system cpu usage
        self.cpu_check_thread = threading.Thread(target=self.cpu_check)
        
        # save data
        self.save_thread = threading.Thread(target=self.save_cache)
        
        self.cpu_check_thread.start()
        self.memory_check_thread.start()
        self.save_thread.start()
        
    def __del__(self):
        self.memory_check_thread.join()
        self.cpu_check_thread.join()
        self.save_thread.join()
        
    def memory_check(self):
        while True:
            self.cache_memory_cost = asizeof.asizeof(self.cache)
            if self.cache_memory_cost > self.cfg['cache_size']:
                print(f"Cache size {self.cache_memory_cost} exceeds the limit {self.cfg['cache_size']}")
                while not self.cfg['force_save'] and self.cache_memory_cost > self.cfg['cache_size']:
                    self.cache.pop(0)
                    self.cache_memory_cost = asizeof.asizeof(self.cache)
            elif self.cache_memory_cost > self.cfg['max_cache_size']:
                raise RuntimeError(f"Cache size {self.cache_memory_cost} exceeds the limit {self.cfg['max_cache_size']}")
            else:
                time.sleep(1)
                
    def cpu_check(self):
        while True:
            self.cpu_use = psutil.cpu_percent(interval=1)
            
    def save_cache(self):
        while True:
            # print(f"Current cache size: {self.cache_memory_cost}") 
            if self.cache and self.cpu_use < self.cfg['cpu_threshold']:
                data, meta_data, data_save_path, meta_data_save_path = self.cache.pop(0)
                self.data_save.save(data, data_save_path)
                self.meta_save.save(meta_data, meta_data_save_path)
            
    def save(self, data, meta_data, source_name):
        time_stamp = get_timestamp13()
        data_save_path = os.path.join(self.path, f'{source_name}_{time_stamp}.{self.cfg["data_type_cfg"]["save_format"].split("_")[-1]}')
        meta_data_save_path = os.path.join(self.path, f'{source_name}_{time_stamp}.{self.cfg["meta_data_cfg"]["save_format"]}')
        
        if self.cpu_use < self.cfg['cpu_threshold']:
            # system cpu usage is low, save data directly
            self.data_save.save(data, data_save_path)
            self.meta_save.save(meta_data, meta_data_save_path)
        else:
            # system cpu usage is high, put data into cache
            self.cache.append((data, meta_data, data_save_path, meta_data_save_path))