from django.contrib import admin
# import your models here
from .models import Job, Note

# Register your models here
admin.site.register(Job)
admin.site.register(Note)

