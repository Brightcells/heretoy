from django.contrib import admin
from eatshit.models import PhotoInfo


class PhotoInfoAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'ip_addr', 'status')


admin.site.register(PhotoInfo, PhotoInfoAdmin)
