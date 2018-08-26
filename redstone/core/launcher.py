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

import stomp

from django.conf import settings

from redstone.core import data as gdata
from .engines import RefreshEngine
from redstone.utils.log import logger


class RedstoneApplication(object):

    def __init__(self):
        super(RedstoneApplication, self).__init__()

    @staticmethod
    def _init_queue():
        """
        连接到ActiveMQ的相关队列中
        """
        refresh_task_queue = stomp.Connection([(settings.ACTIVEMQ_HOST, int(settings.ACTIVEMQ_PORT))])
        refresh_task_queue.start()
        refresh_task_queue.connect(settings.ACTIVEMQ_USERNAME, settings.ACTIVEMQ_PASSWORD, wait=True)
        gdata.REFRESH_TASK_QUEUE = refresh_task_queue

    def run(self):
        """
        程序真正的入口
        """
        logger.info("redstone application start!")

        # 连接到ActiveMQ队列
        self._init_queue()

        # 启动refresh engine
        gdata.REFRESH_ENGINE = RefreshEngine(
            in_queue=None, out_queue=gdata.REFRESH_TASK_QUEUE
        )
        gdata.REFRESH_ENGINE.start()
