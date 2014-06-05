from django.contrib import admin
from houses.models import House, Link, Rso, Damage


class LinkInLine(admin.StackedInline):
    model = Link
    extra = 3


class SroInLine(admin.StackedInline):
    model = Rso
    extra = 1


class DamageInLine(admin.StackedInline):
    model = Damage
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [LinkInLine, SroInLine, DamageInLine]

admin.site.register(House, HouseAdmin)