from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext

from data.models import Html5GamesInfo
from developer.forms import Html5GamesInfoModelForm, Html5GamesInfoUpdateModelForm

from utils import get_safe_now

import re
import urllib
import hashlib

from CodeConvert import CodeConvert as cc


@login_required
def submit_game(request):
    form = Html5GamesInfoModelForm()
    if request.method == 'POST':
        form = Html5GamesInfoModelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.developer = request.user.username
            f.md5 = hashlib.md5(cc.Convert2Utf8('%s: %s' % (f.pk, f.name))).hexdigest()
            f.submit_at = get_safe_now()
            f.save()
            form = Html5GamesInfoModelForm()
            return redirect(reverse('developer:games'))
    return render(request, 'developer/submit_game.html', dict(form=form))


@login_required
def edit_game(request, md5):
    game = get_object_or_404(Html5GamesInfo, md5=md5)
    form = Html5GamesInfoModelForm(initial=model_to_dict(game))
    return render(request, 'developer/edit_game.html', dict(md5=md5, form=form, game=game))


@login_required
def update_game(request, md5):
    game = get_object_or_404(Html5GamesInfo, md5=md5)
    form = Html5GamesInfoUpdateModelForm(request.POST, instance=game)

    if form.is_valid():
        f = form.save(commit=False)
        f.audit = 'audit_ing'
        f.submit_at = get_safe_now()
        f.save()
        return redirect(reverse('developer:games'))
    return render(request, 'developer/edit_game.html', dict(md5=md5, form=form))


@login_required
def games(request):
    domain = settings.DOMAIN

    h5games = Html5GamesInfo.objects.filter(developer=request.user.username).order_by('-modify_at')
    h5games = [h5.info for h5 in h5games]
    return render(request, 'developer/games.html', dict(domain=domain, h5games=h5games))
