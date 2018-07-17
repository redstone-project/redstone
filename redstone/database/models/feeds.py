#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.models.feeds
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    存储所有的RSS源信息

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from mongoengine import Document, StringField


class Feeds(Document):
    name = StringField(required=True)
