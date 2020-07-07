from django.contrib import admin

# Register your models here.

from MyLibrary.models import my_library
admin.site.register(my_library)

from MyLibrary.models import authors
admin.site.register(authors)

