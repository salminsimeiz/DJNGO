from django.contrib import admin
from .models import *


@admin.register(Buyer)
class AdminBuyer(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('name', 'balance')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('cost', 'size')
    search_fields = ('title',)
    list_per_page = 20
