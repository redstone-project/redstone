#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.engines.spider
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    爬虫引擎
        - 从队列中获取需要刷新的源
        - 产生任务放到thread pool中处理

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from .base import MTBaseEngine


class SpiderEngine(MTBaseEngine):
    def __init__(self):
        super(SpiderEngine, self).__init__()

