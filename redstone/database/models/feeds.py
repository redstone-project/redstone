#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.models.feeds
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    存储所有的RSS源信息

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models


class RedstoneFeedsModel(models.Model):
    """
    :name: RSS源名称
    :url: RSS的地址
    :fetch_time: 上次拉取数据的时间
    :interval: 刷新间隔，单位：min，默认每30分钟刷新一次
    :alive_status: 存活状态
        1 - ready，就绪
        2 - alive，存活
        3 - fetching，更新中
        4 - dead，更新失败
    :spider_name: 对应的爬虫ID
    """

    # 定义RSS源的存活状态常量
    ALIVE_STATUS_READY = 0x01
    ALIVE_STATUS_ALIVE = 0x02
    ALIVE_STATUS_FETCHING = 0x03
    ALIVE_STATUS_DEAD = 0x04

    class Meta:
        db_table = "rs_feeds"

    name = models.CharField(max_length=64, default="Default RSS Name", null=False)
    url = models.CharField(max_length=1024, default="", null=False)
    fetch_time = models.DateTimeField(default="", null=False)
    interval = models.IntegerField(default=30, null=False)
    alive_status = models.IntegerField(default=0, null=False)
    spider_type = models.IntegerField(default=0, null=False)
    fail_reason = models.CharField(max_length=512, null=False)

    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
