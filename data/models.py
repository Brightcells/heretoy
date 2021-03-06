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
    ('gravity', u'重力感应'),
)


SCREEN = (
    ('horizontal', u'横屏'),
    ('vertical', u'竖屏'),
)


LUNBOTU_CLASSIFY = (
    ('new', u'最新'),
    ('hot', u'最热'),
    ('both', u'最热&最新'),
)


AUDIT = (
    ('audit_ing', _(u'audit_ing')),
    ('audit_done', _(u'audit_done')),
    ('audit_reject', _(u'audit_reject')),
)


class TestTokenInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'测试 Token')
    status = models.BooleanField(_(u'status'), default=True, help_text=u'Token 状态')

    class Meta:
        verbose_name = _('testtokeninfo')
        verbose_name_plural = _('testtokeninfo')

    def __unicode__(self):
        return u'{0.token}'.format(self)


class Html5GamesClassifyInfo(CreateUpdateMixin):
    first = models.CharField(_(u'1st'), max_length=255, blank=True, null=True, help_text=u'一级分类')
    second = models.CharField(_(u'2nd'), max_length=255, blank=True, null=True, help_text=u'二级分类')

    class Meta:
        verbose_name = _('html5gamesclassifyinfo')
        verbose_name_plural = _('html5gamesclassifyinfo')

    def __unicode__(self):
        return u'{0.first} > {0.second}'.format(self)


