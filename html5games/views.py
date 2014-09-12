# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from data.models import Html5GamesInfo, Html5GamesPlayInfo

from CodeConvert import CodeConvert

import os
import time
import urllib
import datetime


PLAY = settings.PLAY_NUM_PER_CLICK


def home(request):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP

    domain = settings.DOMAIN

    h5games = Html5GamesInfo.objects.filter(status=True).order_by('-play', '-like', 'unlike')[:10]
    hots = [h5.data for h5 in h5games]

    h5games = Html5GamesInfo.objects.filter(status=True).order_by('-create_at')[:10]
    news = [h5.data for h5 in h5games]

    return render(request, 'html5games/home.html', dict(hots=hots, news=news, domain=domain, fromApple=fromApple, app_url=app_url))


def play(request, pk=-1):
    try:
        h5game = Html5GamesInfo.objects.get(pk=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
    except:
        h5game = ''
    return render(request, 'html5games/play.html', dict(h5game=h5game))


@xframe_options_exempt
def share(request, pk=-1):
    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(md5=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
        h5game = h5game.data
    except:
        h5game = ''

    if request.mobile:
        meta = request.META['HTTP_USER_AGENT']
        fromWeixin = 'MicroMessenger' in meta
        fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

        app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_WAP

        return render(request, 'html5games/wap_share.html', dict(h5game=h5game, domain=domain, fromApple=fromApple, app_url=app_url))
    else:
        return render(request, 'html5games/pc_share.html', dict(h5game=h5game, domain=domain))


@xframe_options_exempt
def wap_share(request, pk=-1):
    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(pk=pk)
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
        h5game = Html5GamesInfo.objects.get(pk=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
        h5game = h5game.data
    except:
        h5game = ''
    return render(request, 'html5games/pc_share.html', dict(h5game=h5game, domain=domain))


def downloads(request):
    meta = request.META['HTTP_USER_AGENT']
    fromWeixin = 'MicroMessenger' in meta
    fromApple = 'iPhone' in meta or 'iPad' in meta or 'iPod' in meta

    app_url = settings.APP_DOWNLOAD_URL_WEIXIN if fromWeixin else settings.APP_DOWNLOAD_URL_PC

    domain = settings.DOMAIN

    return render(request, 'html5games/downloads.html', dict(domain=domain, fromApple=fromApple, app_url=app_url))
