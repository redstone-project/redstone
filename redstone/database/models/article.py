#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.models.article
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    记录爬取到的RSS文章
    文章的实际内容存储在mongodb中

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

import datetime

from mongoengine import Document, StringField, DateTimeField, BooleanField, IntField


NOW = datetime.datetime.now


class RedstoneArticleModel(Document):
    """
    :title: 文章的标题
    :url: 文章的原始URL
    :content: 文章内容
    :publish_time: 文章发布时间
    :up_vote: 点赞
    :down_vote: 踩
    """

    meta = {"collection": "rs_article"}

    title = StringField(required=True)
    url = StringField(required=True)
    content = StringField(required=True)
    publish_time = DateTimeField(required=True, default=NOW)
    up_vote = IntField(required=True, default=0)
    down_vote = IntField(required=True, default=0)

    created_time = DateTimeField(required=True, default=NOW)
    updated_time = DateTimeField(required=True, default=NOW)
    is_deleted = BooleanField(required=True, default=False)
