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
import abc
import queue
import threading
from typing import Union

try:
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class EngineStatus:
        READY = 0x00
        RUNNING = 0x01
        STOP = 0x02
except ImportError:
    class EngineStatus:
        READY = 0x00
        RUNNING = 0x01
        STOP = 0x02


class STBaseEngine(object, metaclass=abc.ABCMeta):
    """
    单线程的基础类
    """

    def __init__(self, in_queue, out_queue):
        """
        :param in_queue: 输入队列
        :param out_queue: 输出队列
        """
        super(STBaseEngine, self).__init__()

        # 引擎的名称
        self.name = "SingleThreadEngine"

        # 工作线程
        self.thread: threading.Thread = None

        # 引擎状态
        self._status = EngineStatus.READY

        # 工作标志
        self._ev: threading.Event = threading.Event()

        # 输入、输出队列
        self._in_queue: Union[queue.Queue, queue.PriorityQueue] = None
        self._out_queue: Union[queue.Queue, queue.PriorityQueue] = None

    def start(self):
        self.thread = threading.Thread(target=self._worker, name=self.name)
        self.thread.start()

    def stop(self, force=True):
        def _stop():
            self._status = EngineStatus.STOP
            self._ev.set()
        if force:
            _stop()
        else:
            while True:
                if self._in_queue.empty():
                    _stop()
                else:
                    self._ev.wait(1)
                    continue

    def is_alive(self):
        return self.thread.is_alive()

    def get_task_from_queue(self, timeout=1):
        """
        从输入队列中获取任务
        :param timeout: 超时时间，默认为1s
        :return: task
        """
        while True:
            try:
                task = self._in_queue.get(block=False)
                return task
            except queue.Empty:
                self._ev.wait(timeout)
                continue

    def put_result_to_queue(self, result, timeout=1):
        """
        向输出队列中放置结果
        :param timeout: 超时时间，默认为1s
        :param result: 需要放到队列中的结果
        :return:
        """
        while True:
            try:
                self._out_queue.put(result, block=False)
                return True
            except queue.Full:
                self._ev.wait(timeout)
                continue

    @abc.abstractmethod
    def _worker(self):
        pass
