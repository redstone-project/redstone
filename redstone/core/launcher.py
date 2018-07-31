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

from redstone.utils.log import logger
from . import data
from .engines import RefreshEngine


class RedstoneApplication(object):

    def __init__(self):
        super(RedstoneApplication, self).__init__()

    @staticmethod
    def _init_queue():
        """
        初始化应用中用到的队列
        """
        data.REFRESH_TASK_QUEUE = queue.Queue(10240)

    def run(self):
        """
        程序真正的入口
        """
        logger.info("redstone application start!")
        self._init_queue()

        # 启动refresh engine
        data.REFRESH_ENGINE = RefreshEngine()
        data.REFRESH_ENGINE.start()
