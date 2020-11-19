from django.contrib import admin
from .models import Mug

class MugsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'date',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Mug, MugsAdmin)
