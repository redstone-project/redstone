#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.config.dev
    ~~~~~~~~~~~~~~~~~~~

    DEV配置

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

DEBUG = True
SECRET_KEY = '0q289aidfa23-098rawd#vajeifj'

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

EXTRA_INSTALLED_APPS = [

]

EXTRA_MIDDLEWARE = [

]

# MySQL连接配置
DATABASE_NAME = "redstone"
DATABASE_USER = "root"
DATABASE_PASSWORD = "123!@#"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "3306"
DATABASE_OPTIONS = {
    'init_command': 'SET default_storage_engine=INNODB;SET NAMES utf8mb4',
    'charset': 'utf8mb4',
}

# mongodb连接配置
MONGO_HOST = "﻿"
MONGO_PORT = "27017"
MONGO_DB = "redstone"
MONGO_USER = "redstone"
MONGO_PASSWORD = "123456"
