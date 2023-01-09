from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'account')
    search_fields = ['account', ]
    list_filter = ('id', 'account')
    list_display_links = ('account', 'id')
    search_help_text = 'search on here'




admin.site.register(Profile,ProfileAdmin)
