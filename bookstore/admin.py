from django.contrib import admin

from .models import Response

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'response', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ['user', 'response', 'created_at']

admin.site.register(Response, ResponseAdmin)