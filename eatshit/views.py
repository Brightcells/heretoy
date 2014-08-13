# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from eatshit.models import PhotoInfo
from eatshit.form import PhotoInfoModelForm

from utils.graphics import *

from CodeConvert import CodeConvert


def change_list_2_utf8(obj):
    return [dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in dic.items()) for dic in obj]


def change_dict_2_utf8(obj):
    return dict((CodeConvert.Convert2Utf8(k), CodeConvert.Convert2Utf8(v)) for k, v in obj.items())


def home(request):
    ip_addr = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']

    try:
        photo_data = PhotoInfo.objects.filter(ip_addr=ip_addr).order_by('-create_at')[0].data
    except:
        photo_data = ''
    form = PhotoInfoModelForm(initial=photo_data)

    if request.method == "POST":
        form = PhotoInfoModelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.ip_addr = ip_addr
            f.status = True
            f.save()
            if f.image:
                base, ext = os.path.splitext(f.image.name)
                make_thumb(f.image.path, 70, 70)
                f.image.name = base + '_70x70' + ext
                f.save()
            return redirect('/eatshit/eatshit/%s' %(f.name,))

    return render(request, 'eatshit/home.html', dict(form=form, photo_data=photo_data))


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
