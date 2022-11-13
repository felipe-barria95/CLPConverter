from clpconverter.converter.models import CLPPerUFModel
from django.contrib import admin

@admin.register(CLPPerUFModel)
class CLPPerUFAdmin(admin.ModelAdmin):
    list_display = ['date', 'value']