class Html5GamesInfo(CreateUpdateMixin):
    name = models.CharField(_(u'name'), max_length=255, blank=True, null=True, help_text=u'游戏名称')
    md5 = models.CharField(_(u'md5'), max_length=255, blank=True, null=True, help_text=u'首次 pk + 游戏名称 的 md5')
    image = models.ImageField(_(u'image'), upload_to=upload_path, blank=True, null=True, help_text=u'游戏 Logo')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'游戏描述')
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'游戏链接')
    share_url = models.CharField(_(u'share_url'), max_length=255, blank=True, null=True, help_text=u'游戏分享链接')
    play = models.IntegerField(_(u'play'), default=0, help_text=u'游戏玩数')
    real_play = models.IntegerField(_(u'real_play'), default=0, help_text=u'真实游戏玩数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'游戏赞数')
    real_like = models.IntegerField(_(u'real_like'), default=0, help_text=u'真实游戏赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'游戏踩数')
    nail = models.IntegerField(_(u'nail'), default=0, help_text=u'游戏固定数')
    real_nail = models.IntegerField(_(u'real_nail'), default=0, help_text=u'真实游戏固定数')
    favorite = models.IntegerField(_(u'favorite'), default=0, help_text=u'游戏收藏数')
    real_favorite = models.IntegerField(_(u'real_favorite'), default=0, help_text=u'真实游戏收藏数')
    classify1 = models.ForeignKey(Html5GamesClassifyInfo, verbose_name=_(u'classify1'), blank=True, null=True, related_name='classify1', help_text='分类 - 1')
    classify2 = models.ForeignKey(Html5GamesClassifyInfo, verbose_name=_(u'classify2'), blank=True, null=True, related_name='classify2', help_text='分类 - 2')
    source = models.CharField(_(u'source'), max_length=255, blank=True, null=True, help_text=u'游戏来源')
    version = models.CharField(_(u'version'), max_length=255, blank=True, null=True, help_text=u'游戏版本')
    commit = models.CharField(_(u'commit'), max_length=255, blank=True, null=True, help_text=u'游戏备注')
    language = models.CharField(_(u'language'), max_length=255, choices=LANGUAGE_CODE, blank=True, null=True, help_text=u'游戏语言')
    operate = models.CharField(_(u'operate'), max_length=255, choices=OPERATE, blank=True, null=True, help_text=u'游戏操作')
    screen = models.CharField(_(u'screen'), max_length=255, choices=SCREEN, default='vertical', blank=True, null=True, help_text=u'游戏横竖屏')
    status = models.BooleanField(_(u'status'), default=True, help_text=u'游戏是否显示')
    onshalf = models.CharField(_(u'onshalf'), max_length=255, choices=ONSHALF, default='test', blank=True, null=True, help_text=u'游戏是否上架')
    sole = models.BooleanField(_(u'sole'), default=False, help_text=u'游戏是否独家')
    first_publish = models.BooleanField(_(u'first_publish'), default=False, help_text=u'游戏是否首发')
    boutique = models.BooleanField(_(u'boutique'), default=False, help_text=u'游戏是否精品')
    developer = models.CharField(_(u'developer'), max_length=255, blank=True, null=True, help_text=u'游戏开发者')
    submit_at = models.DateTimeField(_(u'submit_at'), blank=True, null=True, help_text=u'游戏提交时间')
    audit = models.CharField(_(u'audit'), max_length=255, choices=AUDIT, default='audit_ing', blank=True, null=True, help_text=u'游戏审核状态')
    reject_reason = models.TextField(_(u'reject_reason'), blank=True, null=True, help_text=u'游戏驳回原因')

    class Meta:
        verbose_name = _('html5gamesinfo')
        verbose_name_plural = _('html5gamesinfo')

    def __unicode__(self):
        return u'{0.name}'.format(self)

    def _data(self):
        return {
            'pk': self.md5,
            'name': self.name,
            'image': settings.DOMAIN + self.image.url if self.image else settings.APP_DEFAULT_LOGO,
            'descr': self.descr,
            'url': self.url,
            'share_url': self.share_url,
            'play': self.play,
            'like': self.like,
            'unlike': self.unlike,
            'source': self.source,
            'screen': self.screen,
            'sole': self.sole,
            'first_publish': self.first_publish,
            'boutique': self.boutique,
        }

    def _info(self):
        return {
            'pk': self.md5,
            'name': self.name,
            'image': settings.DOMAIN + self.image.url if self.image else settings.APP_DEFAULT_LOGO,
            'descr': self.descr,
            'url': self.url,
            'share_url': self.share_url,
            'play': self.play,
            'like': self.like,
            'unlike': self.unlike,
            'source': self.source,
            'screen': self.screen,
            'sole': self.sole,
            'first_publish': self.first_publish,
            'boutique': self.boutique,
            'version': self.version,
            'submit_at': self.submit_at,
            'audit': self.audit,
        }

    data = property(_data)
    info = property(_info)


class Html5GamesPlayInfo(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_play', help_text='Html5 Game')
    play = models.IntegerField(_(u'play'), default=1, help_text=u'游戏玩数')
    nail = models.BooleanField(_(u'nail'), default=False, help_text=u'游戏是否固定')
    favorite = models.BooleanField(_(u'favorite'), default=False, help_text=u'游戏是否收藏')

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
            'nail': self.nail,
            'favorite': self.favorite,
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


class Html5GamesNailLog(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_nail_log', help_text='Html5 Game')
    nail = models.BooleanField(_(u'nail'), default=False, help_text=u'游戏是否固定')

    class Meta:
        verbose_name = _('html5gamesnaillog')
        verbose_name_plural = _('html5gamesnaillog')

    def __unicode__(self):
        return u'{0.token}'.format(self)


class Html5GamesFavoriteLog(CreateUpdateMixin):
    token = models.CharField(_(u'token'), max_length=255, blank=True, null=True, help_text=u'用户唯一标示码')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_favorite_log', help_text='Html5 Game')
    favorite = models.BooleanField(_(u'favorite'), default=False, help_text=u'游戏是否收藏')

    class Meta:
        verbose_name = _('html5gamesfavoritelog')
        verbose_name_plural = _('html5gamesfavoritelog')

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


class TopicInfo(CreateUpdateMixin):
    tp = models.CharField(_(u'tp'), max_length=255, blank=True, null=True, help_text=u'专题标识')
    name = models.CharField(_(u'name'), max_length=255, blank=True, null=True, help_text=u'专题名称')
    status = models.BooleanField(_(u'status'), default=True, help_text=u'专题状态')

    class Meta:
        verbose_name = _('topicinfo')
        verbose_name_plural = _('topicinfo')

    def __unicode__(self):
        return u'{0.name}'.format(self)


class TopicGamesInfo(CreateUpdateMixin):
    topic = models.ForeignKey(TopicInfo, verbose_name=_(u'topic'), blank=True, null=True, related_name='h5game_topic', help_text='Html5 Topic')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_topicgame', help_text='Html5 Game')
    status = models.BooleanField(_(u'status'), default=True, help_text=u'专题游戏状态')

    class Meta:
        verbose_name = _('topicgamesinfo')
        verbose_name_plural = _('topicgamesinfo')

    def __unicode__(self):
        return u'{0.topic}'.format(self)


class LunbotuInfo(CreateUpdateMixin):
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'轮播图标题')
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'轮播图链接')
    share_url = models.CharField(_(u'share_url'), max_length=255, blank=True, null=True, help_text=u'轮播图分享链接')
    image = models.ImageField(_(u'image'), upload_to=upload_path, blank=True, null=True, help_text=u'轮播图图片')
    sort = models.IntegerField(_(u'sort'), default=0, help_text=u'轮播图类型：0 for 游戏推送，1 for 游戏集合，2 for 广告')
    h5game = models.ForeignKey(Html5GamesInfo, verbose_name=_(u'h5game'), blank=True, null=True, related_name='h5game_lubotugame', help_text='Html5 Game')
    lbt_classify = models.CharField(_(u'lbt_classify'), max_length=255, choices=LUNBOTU_CLASSIFY, default='new', blank=True, null=True, help_text=u'轮播图类别')
    status = models.BooleanField(_(u'status'), default=True, help_text=u'轮播图状态')
    onshalf = models.CharField(_(u'onshalf'), max_length=255, choices=ONSHALF, default='test', blank=True, null=True, help_text=u'轮播图是否上架')

    class Meta:
        verbose_name = _('lunbotuinfo')
        verbose_name_plural = _('lunbotuinfo')

    def __unicode__(self):
        return u'{0.title}'.format(self)

    def _data(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'url': self.url,
            'share_url': self.share_url,
            'image': settings.DOMAIN + self.image.url if self.image else '',
            'sort': self.sort,
            'h5game': self.h5game,
        }

    data = property(_data)
