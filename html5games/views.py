# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from data.models import Html5GamesInfo, Html5GamesPlayInfo, TopicInfo, TopicGamesInfo

from CodeConvert import CodeConvert

import os
import time
import urllib
import random
import datetime


PLAY = settings.PLAY_NUM_PER_CLICK


def game(request):
    rank_type = request.GET.get('type', 'new')

    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP

    domain = settings.DOMAIN

    allh5games = Html5GamesInfo.objects.filter(status=True, onshalf='on')

    h5games = allh5games.order_by('-play', '-like', 'unlike')[:10]
    hots = [h5.data for h5 in h5games]

    h5games = allh5games.order_by('-create_at')[:10]
    news = [h5.data for h5 in h5games]

    return render(request, 'html5games/game.html', dict(rank_type=rank_type, hots=hots, news=news, domain=domain, fromApple=fromApple, app_url=app_url))


def topic(request, tp=''):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP

    domain = settings.DOMAIN

    try:
        topic = TopicInfo.objects.get(tp=tp).name
    except:
        topic = ''

    h5games = TopicGamesInfo.objects.filter(topic__tp=tp, status=True).order_by('-h5game__play', '-h5game__like', 'h5game__unlike')
    h5games = [h5.h5game.data for h5 in h5games]

    return render(request, 'html5games/topic.html', dict(topic=topic, h5games=h5games, domain=domain, fromApple=fromApple, app_url=app_url))


def play(request, pk=-1):
    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
    except:
        h5game = ''
    return render(request, 'html5games/play.html', dict(h5game=h5game))


@xframe_options_exempt
def share(request, pk=-1):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += random.randint(5, 10)
        h5game.real_play += 1
        h5game.save()
        h5game = h5game.data
    except:
        h5game = ''

    if request.mobile:
        app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP
        return render(request, 'html5games/wap_share.html', dict(h5game=h5game, domain=domain, fromApple=fromApple, app_url=app_url))
    else:
        app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_PC
        return render(request, 'html5games/pc_share.html', dict(h5game=h5game, domain=domain, fromApple=fromApple, app_url=app_url))


@xframe_options_exempt
def wap_share(request, pk=-1):
    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
        h5game = h5game.data
    except:
        h5game = ''
    return render(request, 'html5games/wap_share.html', dict(h5game=h5game, domain=domain))


@xframe_options_exempt
def pc_share(request, pk=-1):
    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
        h5game = h5game.data
    except:
        h5game = ''
    return render(request, 'html5games/pc_share.html', dict(h5game=h5game, domain=domain))


def home(request):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    domain = settings.DOMAIN

    if request.mobile:
        app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP
        return render(request, 'html5games/wap_home.html', dict(domain=domain, fromApple=fromApple, app_url=app_url))
    else:
        app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_PC
        return render(request, 'html5games/pc_home.html', dict(domain=domain, fromApple=fromApple, app_url=app_url))


def wap_home(request):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_PC

    domain = settings.DOMAIN

    return render(request, 'html5games/wap_home.html', dict(domain=domain, fromApple=fromApple, app_url=app_url))
