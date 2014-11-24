#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from games_bak.models import *

from CodeConvert import CodeConvert

import os
import time
import json
import urllib
import datetime
import requests


WEIXIN = settings.WEIXIN


@xframe_options_exempt
def inverter(request):
    domain = settings.DOMAIN
    return render(request, 'inverter/inverter.htm', dict(domain=domain))


@xframe_options_exempt
def inverter2(request):
    domain = settings.DOMAIN
    return render(request, 'inverter/inverter2.htm', dict(domain=domain))


@xframe_options_exempt
def colornot(request):
    domain = settings.DOMAIN
    return render(request, 'colornot/colornot.htm', dict(domain=domain))


@xframe_options_exempt
def airplane(request):
    domain = settings.DOMAIN
    return render(request, 'airplane/airplane.htm', dict(domain=domain))


@xframe_options_exempt
def FarmInvaders(request):
    domain = settings.DOMAIN
    return render(request, 'FarmInvaders/FarmInvaders.htm', dict(domain=domain))


@xframe_options_exempt
def Jumping(request):
    domain = settings.DOMAIN
    return render(request, 'Jumping/Jumping.htm', dict(domain=domain))


@xframe_options_exempt
def yzdmx(request):
    domain = settings.DOMAIN
    return render(request, 'yzdmx/yzdmx.htm', dict(domain=domain))


@xframe_options_exempt
def kdxyx(request):
    refer = request.GET.get('refer', '')
    openid = request.GET.get('openid', '')
    if refer == openid:
        pass
    else:
        try:
            oi = OpenidInfo.objects.get(openid=refer, status=True)
            oi.refer += 1
            oi.count += oi.refer % 2
            oi.save()
        except:
            pass
    oi, created = OpenidInfo.objects.get_or_create(openid=openid)

    domain = settings.DOMAIN
    return render(request, '58aydzz/58kdxyx.htm', dict(domain=domain, openid=openid, count=oi.count))


@xframe_options_exempt
def aydzz(request):
    openid = request.GET.get('openid', '')

    can = True
    count = 0
    if openid:
        try:
            oi = OpenidInfo.objects.get(openid=openid, status=True)
            if oi.count:
                oi.count -= 1
                oi.save()
            else:
                can = False
            count = oi.count
        except:
            can = False
    else:
        can = False

    domain = settings.DOMAIN
    if can:
        return render(request, '58aydzz/58aydzz.htm', dict(domain=domain, can=can, openid=openid, count=count))
    else:
        return redirect(reverse('games_bak:share', args=(0, )) + '?openid=' + openid)


@xframe_options_exempt
def bind_phone(request, cash):
    openid = request.GET.get('openid', '')
    try:
        phone = PrizeInfo.objects.filter(openid=openid)[0].phone
    except:
        phone = ''
    domain = settings.DOMAIN
    return render(request, '58aydzz/bindphone.htm', dict(domain=domain, openid=openid, phone=phone, cash=cash))


@xframe_options_exempt
def get_cash(request, cash):
    openid = request.GET.get('openid', '')
    phone = request.POST.get('phone', '')

    if len(phone) == 11:
        try:
            try:
                createtime = PrizeInfo.objects.filter(openid=openid, phone=phone)[0].create_at
                td = timezone.now() - createtime
                seconds = int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6)
            except:
                seconds = 100

            if seconds > 60:
                c = CashInfo.objects.filter(num=cash, status=True)[0]
                c.status = False
                c.save()
                try:
                    data = {'phone': phone, 'conpon': c.cash}
                    req = requests.post(settings.CONPON, data)
                    p = PrizeInfo.objects.create(openid=openid, phone=phone, cash=c.cash, num=cash)
                except:
                    c.status = True
                    c.save()
            else:
                pass
        except:
            pass
    else:
        pass

    domain = settings.DOMAIN
    try:
        count = OpenidInfo.objects.get(openid=openid, status=True).count
    except:
        count = 0
    total_count = PrizeInfo.objects.filter(phone=phone, status=True).count()
    try:
        total_cash = PrizeInfo.objects.filter(phone=phone, status=True).annotate(total_cash=Sum('num'))[0].total_cash
    except:
        total_cash = 0
    try:
        phone = phone[:3] + '****' + phone[-4:]
    except:
        pass
    return render(request, '58aydzz/success.htm', dict(domain=domain, openid=openid, phone=phone, count=count, cash=cash, total_count=total_count, total_cash=total_cash))


@xframe_options_exempt
def share(request, cash):
    openid = request.GET.get('openid', '')
    domain = settings.DOMAIN
    return render(request, '58aydzz/share.htm', dict(domain=domain, openid=openid, cash=cash))


def retry(request):
    openid = request.GET.get('openid', '')
    status = True
    if openid:
        try:
            oi = OpenidInfo.objects.get(openid=openid, status=True)
            if oi.count:
                oi.count -= 1
                oi.save()
            else:
                status = False
            count = oi.count
        except:
            status = False
    else:
        status = False
    return HttpResponse(json.dumps(dict(status=status, errmsg='')))


def refresh(request):
    OpenidInfo.objects.filter(count=0).update(count=1)
    return HttpResponse('hello world')
