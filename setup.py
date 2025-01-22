'''
Author: chenyue93 chenyue21@jd.com
Date: 2025-01-22 09:56:22
LastEditors: chenyue93 chenyue21@jd.com
LastEditTime: 2025-01-22 14:02:03
FilePath: /datalog/setup.py
Description: 

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

setup(
    name='datalog',
    version='0.1.0',
    author='Burger',
    author_email='cy1454@tju.edu.cn',
    description='A package for data logging and processing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Chen94yue/datalog',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    include_package_data=True,  
    package_data={
        'datalog': ['datatype/*.md', 'pipeline/*.py', 'process/*.py', 'utils/*.py', 'datatype/*.py'],
    },
    project_urls={  # 项目相关的更多链接
        'Bug Reports': 'https://github.com/Chen94yue/datalog/issues',
        'Source': 'https://github.com/Chen94yue/datalog',
    },
)
