#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from heretoy.basemodels import CreateUpdateMixin
from accounts.models import Developer

import os
import time
import urllib
import datetime


class OpenidInfo(CreateUpdateMixin):
    openid = models.CharField(_(u'openid'), max_length=255, blank=True, null=True, help_text=u'Openid')
    count = models.IntegerField(_(u'count'), default=1, help_text=u'抽奖次数')
    refer = models.IntegerField(_(u'refer'), default=0, help_text=u'Refer次数')
    status = models.BooleanField(_('status'), default=True, help_text=u'Openid状态')

    class Meta:
        verbose_name = _('openidinfo')
        verbose_name_plural = _('openidinfo')


class CashInfo(CreateUpdateMixin):
    cash = models.CharField(_(u'cash'), max_length=255, blank=True, null=True, help_text=u'Cash')
    num = models.IntegerField(_(u'cash_num'), default=0, help_text=u'代金券数额')
    status = models.BooleanField(_('status'), default=True, help_text=u'Cash状态')

    class Meta:
        verbose_name = _('cashinfo')
        verbose_name_plural = _('cashinfo')


class PrizeInfo(CreateUpdateMixin):
    openid = models.CharField(_(u'openid'), max_length=255, blank=True, null=True, help_text=u'Openid')
    phone = models.CharField(_(u'phone'), max_length=255, blank=True, null=True, help_text=u'Phone')
    cash = models.CharField(_(u'cash'), max_length=255, blank=True, null=True, help_text=u'Cash')
    num = models.IntegerField(_(u'cash_num'), default=0, help_text=u'代金券数额')
    status = models.BooleanField(_('status'), default=True, help_text=u'Cash状态')

    class Meta:
        verbose_name = _('prizeinfo')
        verbose_name_plural = _('prizeinfo')
