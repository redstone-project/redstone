#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.engines.refresh
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    查看数据库中的哪些RSS源需要刷新了，将其放置到任务队列中

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""
import datetime
import json

import stomp
from django.conf import settings

from redstone.utils.log import logger
# from ...utils.log import logger
from .base import STBaseEngine, EngineStatus
from redstone.database.models import RedstoneFeedsModel


class RefreshEngine(STBaseEngine):

    def __init__(self, in_queue, out_queue):
        super(RefreshEngine, self).__init__(in_queue=in_queue, out_queue=out_queue)
        self.name = "RefreshEngine"
        # 为了重新指定一下lint
        self._out_queue: stomp.StompConnection11 = out_queue

    def put_result_to_queue(self, result):
        self._out_queue.send(
            destination="/queue/{}".format(settings.REFRESH_TASK_QUEUE_NAME),
            body=result
        )

    def _worker(self):
        logger.info("RefreshEngine start!")

        while self._status == EngineStatus.RUNNING:

            # 每次读库前等一会
            self._ev.wait(5)

            current_time = datetime.datetime.now()
            rows = RedstoneFeedsModel.objects.filter(is_deleted=0).all()
            for _feed in rows:
                if _feed.fetch_time + datetime.timedelta(minutes=_feed.interval) <= current_time:

                    logger.debug("Detected out-date rss. (ID:%s, Name:%s)", _feed.id, _feed.name)

                    task = {
                        "name": _feed.name,
                        "url": _feed.url,
                        "spider_type": _feed.spider_type
                    }
                    # task = AttribDict()
                    # task.name = _feed.name
                    # task.url = _feed.url
                    # task.spider_type = _feed.spider_type
                    task = json.dumps(task)
                    self.put_result_to_queue(task)

                    _feed.fetch_time = current_time
                    _feed.save()

        logger.info("RefreshEngine end!")
