#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime


def get_safe_now():
    from django.conf import settings
    from django.utils.timezone import utc
    if settings.USE_TZ:
        return datetime.utcnow().replace(tzinfo=utc)
    return datetime.now()
