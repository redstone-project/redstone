#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.database.models.article
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    记录爬取到的RSS文章

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

from django.db import models


class RedstoneArticleModel(models.Model):
    """
    :title: 文章的标题
    :url: 文章的原始URL
    :content: 文章内容
    :publish_time: 文章发布时间
    :up_vote: 点赞
    :down_vote: 踩
    """

    class Meta:
        db_table = "rs_article"

    title = models.CharField(max_length=128, null=False, default="ArticleTitle")
    url = models.CharField(max_length=1024, null=False, default="ArticleURL")
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True, null=False)
    up_vote = models.PositiveIntegerField(default=0)
    down_vote = models.PositiveIntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)
