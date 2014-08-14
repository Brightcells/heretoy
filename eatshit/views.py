# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from eatshit.models import PhotoInfo
from eatshit.form import PhotoInfoModelForm

from utils.graphics import *

from CodeConvert import CodeConvert

import os
import time
import datetime


def change_list_2_utf8(obj):
    return [dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in dic.items()) for dic in obj]


def change_dict_2_utf8(obj):
    return dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in obj.items())


def get_path():
    today = datetime.datetime.today()
    timestamp = str(time.time())
    return 'heretoy/image/{year}{month}/{timestamp}.png'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp
    )


def home(request):
    form = PhotoInfoModelForm()

    if request.method == "POST":
        form = PhotoInfoModelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.status = True
            f.save()
            if f.image:
                base, ext = os.path.splitext(f.image.name)
                make_thumb(f.image.path, 70, 70)
                f.image.name = base + '_70x70' + ext
            else:
                text = CodeConvert.Convert2Unicode(f.name)[-1]
                path = get_path()
                make_pic(text, os.path.join(settings.MEDIA_ROOT, path), 70, 70)
                f.image.name = path
            f.save()
            return redirect(reverse('eatshit:eatshit', kwargs={'name': f.name}))

    return render(request, 'eatshit/home.html', dict(form=form, photo_data=''))


def eatshit(request, name='admin'):
    try:
        photo_data = PhotoInfo.objects.filter(name=name).exclude(image='').order_by('-create_at')[0].data
    except:
        try:
            photo_data = PhotoInfo.objects.filter(name=name).order_by('-create_at')[0].data
        except:
            photo_data = ''

    return render(request, 'eatshit/mix_snake.html', dict(photo_data=photo_data))


def share(request, name='admin'):
    share = request.GET.get('achieve', '')

    try:
        photo_data = PhotoInfo.objects.filter(name=name).exclude(image='').order_by('-create_at')[0].data
    except:
        try:
            photo_data = PhotoInfo.objects.filter(name=name).order_by('-create_at')[0].data
        except:
            photo_data = ''

    return render(request, 'eatshit/share.html', dict(share=share, photo_data=photo_data))
