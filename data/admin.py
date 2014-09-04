from django.contrib import admin
from data.models import TestTokenInfo, Html5GamesClassifyInfo, Html5GamesInfo, Html5GamesPlayInfo, Html5GamesPlayLog, Html5GamesLikeInfo, Html5GamesUnlikeInfo


class TestTokenInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'status')


class Html5GamesClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ('first', 'second')


class Html5GamesInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'onshalf', 'image', 'descr', 'url', 'play', 'real_play', 'like', 'real_like', 'unlike', 'classify1', 'classify2', 'source', 'version', 'commit', 'language', 'operate', 'status')
    search_fields = ('name', 'descr', 'commit')
    list_filter = ('source', 'version', 'language', 'operate', 'classify1', 'classify2')


class Html5GamesPlayInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game', 'play')


class Html5GamesPlayLogAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game')


class Html5GamesLikeInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game')


class Html5GamesUnlikeInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game')


admin.site.register(TestTokenInfo, TestTokenInfoAdmin)
admin.site.register(Html5GamesClassifyInfo, Html5GamesClassifyInfoAdmin)
admin.site.register(Html5GamesInfo, Html5GamesInfoAdmin)
admin.site.register(Html5GamesPlayInfo, Html5GamesPlayInfoAdmin)
admin.site.register(Html5GamesPlayLog, Html5GamesPlayLogAdmin)
admin.site.register(Html5GamesLikeInfo, Html5GamesLikeInfoAdmin)
admin.site.register(Html5GamesUnlikeInfo, Html5GamesUnlikeInfoAdmin)
