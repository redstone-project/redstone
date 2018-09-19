#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.launcher
    ~~~~~~~~~~~~~~~~~~~~~~

    整个项目的入口启动器

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""
import queue
import stomp

from django.conf import settings

from redstone.core import data as gdata
from .engines import RefreshEngine
from redstone.utils.log import logger


class RedstoneApplication(object):

    class BufferedQueues:
        """
        存放所有的本地buffer queue
        """
        REFRESH_TASK_BUFFER_QUEUE: queue.Queue = None
        SPIDER_RESULT_BUFFER_QUEUE: queue.Queue = None

    class AppEngines:
        """
        存放所有的engines
        """
        REFRESH_ENGINE: RefreshEngine = None

    def __init__(self):
        super(RedstoneApplication, self).__init__()

    def run(self):
        """
        程序真正的入口
        """
        logger.info("redstone application start!")

        # TODO: 初始化keeper

        # 初始化RefreshEngine和它所用的本地buffer queue
        self.BufferedQueues.REFRESH_TASK_BUFFER_QUEUE = queue.Queue()
        self.AppEngines.REFRESH_ENGINE = RefreshEngine(app_ctx=self)

