from django.contrib import admin
from .models import Proffy


class ProffyAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'whatsapp', 'email', 'subject')
    list_display_links = ('fullName',)
    list_per_page = 10
    list_editable = ('whatsapp','subject')


admin.site.register(Proffy, ProffyAdmin)