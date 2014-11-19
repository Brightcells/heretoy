# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


DEV_TYPE = (
    ('company', u'公司'),
    ('team', u'团队'),
    ('person', u'个人'),
)


class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u'帐户'), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))
    password = forms.CharField(label=_(u'密码'), max_length=30, widget=forms.PasswordInput(attrs={'size': 30, }))
    email = forms.EmailField(label=_(u'邮箱'), max_length=30, widget=forms.TextInput(attrs={'size': 30, }), required=False)
    devtype = forms.ChoiceField(label=_(u'开发者类型'), choices=DEV_TYPE, widget=forms.Select(attrs={}))
    com_tem_per = forms.CharField(label=_(u'公司/团队/个人名称'), max_length=255, widget=forms.TextInput(attrs={'size': 30, }))
    contact = forms.CharField(label=_(u'联系人'), max_length=30, widget=forms.TextInput(attrs={'size': 30, }), required=False)
    mobile = forms.CharField(label=_(u'联系电话'), max_length=30, widget=forms.TextInput(attrs={'size': 30, }))

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username__iexact=username)
        if users:
            raise forms.ValidationError(_(u'该帐户已经注册'))
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        emails = User.objects.filter(email__iexact=email)
        if emails:
            raise forms.ValidationError(_(u"该邮箱已经注册"))
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'帐户'), max_length=30, widget=forms.TextInput(attrs={'class': 'login_username', }))
    password = forms.CharField(label=_(u'密码'), max_length=30, widget=forms.PasswordInput(attrs={'class': 'login_password', }))
