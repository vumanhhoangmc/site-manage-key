from django.contrib import admin
from .models import Managekey
# Register your models here.

class ManagekeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'tool', 'owner', 'date_create', 'expiration_date', 'hsd']
    list_filter = ['date_create']
    search_fields = ['key', 'tool', 'owner']

admin.site.register(Managekey, ManagekeyAdmin)
