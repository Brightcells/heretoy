#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from heretoy.basemodels import CreateUpdateMixin

import os
import rsa
import time
import urllib
import datetime

from pyDes import *


RSA = settings.RSA_VALUES
BOB_PUB = rsa.PublicKey(RSA['n'], RSA['e'])
BOB_PRIV = rsa.PrivateKey(RSA['n'], RSA['e'], RSA['d'], RSA['p'], RSA['q'])

k = des('DIORSLAB', CBC, '\0\0\0\0\0\0\0\0', pad=None, padmode=PAD_PKCS5)


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'data/image/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


LANGUAGE_CODE = (
    ('zh-cn', u'中文'),
    ('en', u'英文'),
    ('zh-cn_en', u'中英文'),
)


ONSHALF = (
    ('on', u'上架'),
    ('off', u'下架'),
    ('test', u'测试'),
)


OPERATE = (
    ('single', u'单手'),
    ('double', u'双手'),
)


class TestTokenInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'测试 Token')
    status = models.BooleanField(_('status'), default=True, help_text=u'Token 状态')

    class Meta:
        verbose_name = _('testtokeninfo')
        verbose_name_plural = _('testtokeninfo')

    def __unicode__(self):
        return u'{0.token}'.format(self)


class Html5GamesClassifyInfo(CreateUpdateMixin):
    first = models.CharField(_('1st'), max_length=255, blank=True, null=True, help_text=u'一级分类')
    second = models.CharField(_('2nd'), max_length=255, blank=True, null=True, help_text=u'二级分类')

    class Meta:
        verbose_name = _('html5gamesclassifyinfo')
        verbose_name_plural = _('html5gamesclassifyinfo')

    def __unicode__(self):
        return u'{0.first} > {0.second}'.format(self)


class Html5GamesInfo(CreateUpdateMixin):
    name = models.CharField(_('name'), max_length=255, blank=True, null=True, help_text=u'游戏名称')
    md5 = models.CharField(_('md5'), max_length=255, blank=True, null=True, help_text=u'首次 pk + 游戏名称 的 md5')
    image = models.ImageField(_('image'), upload_to=upload_path, blank=True, null=True, help_text=u'游戏 Logo')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'游戏描述')
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'游戏链接')
    play = models.IntegerField(_(u'play'), default=0, help_text=u'游戏玩数')
    real_play = models.IntegerField(_(u'real_play'), default=0, help_text=u'真实游戏玩数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'游戏赞数')
    real_like = models.IntegerField(_(u'real_like'), default=0, help_text=u'真实游戏赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'游戏踩数')
    classify1 = models.ForeignKey(Html5GamesClassifyInfo, verbose_name=_(u'classify1'), blank=True, null=True, related_name='classify1', help_text='分类 - 1')
    classify2 = models.ForeignKey(Html5GamesClassifyInfo, verbose_name=_(u'classify2'), blank=True, null=True, related_name='classify2', help_text='分类 - 2')
    source = models.CharField(_(u'source'), max_length=255, blank=True, null=True, help_text=u'游戏来源')
    version = models.CharField(_(u'version'), max_length=255, blank=True, null=True, help_text=u'游戏版本')
    commit = models.CharField(_(u'commit'), max_length=255, blank=True, null=True, help_text=u'游戏备注')
    language = models.CharField(_(u'language'), max_length=255, choices=LANGUAGE_CODE, blank=True, null=True, help_text=u'游戏语言')
    operate = models.CharField(_(u'operate'), max_length=255, choices=OPERATE, blank=True, null=True, help_text=u'游戏操作')
    status = models.BooleanField(_('status'), default=True, help_text=u'游戏是否显示')
    onshalf = models.CharField(_(u'onshalf'), max_length=255, choices=ONSHALF, default='test', blank=True, null=True, help_text=u'游戏是否上架')

    class Meta:
        verbose_name = _('html5gamesinfo')
        verbose_name_plural = _('html5gamesinfo')

    def __unicode__(self):
        return u'{0.name}'.format(self)

    def _data(self):
        return {
            'pk': self.md5,
            'name': self.name,
            'image': self.image.url if self.image else '',
            'descr': self.descr,
            'url': self.url,
            'play': self.play,
            'like': self.like,
            'unlike': self.unlike,
        }

    def _info(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'image': settings.DOMAIN + self.image.url if self.image else '',
            'descr': self.descr,
            'url': self.url,
            'play': self.play,
            'like': self.like,
            'unlike': self.unlike,
        }

    data = property(_data)
    info = property(_info)


class Html5GamesPlayInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_play', help_text='Html5 Game')
    play = models.IntegerField(_(u'play'), default=1, help_text=u'游戏玩数')

    class Meta:
        verbose_name = _('html5gamesplayinfo')
        verbose_name_plural = _('html5gamesplayinfo')

    def __unicode__(self):
        return u'{0.token}'.format(self)

    def _data(self):
        return {
            'pk': self.h5game.pk,
            'name': self.h5game.name,
            'image': settings.DOMAIN + self.h5game.image.url if self.h5game.image else '',
            'descr': self.h5game.descr,
            'url': self.h5game.url,
            'play': self.h5game.play,
            'like': self.h5game.like,
            'unlike': self.h5game.unlike,
            'myplay': self.play,
        }

    data = property(_data)


class Html5GamesPlayLog(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_play_log', help_text='Html5 Game')

    class Meta:
        verbose_name = _('html5gamesplaylog')
        verbose_name_plural = _('html5gamesplaylog')

    def __unicode__(self):
        return u'{0.token}'.format(self)


class Html5GamesLikeInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_like', help_text='Html5 Game')

    class Meta:
        verbose_name = _('html5gameslikeinfo')
        verbose_name_plural = _('html5gameslikeinfo')

    def __unicode__(self):
        return u'{0.token}'.format(self)


class Html5GamesUnlikeInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_unlike', help_text='Html5 Game')

    class Meta:
        verbose_name = _('html5gamesunlikeinfo')
        verbose_name_plural = _('html5gamesunlikeinfo')

    def __unicode__(self):
        return u'{0.token}'.format(self)
