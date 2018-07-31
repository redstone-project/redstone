#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.data
    ~~~~~~~~~~~~~~~~~~

    全局数据存储点

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""
import queue

from django.conf import settings

from .engines import RefreshEngine

# 项目基础路径
BASE_DIR = settings.BASE_DIR

# 全局保存的应用实例
REDSTONE_APP = None

# 存储刷新任务的任务队列
REFRESH_TASK_QUEUE: queue.Queue = None
REFRESH_ENGINE: RefreshEngine = None
