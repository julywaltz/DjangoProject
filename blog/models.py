#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-11-05 22:13:52
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-11-05 22:29:45
# @Email: julywaltz77@hotmail.com

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_data = timezone.now
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
