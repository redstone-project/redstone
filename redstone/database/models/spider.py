#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.models.spider
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    记录爬虫相关的数据模型

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models


class RedstoneSpiderModel(models.Model):
    """
    :name: 爬虫的名称，用于识别每个爬虫的作用
    :filename: 用于导入爬虫类使用，爬虫的类名建议与文件名相同，并且将下划线命名 -> PEP8
    """
    class Meta:
        db_table = "rs_spider"

    name = models.CharField(max_length=128, null=False, default="Default Spider")
    filename = models.CharField(max_length=256, null=False, default="default_rss.py")

    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
