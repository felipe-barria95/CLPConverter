from clpconverter.converter.models import CLPPerUFModel
from django.contrib import admin

@admin.register(CLPPerUFModel)
class CLPPerUFAdmin(admin.ModelAdmin):
    list_display = ['date', 'value']

    actions=["fix_value"]

    def fix_value(self, request, query):
        values = CLPPerUFModel.objects.all()
        for v in values:
            if 1000000 < v.value < 10000000:
                v.value = v.value/100
            elif 100000 < v.value< 1000000:
                v.value= v.value /10
            v.save()