# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from data.models import Html5GamesInfo, Html5GamesPlayInfo

from CodeConvert import CodeConvert

import os
import time
import datetime


PLAY = settings.PLAY_NUM_PER_CLICK


def change_list_2_utf8(obj):
    return [dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in dic.items()) for dic in obj]


def change_dict_2_utf8(obj):
    return dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in obj.items())


def home(request):
    h5games = Html5GamesInfo.objects.filter(status=True).order_by('-play', '-like', 'unlike')[:10]
    hots = [h5.data for h5 in h5games]

    h5games = Html5GamesInfo.objects.filter(status=True).order_by('-modify_at')[:10]
    news = [h5.data for h5 in h5games]

    h5gamesplay = Html5GamesPlayInfo.objects.filter().order_by('-modify_at')[:20]
    mes = [h5.data for h5 in h5gamesplay]

    return render(request, 'html5games/home.html', dict(hots=hots, news=news, mes=mes))


def play(request, pk=-1):
    try:
        h5game = Html5GamesInfo.objects.get(pk=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
    except:
        h5game = ''
    return render(request, 'html5games/play.html', dict(h5game=h5game))


def share(request, pk=-1):
    if request.mobile:
        return redirect(reverse('html5games:wap_share', args=[pk,]))
    else:
        return redirect(reverse('html5games:pc_share', args=[pk,]))


def wap_share(request, pk=-1):
    domain = settings.DOMAIN

    try:
        h5game = Html5GamesInfo.objects.get(pk=pk)
        h5game.play += PLAY
        h5game.real_play += 1
        h5game.save()
    except:
        h5game = ''
    return render(request, 'html5games/wap_share.html', dict(h5game=h5game, domain=domain))


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
