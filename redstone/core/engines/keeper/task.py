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

from ..base import SingleThreadBaseEngine, EngineStatus


if typing.TYPE_CHECKING:
    from redstone.core.application import RedstoneApplication


class TaskKeeper(SingleThreadBaseEngine):
    """
    从TaskBufferQueue中获取任务放到ActiveMQ中
    """
    def __init__(self, app_ctx):
        super(TaskKeeper, self).__init__()
        self.name = "TaskKeeper"
        self.app_ctx: RedstoneApplication = app_ctx

    def start(self):
        # TODO: Connect To ActiveMQ
        super(TaskKeeper, self).start()

    def _worker(self):

        buffer_queue = self.app_ctx.BufferedQueues.REFRESH_TASK_BUFFER_QUEUE

        while self._status == EngineStatus.RUNNING:
            pass
