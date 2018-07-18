#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.mongo
    ~~~~~~~~~~~~~~~~~~~~~~~

    连接mongo数据库

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.conf import settings
from mongoengine import connect


def connect_mongo():
    connect(
        db=settings.MONGO_DB,
        host=settings.MONGO_HOST,
        username=settings.MONGO_USER,
        password=settings.MONGO_PASSWORD
    )
