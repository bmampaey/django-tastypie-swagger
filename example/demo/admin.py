from django.contrib import admin
from .models import FooModel, BarModel

admin.site.register(FooModel)
admin.site.register(BarModel)
