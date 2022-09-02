from django.contrib import admin

# Import Book model

from .models import Book,Detail

# Register Book model

admin.site.register(Book)
admin.site.register(Detail)