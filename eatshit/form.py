#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.forms import ModelForm, ChoiceField, ModelChoiceField
from django.forms.widgets import Input, Textarea, ClearableFileInput, URLInput, Select
from django.utils.translation import ugettext_lazy as _

from eatshit.models import PhotoInfo


class PhotoInfoModelForm(ModelForm):
    image = forms.ImageField(
        widget=ClearableFileInput(attrs={'class': 'form-control photo_input', 'autocomplete': 'off', 'placeholder': _('image')}),
        required=False
    )

    name = forms.CharField(
        widget=Input(attrs={'class': 'form-control name_input', 'autocomplete': 'off', 'placeholder': _('name')}),
        required=False
    )

    class Meta:
        model = PhotoInfo
        include = ('image', 'name')

    def clean(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError(_('Must uploda an image or input an image\'s url'))
        else:
            return self.cleaned_data