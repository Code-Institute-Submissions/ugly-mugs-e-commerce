from django.contrib import admin
from .models import Mugs

class MugsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Mugs, MugsAdmin)
