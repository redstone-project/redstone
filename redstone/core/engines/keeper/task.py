#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

    ~~~~~~~~~~~~~~~~~~


    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

import typing

import stomp

from ..base import SingleThreadBaseEngine, EngineStatus


if typing.TYPE_CHECKING:
    from redstone.core.application import RedstoneApplication


class TaskKeeper(SingleThreadBaseEngine):
    """
    从TaskBufferQueue中获取任务放到ActiveMQ中
    """
    def __init__(self, app_ctx, activemq_info: dict):
        super(TaskKeeper, self).__init__()

        # engine name
        self.name = "TaskKeeper"

        # Application context
        self.app_ctx: RedstoneApplication = app_ctx

        # 队列信息，后面要靠rc项目通用化
        self.activemq_info: dict = activemq_info

        # activemq
        self.activemq_queue = None

    def connect_activemq(self):
        host_info = self.activemq_info.pop("host_info")
        username = self.activemq_info.pop("username")
        password = self.activemq_info.pop("password")
        queue_name = self.activemq_info.pop("queue_name")

        self.activemq_queue = stomp.Connection([host_info])
        self.activemq_queue.connect()

    def start(self):
        # TODO: Connect To ActiveMQ
        self.connect_activemq()
        super(TaskKeeper, self).start()

    def _worker(self):

        buffer_queue = self.app_ctx.BufferedQueues.REFRESH_TASK_BUFFER_QUEUE

        while self._status == EngineStatus.RUNNING:
            pass
