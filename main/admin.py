from django.contrib import admin
from .models import ToDo
from .models import toMeet

# Register your models here.
admin.site.register(ToDo)
admin.site.register(toMeet)