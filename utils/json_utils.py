# encoding: utf-8

import datetime
import decimal
import json
import logging

from django.utils.timezone import is_aware
from django.http import HttpResponse
from django.utils.functional import Promise

logger = logging.getLogger(__name__)


class LazableJSONEncoder(json.JSONEncoder):
    """Docstring for LazableJSONEncoder """

    def default(self, o):
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(LazableJSONEncoder, self).default(o)


class JsonHttpResponse(HttpResponse):
    """Docstring for JsonHttpResponse """

    def __init__(self, obj, status=200, encode='utf8', *args, **kwargs):
        """@todo: to be defined

        :jsonobj: @todo
        :*args: @todo
        :**kwargs: @todo

        """
        try:
            status = kwargs.get('status', 200)
            content = json.dumps(obj, ensure_ascii=False, cls=LazableJSONEncoder, *args)
        except Exception as err:
            content = u"{0} can't be jsonlized, due to {1}".format(obj, err)
            logger.debug(err)
        finally:
            super(JsonHttpResponse, self).__init__(
                content,
                status=status,
                content_type="application/json;charset=UTF-8",
                # mimetype="text/plain"
            )
