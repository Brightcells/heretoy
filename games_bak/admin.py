from django.contrib import admin
from games_bak.models import *


class OpenidInfoAdmin(admin.ModelAdmin):
    list_display = ('openid', 'count', 'token', 'tcount', 'status')


class ReferInfoAdmin(admin.ModelAdmin):
    list_display = ('refer', 'openid', 'refer_ymd')


class CashInfoAdmin(admin.ModelAdmin):
    list_display = ('cash', 'num', 'status')
    search_fields = ('cash', )


class PrizeInfoAdmin(admin.ModelAdmin):
    list_display = ('openid', 'token', 'phone', 'cash', 'num', 'status')


admin.site.register(OpenidInfo, OpenidInfoAdmin)
admin.site.register(ReferInfo, ReferInfoAdmin)
admin.site.register(CashInfo, CashInfoAdmin)
admin.site.register(PrizeInfo, PrizeInfoAdmin)
