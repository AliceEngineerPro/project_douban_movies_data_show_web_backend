# coding: utf8
""" 
@File: Config.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 3:10
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR_2 = os.path.dirname(os.path.realpath(__name__))
# RUN_ENV Option: DevelopmentConfig, ProductionConfig; if other RUN_ENV is DefaultConfig
RUN_ENV = 'DevelopmentConfig'
# RUN_ENV = ''

class DefaultConfig(object):
    __version = '1.0.0_Beta'
    
    
class DevelopmentConfig(DefaultConfig):
    __version = '1.0.0_Dev'
    MYSQL_HOST = '10.31.102.2'
    MYSQL_PORT = 13306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DATABASE = 'tb_douban_movies'
    MYSQL_CHARSET = ''
    
    
class ProductionConfig(DefaultConfig):
    __version = '1.0.0_Releases'

if RUN_ENV == 'DevelopmentConfig':
    RUN_ENV = DevelopmentConfig()
elif RUN_ENV == 'ProductionConfig':
    RUN_ENV = ProductionConfig()
else:
    RUN_ENV = DefaultConfig()
if RUN_ENV.MYSQL_CHARSET == '':
    RUN_ENV.MYSQL_CHARSET = 'utf8'
