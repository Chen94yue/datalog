'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-20 18:32:18
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-22 14:06:32
FilePath: /datalog/datalog/datatype/image.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from datalog.register import data_type_register
from datalog.datatype.base_datatype import BaseDataType

import cv2
from PIL import Image
import numpy as np
import h5py
import pickle


@data_type_register.register("image")
class Image(BaseDataType):
    def __init__(self, cfg=None):
        if cfg is None:
            self.save_format = 'npy'
        else:
            self.save_format = cfg.get('save_format', 'npy')
    
    def save(self, data, save_path):
        if self.save_format == 'npy':
            np.save(save_path, data)
        elif self.save_format == 'npz':
            np.savez(save_path, data)
        elif self.save_format == 'h5':
            with h5py.File(save_path, 'w') as f:
                f.create_dataset('data', data=data)
        elif self.save_format == 'pkl':
            pickle.dump(data, open(save_path, 'wb'))
        elif self.save_format == 'cv2_png':
            cv2.imwrite(save_path, data)
        elif self.save_format == 'pil_png':
            img = Image.fromarray(data)
            img.save(save_path)
        else:
            raise ValueError(f"Unsupported save format {self.save_format}")
        
        
        




