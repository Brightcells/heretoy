#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


class CreateUpdateMixin(models.Model):
    create_at = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True)  # 添加时间
    modify_at = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True)  # 修改时间

    class Meta:
        abstract = True
