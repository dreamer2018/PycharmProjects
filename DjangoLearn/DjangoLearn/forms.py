#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Created by zhoupan on 8/8/16.
"""
from django import forms


class ContactForm(forms.Form):
    shbject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
