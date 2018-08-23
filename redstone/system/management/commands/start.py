#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.system.management.commands.start
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    CLI的启动入口点，通过调用redstone.core.launcher中的方法启动

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.core.management.base import BaseCommand, CommandError

from redstone.core.launcher import RedstoneApplication
from redstone.core import data


class Command(BaseCommand):

    AVAILABLE_OPTS = [
        "spider_mode", "server_mode"
    ]

    def add_arguments(self, parser):
        parser.add_argument(
            "--spider", action="store_true", dest="spider_mode", help="Run redstone in 'spider' mode."
        )
        parser.add_argument(
            "--server", action="store_true", dest="server_mode", help="Run redstone in 'server' mode."
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Starting Redstone application...")
        )

        # 检查启动参数
        if not any([options.get(opt) for opt in self.AVAILABLE_OPTS]):
            raise CommandError("Must start at least one service!")

        if all([options.get(opt) for opt in self.AVAILABLE_OPTS]):
            raise CommandError("Only one service can be started!")

        # 启动模式
        mode = "spider"
        if options.get("spider_mode"):
            mode = "spider"
        elif options.get("server_mode"):
            mode = "server"

        try:
            # 调用launcher中的方法启动整个程序
            data.REDSTONE_APP = RedstoneApplication(mode)
            data.REDSTONE_APP.run()
        except Exception as e:
            self.stdout.write(
                self.style.ERROR("Un-handled exception happened. Exception: {}".format(e))
            )
            import sys
            import traceback
            exc_type, exc_value, exc_tb = sys.exc_info()
            tbe = traceback.TracebackException(exc_type, exc_value, exc_tb)
            full_err = ''.join(tbe.format())
            self.stdout.write("Full call stack information below:\n {}".format(full_err))
