# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from CodeConvert import CodeConvert

import os
import time
import datetime


@xframe_options_exempt
def inverter(request):
    domain = settings.DOMAIN
    return render(request, 'inverter/inverter.htm', dict(domain=domain))
