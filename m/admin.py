from django.contrib import admin
from .models import MiniUrl

class MiniUrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'code', 'pseudo', 'creation_date']
    list_filter = ('pseudo',)
    date_hierarchy = 'creation_date'
    ordering = ('creation_date',)
    search_fields = ('url',)

admin.site.register(MiniUrl, MiniUrlAdmin)
# Register your models here.
