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
    title: 爬虫的名称，用于识别每个爬虫的作用，供用户阅读
    spider_name: 爬虫的正式名称，如果没有提供用于将其转换为filename和pkg name；
                 转换规则：
                 SpiderName: ExampleSpider
                        => Pkg name: example_spider
                        => Filename: example_spider.py
    filename: TODO 自动生成，后期支持自定义
    class_name: TODO 自动生成，后期支持自定义
    """
    class Meta:
        db_table = "rs_spider"

    title = models.CharField(max_length=128, null=False, default="Default Spider")
    spider_name = models.CharField(max_length=128, null=False, default="SpiderName", db_index=True)
    filename = models.CharField(max_length=256, null=False, default="default_rss.py")
    class_name = models.CharField(max_length=256, null=False, default="DefaultRSSClassName")

    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
