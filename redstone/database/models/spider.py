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
    class Meta:
        db_table = "rs_spider"


