# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from CodeConvert import CodeConvert

import os
import time
import json
import urllib
import datetime
import requests


@xframe_options_exempt
def yiguankoudai(request):
    domain = settings.DOMAIN
    return render(request, 'yiguankoudai/index.html', dict(domain=domain))


@xframe_options_exempt
def yiguankoudai2(request):
    domain = settings.DOMAIN
    return render(request, 'yiguankoudai2/index.html', dict(domain=domain))


@xframe_options_exempt
def yiguankoudai3(request):
    domain = settings.DOMAIN
    return render(request, 'yiguankoudai3/index.html', dict(domain=domain))
