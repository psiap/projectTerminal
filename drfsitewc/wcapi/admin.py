from django.contrib import admin

from .models import Statistics, Settings, History
# Register your models here.
admin.site.register(Statistics)
admin.site.register(Settings)
admin.site.register(History)
