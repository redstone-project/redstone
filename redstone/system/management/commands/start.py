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

from django.core.management.base import BaseCommand

from redstone.core.application import RedstoneApplication
from redstone.core import data


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Starting Redstone application...")
        )

        try:
            # 调用launcher中的方法启动整个程序
            data.REDSTONE_APP = RedstoneApplication()
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
