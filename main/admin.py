from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.site_title = 'Celery with Django'
admin.site.site_header = 'CELERY'
