from django.contrib import admin

from apps.models import Ads


# Register your models here.

@admin.register(Ads)
class CommentAdmin(admin.ModelAdmin):
    pass
