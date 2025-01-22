<!--
 * @Author: chenyue93 chenyue21@jd.com
 * @Date: 2025-01-20 15:10:20
 * @LastEditors: chenyue93 chenyue21@jd.com
 * @LastEditTime: 2025-01-22 14:38:19
 * @FilePath: /datalog/README.md
 * @Description: 
 * 
 * Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
-->
<div align=center><img src="doc/icon.png" width="200px" >
<div align=left>

# datalog

数据落盘一直是一些在线算法实现数据回流的有效手段。特别是在一些实时的业务系统中。但是目前没有一款python的工具能够对数据落盘进行有效的管理。datalog能够被灵活的嵌入到任意python的实时推理业务中。只需要进行简单的设置，就可以实现统一的数据落盘。

datalog是一个轻量化数据落盘工具，提供以下功能：

- [ ] 支持多种数据类型的落盘，包括：文本，图像，视频，声音，点云，并支持灵活的自定义数据类型。
- [ ] 支持自定义数据落盘前的处理方式，防止敏感数据泄露。
- [x] 灵活的资源管理方式，可以用户自定义内存和硬盘缓存的大小。
- [x] 灵活的资源使用方式，自动监控当前系统资源使用情况，避免数据落盘对主进程带来太多负担。
- [ ] 系统的数据归集，完整的元数据保证能够轻松回溯系统运行状况。

## 安装方法

安装依赖项：

```shell
pip3 install -r requirements.txt
```

直接安装：
```shell
git clone https://github.com/Chen94yue/datalog.git
python3 setup.py install
```

## 使用方法

```python
from datalog.pipeline import CacheSavePipeline
import cv2
import time

data_log_cfg = {
    "path": "./tmp",
    "data_type": "image",
    "data_type_cfg": {
        "save_format": "npy"
    },
    "meta_data": "metadata",
    "meta_data_cfg": {
        "save_format": "yaml"
    },
    "cache_size": 1024*1024*1024,  # bytes, 1GB
    "force_save": False,
    "max_cache_size": 1024*1024*1024*10,  # bytes, 10GB
    "cpu_threshold": 20  # percent
}
    
data_log = CacheSavePipeline(data_log_cfg)

test_image = cv2.imread("./test.jpg")
test_meta = {
    "session_id": "6e611dea-23c9-4b80-b028-4c5fd7915eef",
    "timestamp_sec": 1736855233,
    "timestamp_nsec": 166895104
}

for i in range(10):
    data_log.save(test_image, test_meta, "test")
```

