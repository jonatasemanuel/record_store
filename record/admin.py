from django.contrib import admin
from .models import Credits, Disc


# Register your models here.
class CreditAdmin(admin.ModelAdmin):
    list_display = ('disc', 'artist', 'label', 'release')
  

admin.site.register(Credits, CreditAdmin)
admin.site.register(Disc)