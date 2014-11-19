#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _, ugettext

from heretoy.basemodels import CreateUpdateMixin


DEV_TYPE = (
    ('company', u'公司'),
    ('team', u'团队'),
    ('person', u'个人'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    class Meta:
        verbose_name = _(u'profile')
        verbose_name_plural = _(u'profile')

    def __unicode__(self):
        return u'{0.user.username}'.format(self)


class Developer(CreateUpdateMixin):
    profile = models.OneToOneField(Profile, related_name='developer')
    devtype = models.CharField(_(u'devtype'), max_length=255, choices=DEV_TYPE, blank=True, null=True, help_text=u'开发者类型')
    com_tem_per = models.CharField(_(u'com_tem_per'), max_length=255, blank=True, null=True, help_text=u'公司/团队/个人名称')
    contact = models.CharField(_(u'contact'), max_length=255, blank=True, null=True, help_text=u'联系人')
    mobile = models.CharField(_(u'mobile'), max_length=255, blank=True, null=True, help_text=u'联系电话')

    def __unicode__(self):
        return u'{0.profile.user.username}'.format(self)
