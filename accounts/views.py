from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseForbidden

from accounts.models import Profile, Developer
from accounts.forms import RegisterForm, LoginForm

import re
import urllib


def get_referer_view(request, default=None):
    '''
    Return the referer view of the current request

    Example:

    def some_view(request):
    ...
    referer_view = get_referer_view(request)
    return HttpResponseRedirect(referer_view, '/accounts/login/')
    '''

    # if the user typed the url directly in the browser's address bar
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    '''
    if referer[0] != request.META.get('SERVER_NAME'):
        return default
    '''

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    return referer


@transaction.atomic
def user_signup(request):
    next = request.GET.get('next', '') or get_referer_view(request, '/')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            devtype = form.cleaned_data['devtype']
            com_tem_per = form.cleaned_data['com_tem_per']
            contact = form.cleaned_data['contact']
            mobile = form.cleaned_data['mobile']

            user = User.objects.create_user(username=username, password=password, email=email)
            profile = Profile.objects.create(user=user)
            developer = Developer.objects.create(profile=profile, devtype=devtype, com_tem_per=com_tem_per, contact=contact, mobile=mobile)

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect(reverse('developer:games'))
    return render(request, 'accounts/signup.html', dict(form=form, next=next))


def user_login(request):
    next = request.GET.get('next', '') or get_referer_view(request, '/')

    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect(reverse('developer:games'))
    return render(request, 'accounts/login.html', dict(form=form, next=next))


def user_logout(request):
    next = request.GET.get('next', '') or get_referer_view(request, '/')
    logout(request)
    return redirect(next)
