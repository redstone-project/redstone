#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.engines.base
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    基础引擎，所有engine的父类，提供固定的接口

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

import multiprocessing
import queue
import threading
from typing import Union, List, TYPE_CHECKING

import abc

if TYPE_CHECKING:
    from redstone.core.application import RedstoneApplication


class EngineStatus:
    # TODO: 使用dataclass替换该类
    READY = 0x00
    RUNNING = 0x01
    STOP = 0x02


class SingleThreadBaseEngine(object, metaclass=abc.ABCMeta):
    """
    单线程的基础类
    """

    def __init__(self):
        super(SingleThreadBaseEngine, self).__init__()

        # 引擎的名称
        self.name = "SingleThreadEngine"

        # 工作线程
        self.thread: threading.Thread = None

        # 引擎状态
        self._status = EngineStatus.READY

        # 工作标志
        self._ev: threading.Event = threading.Event()

        # app的上下文
        self.app_ctx: RedstoneApplication = None

    def start(self):
        self._status = EngineStatus.RUNNING
        self.thread = threading.Thread(target=self._worker, name=self.name)
        self.thread.start()

    def stop(self):
        self._status = EngineStatus.STOP
        self._ev.set()

    def is_alive(self):
        return self.thread.is_alive()

    @abc.abstractmethod
    def _worker(self):
        pass


class MultiThreadBaseEngine(object, metaclass=abc.ABCMeta):
    def __init__(self, pool_size=None):
        """
        多线程引擎的基类
        :param pool_size: 线程池的大小
        """
        super(MultiThreadBaseEngine, self).__init__()

        # 引擎名称
        self.name = "MultiThreadEngine"

        # 线程池
        self.thread_pool: List[threading.Thread] = []

        # 线程池大小
        self.pool_size = pool_size if pool_size else multiprocessing.cpu_count() * 2 + 1

        # 引擎状态
        self._status = EngineStatus.READY

        # 工作标志
        self._ev = threading.Event = threading.Event()

    def start(self):
        self._status = EngineStatus.RUNNING
        self.thread_pool = [
            threading.Thread(target=self._worker, name="{}-{}".format(self.name, idx)) for idx in range(self.pool_size)
        ]
        _ = [_thread.start() for _thread in self.thread_pool]

    def stop(self):
        self._status = EngineStatus.STOP
        self._ev.set()

    def is_alive(self):
        return any([x.is_alive() for x in self.thread_pool])

    @abc.abstractmethod
    def _worker(self):
        pass
