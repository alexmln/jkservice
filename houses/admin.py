from django.contrib import admin
from houses.models import House, Link


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 3


class HouseAdmin(admin.ModelAdmin):
    inlines = [LinkInLine]

admin.site.register(House, HouseAdmin)