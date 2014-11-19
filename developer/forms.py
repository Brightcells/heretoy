# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from data.models import Html5GamesInfo


class Html5GamesInfoModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(Html5GamesInfoModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Html5GamesInfo
        fields = ('name', 'image', 'descr', 'url', 'classify1', 'classify2', 'version', 'language', 'operate', 'screen')

    def clean_image(self):
        image = self.cleaned_data['image']
        if image and False:
            raise forms.ValidationError(_('The width/hegith should be 150'))
        return image

    def clean_url(self):
        url = self.cleaned_data['url']
        urls = Html5GamesInfo.objects.filter(url=url)
        if urls:
            raise forms.ValidationError(_(u'该游戏已经提交'))
        return url


class Html5GamesInfoUpdateModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(Html5GamesInfoUpdateModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Html5GamesInfo
        fields = ('name', 'image', 'descr', 'url', 'classify1', 'classify2', 'version', 'language', 'operate', 'screen')

    def clean_image(self):
        image = self.cleaned_data['image']
        if image and False:
            raise forms.ValidationError(_('The width/hegith should be 150'))
        return image
