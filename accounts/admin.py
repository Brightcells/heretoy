from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile, Developer


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserCusAdmin(UserAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('profile', 'devtype', 'com_tem_per', 'contact', 'mobile')


admin.site.unregister(User)
admin.site.register(User, UserCusAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Developer, DeveloperAdmin)
