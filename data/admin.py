from django.contrib import admin
from data.models import TestTokenInfo, Html5GamesClassifyInfo, Html5GamesInfo, Html5GamesPlayInfo, Html5GamesPlayLog, Html5GamesNailLog, Html5GamesLikeInfo, Html5GamesUnlikeInfo, TopicInfo, TopicGamesInfo, LunbotuInfo

import hashlib

from CodeConvert import CodeConvert as cc


def string2hash(string):
    '''
        @function: change string to hash by using hashlib's md5 method
        @paras: string
        @returns: hexdigest string
    '''
    hash_string = hashlib.md5()
    hash_string.update(string)
    return hash_string.hexdigest()


class TestTokenInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'status')


class Html5GamesClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ('first', 'second')


class Html5GamesInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'md5', 'onshalf', 'screen', 'image', 'descr', 'url', 'play', 'real_play', 'like', 'real_like', 'unlike', 'classify1', 'classify2', 'source', 'sole', 'first_publish', 'boutique', 'version', 'commit', 'language', 'operate', 'status')
    search_fields = ('name', 'md5', 'descr', 'commit')
    list_filter = ('onshalf', 'source', 'version', 'language', 'operate', 'classify1', 'classify2')

    def save_model(self, request, obj, form, change):
        if obj.md5 == '':
            obj.md5 = string2hash(cc.Convert2Utf8('%s: %s' % (obj.pk, obj.name)))
        else:
            pass
        obj.save()


class Html5GamesPlayInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game', 'play', 'nail')


class Html5GamesPlayLogAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game', 'create_at')


class Html5GamesLikeInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game')


class Html5GamesNailLogAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game', 'nail')


class Html5GamesUnlikeInfoAdmin(admin.ModelAdmin):
    list_display = ('token', 'h5game')


class TopicInfoAdmin(admin.ModelAdmin):
    list_display = ('tp', 'name', 'status')


class TopicGamesInfoAdmin(admin.ModelAdmin):
    list_display = ('topic', 'h5game', 'status')


class LunbotuInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image', 'onshalf', 'sort', 'h5game', 'lbt_classify', 'status')


admin.site.register(TestTokenInfo, TestTokenInfoAdmin)
admin.site.register(Html5GamesClassifyInfo, Html5GamesClassifyInfoAdmin)
admin.site.register(Html5GamesInfo, Html5GamesInfoAdmin)
admin.site.register(Html5GamesPlayInfo, Html5GamesPlayInfoAdmin)
admin.site.register(Html5GamesPlayLog, Html5GamesPlayLogAdmin)
admin.site.register(Html5GamesNailLog, Html5GamesNailLogAdmin)
admin.site.register(Html5GamesLikeInfo, Html5GamesLikeInfoAdmin)
admin.site.register(Html5GamesUnlikeInfo, Html5GamesUnlikeInfoAdmin)
admin.site.register(TopicInfo, TopicInfoAdmin)
admin.site.register(TopicGamesInfo, TopicGamesInfoAdmin)
admin.site.register(LunbotuInfo, LunbotuInfoAdmin)
