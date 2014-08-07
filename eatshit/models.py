#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from heretoy.basemodels import CreateUpdateMixin

import os
import time
import datetime


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'heretoy/image/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


class PhotoInfo(CreateUpdateMixin):
    image = models.ImageField(_('image'), upload_to=upload_path, blank=True, null=True, help_text=u'好友照片')
    name = models.CharField(_('name'), max_length=255, blank=True, null=True, help_text=u'好友名称')
    ip_addr = models.CharField(_('ip_addr'), max_length=255, blank=True, null=True, help_text=u'照片上传IP')
    status = models.BooleanField(_('status'), default=True, help_text=u'图片是否显示')

    class Meta:
        verbose_name = _('photoinfo')
        verbose_name_plural = _('photoinfo')

    def __unicode__(self):
        return u'{0.name}'.format(self)

    def _data(self):
        return {
            'pk': self.pk,
            'image': self.image.url if self.image else '',
            'name': self.name
        }

    data = property(_data)
