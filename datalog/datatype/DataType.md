<!--
 * @Author: chenyue93 chenyue21@jd.com
 * @Date: 2025-01-21 10:40:40
 * @LastEditors: chenyue93 chenyue21@jd.com
 * @LastEditTime: 2025-01-21 14:29:26
 * @FilePath: /datalog/datalog/datatype/DataType.md
 * @Description: 
 * 
 * Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
-->

# 数据类型性能测试

**测试环境：MacBook Pro Apple M1 Max 32GB**

## 图像数据

**原始数据尺寸：1280*720*3**

### 存储大小：

|数据类型|png|pkl|npy|npz|h5|
|:-:|:-:|:-:|:-:|:-:|:-:|
|空间占用(byte)|1187658|3072162|3072128|3072264|3074048|

### 存储时间：

|数据类型|cv2_png|pil_png|pkl|npy|npz|h5|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|存储时间(ms)|27.5769|360.0804|1.4348|1.2237|1.3248|1.2960|

### 加载时间：

|数据类型|cv2_png|pil_png|pkl|npy|npz|h5|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|存储时间(ms)|17.4189|0.0486|0.3828|0.4073|0.0596|0.5609|

### 使用建议：
- 尽量避免保存png图像，可在完成落盘之后使用数据转换工具查看
- 除png之外，其他数据格式空间占用相当，存储时间也相当但加载时间npz最优。
- 考虑尽可能的降低数据存储时的压力，npz需要对矩阵进行压缩算法，建议使用npy格式。

## 元数据存储

**元数据示例**
```shell
{
    "humans_info": [
        {
            "user_id": "00000001",
            "tracking_id": 1,
            "reliable": False,
            "id_source": "tracking_body_reg",
            "id_source_rank": 2,
            "final_score": 0,
            "x": 0.584,
            "y": 0.036,
            "z": 0.785,
            "rx": 0.0,
            "ry": 0.0,
            "rz": 0.0,
            "face_x": 0.0,
            "face_y": 0.0,
            "face_z": 0.0,
            "chest_x": 0.611,
            "chest_y": -0.113,
            "chest_z": 0.929,
            "face_x2d": 343.0,
            "face_y2d": 158.0
        }
    ],
    "session_id": "6e611dea-23c9-4b80-b028-4c5fd7915eef",
    "timestamp_sec": 1736855233,
    "timestamp_nsec": 166895104
}
```
### 存储测试

|数据类型|json|pickle|yaml|txt|
|:-:|:-:|:-:|:-:|:-:|
|存储时间(ms)|0.1111|0.0540|0.0019|0.0654|

### 使用建议

- 若仅考虑效率，使用yaml最佳，资源开销最小且兼具可读性。
- 若想要缓存部分算法中间结果，或用一些特定工具直接查看原数据结果，可以考虑使用json，txt等，以兼容特定算法的标注规范。


