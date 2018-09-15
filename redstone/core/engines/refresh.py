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
from typing import TYPE_CHECKING

import stomp
from django.conf import settings

from redstone.database.models import RedstoneFeedsModel, RedstoneSpiderModel
from redstone.utils.log import logger
# from ...utils.log import logger
from .base import SingleThreadBaseEngine, EngineStatus

if TYPE_CHECKING:
    from redstone.core.application import RedstoneApplication


class RefreshEngine(SingleThreadBaseEngine):

    def __init__(self, in_queue, out_queue, app_ctx):
        super(RefreshEngine, self).__init__(in_queue=in_queue, out_queue=out_queue)
        self.name = "RefreshEngine"
        # 为了重新指定一下lint
        self._out_queue: stomp.StompConnection11 = out_queue

        self.app_ctx: RedstoneApplication = app_ctx

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

                    try:
                        # 获取该feed使用的spider名称
                        sp = RedstoneSpiderModel.objects.filter(is_deleted=0, pk=_feed.spider_type).first()
                        if not sp:
                            logger.error("Can't get (name: {}, id: {}) spider info!".format(_feed.name, _feed.id))
                            # TODO: 考虑将feed的状态设置为失效
                            continue

                        # 将需要刷新的任务封装成指定的格式
                        task = {
                            "feed_url": _feed.url,
                            "feed_id": _feed.id,
                            "feed_name": _feed.name,
                            "feed_config": {
                                "use_proxy": _feed.use_proxy
                            },
                            "spider_name": sp.name
                        }

                        task = json.dumps(task)
                        self.put_result_to_queue(task)
                    finally:
                        # 保证一定更新fetch_time字段
                        _feed.fetch_time = current_time
                        _feed.save()

        logger.info("RefreshEngine end!")
