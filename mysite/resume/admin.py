from django.contrib import admin

from .models import Person, Employment, Company

admin.site.register(Person)
admin.site.register(Employment)
admin.site.register(Company)
